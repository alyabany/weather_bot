from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def weather_kb() :
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="بحث حسب الإحداثيات", callback_data="current_weather")],
        [InlineKeyboardButton(text="بحث حسب اسم المدينة", callback_data="city_weather")],
        [InlineKeyboardButton(text="العودة إلى القائمة الرئيسية", callback_data="main_menu")],
    ])
    return kb