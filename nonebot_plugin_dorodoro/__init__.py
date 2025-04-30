from nonebot.plugin import PluginMetadata
from nonebot_plugin_alconna import Alconna, Args, Arparma, CommandMeta, Text, on_alconna
from nonebot_plugin_uninfo import Session, UniSession

from .game_logic import (
    get_next_node,
    get_node_data,
    is_end_node,
    update_user_state,
    user_game_state,
)
from .image_handler import send_images

__plugin_meta__ = PluginMetadata(
    name="doro大冒险",
    description="一个基于文字冒险的游戏插件",
    type="application",
    usage="""
    使用方法：
    doro ：开始游戏
    choose <选项> 或 选择 <选项>：在游戏中做出选择
    """,
    homepage="https://github.com/ATTomatoo/dorodoro",
    supported_adapters={"~onebot.v11"},
    extra={
        "author": "ATTomatoo",
        "version": "1.5.3",
        "priority": 5,
        "plugin_type": "NORMAL",
    },
)

# 定义doro命令
doro = on_alconna(Alconna("doro"), aliases={"多罗"}, priority=5, block=True)


@doro.handle()
async def handle_doro(session: Session = UniSession()):
    user_id = session.user.id
    start_node = "start"
    await update_user_state(user_id, start_node)
    if start_data := await get_node_data(start_node):
        msg = start_data["text"] + "\n"
        for key, opt in start_data.get("options", {}).items():
            msg += f"{key}. {opt['text']}\n"

        await send_images(start_data.get("image"))
        await doro.send(Text(msg), reply_to=True)
    else:
        await doro.send(Text("游戏初始化失败，请联系管理员。"), reply_to=True)


# 定义choose命令
choose = on_alconna(
    Alconna("choose", Args["c", str], meta=CommandMeta(compact=True)),
    aliases={"选择"},
    priority=5,
    block=True,
)


@choose.handle()
async def handle_choose(p: Arparma, session: Session = UniSession()):
    user_id = session.user.id
    if user_id not in user_game_state:
        await choose.finish(
            Text("你还没有开始游戏，请输入 /doro 开始。"), reply_to=True
        )

    choice = p.query("c")
    assert isinstance(choice, str)
    choice = choice.upper()
    current_node = user_game_state[user_id]

    next_node = await get_next_node(current_node, choice)
    if not next_node:
        await choose.finish(Text("无效选择，请重新输入。"), reply_to=True)

    next_data = await get_node_data(next_node)
    if not next_data:
        await choose.finish(Text("故事节点错误，请联系管理员。"), reply_to=True)

    await update_user_state(user_id, next_node)

    msg = next_data["text"] + "\n"
    for key, opt in next_data.get("options", {}).items():
        msg += f"{key}. {opt['text']}\n"

    await send_images(next_data.get("image"))

    if await is_end_node(next_data):
        await choose.send(Text(msg + "\n故事结束。"), reply_to=True)
        user_game_state.pop(user_id, None)
    else:
        await choose.finish(Text(msg), reply_to=True)
