import asyncio
import logging
import sys

import base64
from io import BytesIO
from manager_agent.tools.descrever_uma_img import descreverimagem
from os import getenv

from runner import conversar

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
import dotenv

dotenv.load_dotenv()

TOKEN = getenv("TELEGRAM_TOKEN")


dp = Dispatcher()


@dp.message()
async def echo_handler(message: Message) -> None:
    # try:
    print(message.chat.id)
    id = message.from_user.id
    if message.text:
        await bot.send_chat_action(message.chat.id, 'typing')
        # If the message is text, we can use it directly
        response = await conversar(message.text, str(id))
        await message.answer(response)
    elif message.photo:
        await bot.send_chat_action(message.chat.id, 'upload_photo')

        photo = message.photo[-1]
        file = await bot.get_file(photo.file_id)
        file_data = await bot.download(file.file_id)

        image_bytes = file_data.read()
        base64_str = base64.b64encode(image_bytes).decode('utf-8')
        descricao = descreverimagem(base64_str)
        print(descricao)

        response = await conversar(descricao, str(id))
        await message.answer(response)

    # elif message.document and message.document.mime_type.startswith("image/"):
    #     await bot.send_chat_action(message.chat.id, 'upload_photo')

    #     file = await bot.get_file(message.document.file_id)
    #     file_data = await bot.download(file.file_id)

    #     image_bytes = file_data.read()
    #     base64_str = base64.b64encode(image_bytes).decode('utf-8')

    #     response = await conversar(base64_str, str(id))
    #     await message.answer(response)

    else:
        await message.answer("Envie uma mensagem de texto ou imagem.")


async def main() -> None:
    global bot
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())