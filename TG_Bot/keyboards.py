from pyrogram.types import ReplyKeyboardMarkup
import buttons

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.photo_button],
    ],
    resize_keyboard=True,
)
