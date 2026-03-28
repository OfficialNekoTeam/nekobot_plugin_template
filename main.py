from packages.decorators import command, event_handler, plugin
from packages.plugins import BasePlugin


@plugin(
    name="nekobot_plugin_example",
    version="1.0.0",
    description="NekoBot 插件示例",
)
class NekoPluginExample(BasePlugin):
    @command(name="hello", aliases=("hi",), description="打招呼")
    async def cmd_hello(self, payload: dict) -> None:
        args: list[str] = payload.get("command_args", [])  # type: ignore[assignment]
        name = args[0] if args else "World"
        await self.context.reply(f"Hello, {name}!")

    @event_handler(event="message.group", description="群消息处理示例")
    async def on_group_message(self, payload: dict) -> None:
        text = payload.get("plain_text", "")
        # 示例：监听特定关键词
        if isinstance(text, str) and "ping" in text.lower():
            await self.context.reply("pong")
