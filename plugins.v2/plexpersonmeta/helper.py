"""
helper.py

这个模块定义了用于存储媒体项目信息的 `RatingInfo` 数据类以及缓存、限流等装饰器
"""
import functools
import inspect
from dataclasses import dataclass
from typing import Optional

from cachetools.keys import hashkey
from app.core.cache import Cache
from app.log import logger


@dataclass
class RatingInfo:
    """
    媒体项目信息的数据类
    """
    key: Optional[str] = None  # 媒体项目的唯一标识
    type: Optional[str] = None  # 媒体项目的类型（例如：电影、电视剧）
    title: Optional[str] = None  # 媒体项目的标题
    search_title: Optional[str] = None  # 用于搜索的标题
    tmdbid: Optional[int] = None  # TMDB 的唯一标识，可选


def get_cache_key(func, args, kwargs) -> str:
    """
    根据函数和参数生成缓存键

    :param func: 函数对象
    :param args: 位置参数
    :param kwargs: 关键字参数
    :return: 缓存键
    """
    signature = inspect.signature(func)
    # 绑定传入的参数并应用默认值
    bound = signature.bind(*args, **kwargs)
    bound.apply_defaults()
    # 忽略第一个参数，如果它是实例(self)或类(cls)
    parameters = list(signature.parameters.keys())
    if parameters and parameters[0] in ("self", "cls"):
        bound.arguments.pop(parameters[0], None)
    # 按照函数签名顺序提取参数值列表
    keys = [
        bound.arguments[param] for param in signature.parameters if param in bound.arguments
    ]
    # 使用有序参数生成缓存键
    return f"{func.__name__}_{hashkey(*keys)}"


def cache_with_logging(region, source):
    """
    装饰器，用于在函数执行时处理缓存逻辑和日志记录。
    :param region: 缓存区，用于存储和检索缓存数据
    :param source: 数据来源，用于日志记录（例如：PERSON 或 MEDIA）
    :return: 装饰器函数
    """

    def decorator(func):

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            cache = Cache()
            key = get_cache_key(func, args, kwargs)
            exists_cache = cache.exists(key=key, region=region)
            if exists_cache:
                value = cache.get(key=key, region=region)
                if value is not None:
                    if source == "PERSON":
                        logger.info(f"从缓存中获取到 {source} 人物信息")
                    else:
                        logger.info(f"从缓存中获取到 {source} 媒体信息: {kwargs.get('title', 'Unknown Title')}")
                    return value
                return None

            # 执行被装饰的函数
            result = func(*args, **kwargs)

            if result is None:
                # 如果结果为 None，说明触发限流或网络等异常，缓存5分钟，以免高频次调用
                cache.set(key, "None", ttl=60 * 5, region=region, maxsize=100000)
            else:
                # 结果不为 None，使用默认 TTL 缓存
                cache.set(key, result, ttl=60 * 60 * 24 * 3, region=region, maxsize=100000)

            return result

        return wrapped_func

    return decorator
