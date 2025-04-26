from nonebot_plugin_alconna import Image, UniMessage

from .config import IMAGE_DIR


async def get_image_segment(image_name):
    image_path = IMAGE_DIR / image_name
    return Image(path=image_path) if image_path.exist() else None


async def send_images(images):
    if isinstance(images, list):
        for img_file in images:
            if img_seg := await get_image_segment(img_file):
                await UniMessage(img_seg).send(reply_to=True)
            else:
                await UniMessage(f"图片 {img_file} 不存在。").send(reply_to=True)
    elif isinstance(images, str):
        if img_seg := await get_image_segment(images):
            await UniMessage(img_seg).send(reply_to=True)
        else:
            await UniMessage(f"图片 {images} 不存在。").send(reply_to=True)
