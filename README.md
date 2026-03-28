# NekoBot Plugin Example

这是一个 NekoBot 插件的示例，开发者可以使用此仓库作为模板来开发自己的插件。

## 插件结构

```
my_plugin/
    __init__.py      # 框架发现入口，只做 re-export
    main.py          # 插件逻辑，@plugin / @command / @event_handler 全在这里
    requirements.txt # 可选，第三方依赖
    metadata.yaml    # 插件元信息
    README.md
```

## 快速开始

1. 使用此仓库作为模板创建你的插件仓库

2. 将插件放入 NekoBot 插件目录：

```bash
cd /path/to/nekobot/data/plugins
git clone https://github.com/your/plugin_repo.git
```

3. 在 NekoBot 中加载插件（自动扫描目录）或手动加载：

```python
reloader.load_directory("data/plugins")
```

## 插件开发

### metadata.yaml

```yaml
name: my_plugin           # 唯一标识符，需与 @plugin(name=) 一致
display_name: 我的插件
version: 1.0.0
description: 插件描述
author: yourname
repository: https://github.com/you/my_plugin
tags:
  - utility
nekobot_version: ">=0.1.0"
support_platforms:
  - onebot_v11
```

### main.py

```python
from packages.decorators import command, event_handler, plugin
from packages.plugins import BasePlugin


@plugin(name="my_plugin", version="1.0.0", description="插件描述")
class MyPlugin(BasePlugin):

    @command(name="hello", aliases=("hi",), description="打招呼")
    async def cmd_hello(self, payload: dict) -> None:
        args = payload.get("command_args", [])
        name = args[0] if args else "World"
        await self.context.reply(f"Hello, {name}!")

    @event_handler(event="message.group", description="群消息处理")
    async def on_group_message(self, payload: dict) -> None:
        text = payload.get("plain_text", "")
        if isinstance(text, str) and "ping" in text.lower():
            await self.context.reply("pong")
```

### __init__.py

```python
from .main import MyPlugin

__all__ = ["MyPlugin"]
```

## 相关链接

- [NekoBot 插件开发文档](https://docs.nekolook.com/plugins/intro)
- [NekoBot 插件商店](https://store.nekolook.com)
- [提交插件](https://store.nekolook.com/plugins/publish)
