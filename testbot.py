import sqlite3
import asyncio
import webbrowser
import sys
import logging
import aiogram


from aiogram import Bot, Dispatcher, html, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

TOKEN= '6685205242:AAHn-UfQGY8y6NJSoKO0GDse6X1xw9uxhVU'

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    user_id = message.from_user.id
    username = message.chat.username

    inline_btn = InlineKeyboardMarkup(inline_keyboard=[
                                      [InlineKeyboardButton(text='Join Community', url='https://t.me/SpaceM_crypto')]
    ])
    welcome_text = (f"<b>Hi,{username}</b>,\nSpaceM. The world's first marketing crypto agency.Space is an infinite expanse. "
                    f"\nThis is the kind of space you will get for your ideas, projects, and ventures.)"
                    f"\nInstant processing, fast payments, convenience, audience - all of this and much more is what we are about. You can achieve all this with our help."
                    f"\nJoin us and create a revolution in the marketing industry together. Let's change this world together!"
    )

    # photo_url = 'https://drive.google.com/file/d/1n2679F1ORI8nEdyzuOmxq6xmb50YBu2C/view?usp=sharing'

    await message.answer(text=welcome_text, reply_markup=inline_btn)


async def main() -> None:
    bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



