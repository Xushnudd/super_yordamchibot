from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔝Bosh sahifa")]
    ],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="AI bilan suhbat")],
            [KeyboardButton(text="PDF qilish")]
        ],
        resize_keyboard=True
    )