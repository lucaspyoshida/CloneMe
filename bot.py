import asyncio
import logging
import sys
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
    else:
        # If the message is not text, we can convert it to a string
        response = str(message)
    # await message.send_copy(chat_id=message.chat.id)
    # await message.answer(f"ID do remetente: {message.from_user.id}")
    # except TypeError:
    #     # But not all the types is supported to be copied so need to handle it
    #     await message.answer("Nice try!")


async def main() -> None:
    global bot
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())