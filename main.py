import asyncio
import logging


from aiogram import Bot, Dispatcher,  types, F
from aiogram.filters import CommandStart
from buttons import *


BOT_TOKEN = "Your Bot Token"

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")



# for start handler
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=f"<b>Hello, {message.from_user.full_name}!</b>",
        reply_markup= lang
    )



# for keyboardbutton handler
@dp.message(F.text=="O'zbekcha")
async def lang_func(message: types.Message):
    await message.answer(
        text="<b>Dasturlash tilini tanlang...</b>",
        reply_markup=prog_button
    )


# for inlinekeyboardbutton handler
@dp.callback_query(lambda c: c.data == 'python')
async def lang_func2(c: types.CallbackQuery):
    await c.message.answer(
        text="<code>print('Hello world')</code>"
    )


@dp.message()
async def echo_message(message: types.Message):
    await message.answer(
        text=message.text
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())