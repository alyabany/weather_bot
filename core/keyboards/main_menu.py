from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu() :
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="الطقس", callback_data="weather")],
    ])
    return kb