from .. import loader, utils
import io
from PIL import Image, ImageOps
from telethon.tl.types import DocumentAttributeFilename
import logging

logger = logging.getLogger(__name__)


def register(cb):
    cb(WEBPtoPNGMod())


@loader.tds
class WEBPtoPNGMod(loader.Module):
    strings = {
        "name": "Converter"
    }

    async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def wtpcmd(self, message):
        reply_message = await message.get_reply_message()
        image = io.BytesIO()
        await self.client.download_media(reply_message.media.document, image)
        image = Image.open(image)
        image_stream = io.BytesIO()
        image_stream.name = "png.png"
        image.save(image_stream, "PNG")
        image_stream.seek(0)
        await self.client.delete_messages(message.to_id, message.id)
        await self.client.send_file(message.to_id, image_stream, force_document=True)

    async def ptwcmd(self, message):
        reply_message = await message.get_reply_message()
        image = io.BytesIO()
        await self.client.download_media(reply_message.media, image)
        image = Image.open(image)
        image_stream = io.BytesIO()
        image_stream.name = "webp.webp"
        image.save(image_stream, "WEBP")
        image_stream.seek(0)
        await self.client.delete_messages(message.to_id, message.id)
        await self.client.send_file(message.to_id, image_stream, force_document=False)

    async def jtpcmd(self, message):
        reply_message = await message.get_reply_message()
        image = io.BytesIO()
        await self.client.download_media(reply_message.media, image)
        image = Image.open(image).convert("RGB")
        image_stream = io.BytesIO()
        image_stream.name = "10_из_10шакалов.png"
        image.save(image_stream, "PNG")
        image_stream.seek(0)
        await self.client.delete_messages(message.to_id, message.id)
        await self.client.send_file(message.to_id, image_stream, force_document=True)



