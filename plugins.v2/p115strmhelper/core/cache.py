from typing import List, Dict, MutableMapping, Optional
from time import time

from cachetools import TTLCache as MemoryTTLCache

from app.core.cache import Cache, LRUCache


class IdPathCache:
    """
    文件路径ID缓存
    """

    def __init__(self, maxsize=128):
        self.id_to_dir = LRUCache(
            region="p115strmhelper_id_path_cache_id_to_dir",
            maxsize=maxsize,
        )
        self.dir_to_id = LRUCache(
            region="p115strmhelper_id_path_cache_dir_to_id",
            maxsize=maxsize,
        )

    def add_cache(self, id: int, directory: str):
        """
        添加缓存
        """
        self.id_to_dir.set(key=str(id), value=directory)
        self.dir_to_id.set(key=directory, value=str(id))

    def get_dir_by_id(self, id: int) -> Optional[str]:
        """
        通过 ID 获取路径

        return: str | None
        """
        return self.id_to_dir.get(str(id))

    def get_id_by_dir(self, directory: str) -> Optional[int]:
        """
        通过路径获取 ID

        return: int | None
        """
        _id = self.dir_to_id.get(directory)
        if _id is None:
            return None
        try:
            return int(_id)
        except ValueError:
            return None

    def clear(self):
        """
        清空所有缓存
        """
        self.id_to_dir.clear()
        self.dir_to_id.clear()


class PanTransferCache:
    """
    网盘整理缓存
    """

    def __init__(self):
        self.delete_pan_transfer_list = []
        self.creata_pan_transfer_list = []
        self.top_delete_pan_transfer_list: Dict[str, List] = {}


class LifeEventCache:
    """
    生活事件监控缓存
    """

    def __init__(self):
        self.create_strm_file_dict: MutableMapping[str, List] = MemoryTTLCache(
            maxsize=1_000_000, ttl=600
        )


class R302Cache:
    """
    302 跳转缓存
    """

    def __init__(self, maxsize=8096):
        """
        初始化缓存

        参数:
        maxsize (int): 缓存可以容纳的最大条目数
        """
        self._cache = Cache(maxsize=maxsize)
        self.region = "p115strmhelper_r302_cache"

    def set(self, pick_code, ua_code, url, expires_time):
        """
        向缓存中添加一个URL，并为其设置独立的过期时间。

        参数:
        pick_code (str): 第一层键
        ua_code (str): 第二层键
        url (str): 需要缓存的URL
        expires_time (int): 过期时间
        """
        self._cache.set(
            key=f"{pick_code}○{ua_code}",
            value=url,
            ttl=int(expires_time - time()),
            region=self.region,
        )

    def get(self, pick_code, ua_code) -> Optional[str]:
        """
        从缓存中获取一个URL，如果它存在且未过期

        参数:
        pick_code (str): 第一层键
        ua_code (str): 第二层键

        return: str | None
        str: 如果URL存在且未过期，则返回该URL
        None: 如果URL不存在或已过期
        """
        return self._cache.get(key=f"{pick_code}○{ua_code}", region=self.region)

    def count_by_pick_code(self, pick_code) -> int:
        """
        计算与指定 pick_code 匹配的缓存条目数量。

        参数:
        pick_code (str): 要匹配的第一层键

        return: int
        int: 匹配的缓存条目数量
        """
        count = 0
        for key_str, _ in self._cache.items(region=self.region):
            key = key_str.split("○")
            if key[0] == pick_code:
                count += 1
        return count

    def clear(self):
        """
        清空所有缓存
        """
        self._cache.clear(region=self.region)


idpathcacher = IdPathCache(maxsize=4096)
pantransfercacher = PanTransferCache()
lifeeventcacher = LifeEventCache()
r302cacher = R302Cache(maxsize=8096)
