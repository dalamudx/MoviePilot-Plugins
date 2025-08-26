# MoviePilot-Plugins

MoviePilot插件集合 - 整合了三个优秀的插件仓库，部分插件进行了适配修改。

## 📦 包含的插件仓库

本项目整合了以下三个优秀的MoviePilot插件仓库：

### 1. [DDS-Derek](https://github.com/DDS-Derek/MoviePilot-Plugins)
- **作者**: DDS-Derek
- **特色**: 专注于流媒体发现和115网盘相关插件
- **主要插件**: P115StrmHelper、各种发现插件等

### 2. [InfinityPacer](https://github.com/InfinityPacer/MoviePilot-Plugins)
- **作者**: InfinityPacer  
- **特色**: 丰富的Plex增强插件和系统管理工具
- **主要插件**: Plex相关插件、刷流管理、系统诊断等

### 3. [thsrite](https://github.com/thsrite/MoviePilot-Plugins)
- **作者**: thsrite
- **特色**: 全面的媒体库管理和云盘工具
- **主要插件**: Emby增强、云盘管理、媒体处理等


## 📁 目录结构

整合后的目录结构如下：

```
MoviePilot-Plugins/
├── plugins/           # v1版本插件
├── plugins.v2/        # v2版本插件
├── icons/             # 插件图标
├── docs/              # 插件文档
├── frontend/          # 前端文件
├── data/              # 数据文件
├── images/            # 图片资源
├── modules/           # 子模块目录
│   ├── DDS-Derek/
│   ├── InfinityPacer/
│   └── thsrite/
├── package.json       # v1插件包配置
├── package.v2.json    # v2插件包配置
└── README.md          # 本文件
```

## 🔧 插件分类

### 媒体发现类
- 各种流媒体平台发现插件
- 番剧、电影、电视剧发现

### Plex增强类  
- Plex自动语言设置
- Plex版本管理
- Plex本地化增强
- Plex匹配优化

### Emby增强类
- Emby演员同步
- Emby弹幕支持
- Emby元数据刷新
- Emby收藏排序

### 云盘管理类
- 115网盘助手
- CloudDrive管理
- 云盘监控
- 文件同步

### 系统工具类
- 插件管理器
- 系统诊断
- 流量助手
- 定时任务

### 下载增强类
- 刷流管理
- 种子分类
- 下载监控
- 命中率优化

## ⚠️ 注意事项

1. **插件兼容性**: 请确保插件与你的MoviePilot版本兼容
2. **配置备份**: 更新前请备份重要的插件配置
3. **依赖检查**: 某些插件可能需要额外的依赖包
4. **权限设置**: 确保MoviePilot有足够的权限访问插件文件

## 🤝 贡献

欢迎提交Issue和Pull Request来改进本项目。

### 贡献方式

1. Fork本仓库
2. 创建特性分支
3. 提交更改
4. 发起Pull Request

## 📄 许可证

本项目遵循MIT许可证，详见 [LICENSE](LICENSE) 文件。


## 🙏 致谢

感谢以下开发者的优秀工作：

- [DDS-Derek](https://github.com/DDS-Derek) - DDS-Derek插件仓库
- [InfinityPacer](https://github.com/InfinityPacer) - InfinityPacer插件仓库
- [thsrite](https://github.com/thsrite) - thsrite插件仓库

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 提交Issue到本仓库
- 或者到对应的原仓库寻求帮助

---

**注意**: 本仓库仅为整合仓库，具体插件的功能和使用方法请参考各个原仓库的文档。
