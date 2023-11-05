from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup



lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'zbekcha")
        ],
        [
            KeyboardButton(text="Russcha")
        ]
    ],
    resize_keyboard=True
)

prog_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python", callback_data="python")
        ],
        [
            InlineKeyboardButton(text="C++", callback_data='cpp')
        ]
    ],
   
)
