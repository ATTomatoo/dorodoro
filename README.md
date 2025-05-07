# Dorodoro 文字冒险游戏插件

![NoneBot Plugin](https://img.shields.io/badge/NoneBot%20Plugin-Dorodoro-blue)
![Version](https://img.shields.io/badge/Version-1.5.7-green)
![License](https://img.shields.io/badge/License-AGPL--3.0-orange)

Dorodoro 是一个基于 NoneBot2 框架的文字冒险游戏插件，提供交互式故事体验。

## 功能特性

- 交互式文字冒险游戏体验
- 支持分支剧情选择
- 可配合图片展示增强游戏体验
- 多用户独立游戏进度保存

## 安装方法

1. nb-cli安装（推荐）
在bot配置文件同级目录下执行以下命令：
   ```bash
   nb plugin install nonebot-plugin-dorodoro
   ```
2. 使用 pip 安装插件：
   ```bash
   pip install nonebot-plugin-dorodoro
   ```
打开 nonebot2 项目的 bot.py 文件, 在其中写入
nonebot.load_plugin('nonebot_plugin_dingzhen')
当然，如果是默认nb-cli创建的nonebot2的话，在bot路径pyproject.toml的[tool.nonebot]的plugins中添加nonebot_plugin_dingzhen即可。

## 使用方法
开始游戏
<br />`doro` 
<br />做出选择
<br />`choose <选项> `或` 选择 <选项>`

## 贡献指南
欢迎提交 Issue 或 Pull Request 来改进本插件。

# 许可证
本项目采用 AGPL-3.0 许可证。详见 LICENSE 文件。
原项目 [doro_ending](https://github.com/ttq7/doro_ending) 采用 AGPL-3.0 许可证。
