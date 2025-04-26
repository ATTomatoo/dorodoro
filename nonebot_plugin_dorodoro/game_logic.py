try:
    import ujson as json
except ImportError:
    import json
from pathlib import Path
import random

import aiofiles

# 构造 story_data.json 的完整路径
story_data_path = Path(__file__).parent / "story_data.json"

# 使用完整路径打开文件
STORY_DATA = {}

async def load_story_data():
    """异步加载故事数据"""
    async with aiofiles.open(story_data_path, encoding="utf-8") as f:
        content = await f.read()
        global STORY_DATA
        STORY_DATA = json.loads(content)


user_game_state = {}


async def get_next_node(current_node, choice):
    data = STORY_DATA.get(current_node, {})
    options = data.get("options", {})
    if choice not in options:
        return None

    next_node = options[choice]["next"]
    if isinstance(next_node, list):  # 随机选项
        rand = random.random()
        cumulative = 0.0
        for item in next_node:
            cumulative += item["probability"]
            if rand <= cumulative:
                return item["node"]
    return next_node


async def update_user_state(user_id, next_node):
    user_game_state[user_id] = next_node


async def get_node_data(node):
    return STORY_DATA.get(node)


async def is_end_node(node_data) -> bool:
    return node_data.get("is_end", False)
