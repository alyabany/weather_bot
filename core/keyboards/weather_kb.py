from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def weather_kb() :
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="احصل على الطقس الحالي", callback_data="current_weather")],
        
        [InlineKeyboardButton(text="العودة إلى القائمة الرئيسية", callback_data="main_menu")],
    ])
    return kb