from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton , ReplyKeyboardMarkup, KeyboardButton
def weather_kb() :
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="الطقس حسب الإحداثيات", callback_data="current_weather")],
        [InlineKeyboardButton(text="الطقس حسب اسم المدينة", callback_data="city_weather")],
        [InlineKeyboardButton(text="الطقس حسب موقعي", callback_data="my_location_weather")],
        [InlineKeyboardButton(text="العودة إلى القائمة الرئيسية", callback_data="main_menu")],
    ])
    return kb

def location_kb() :
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="إرسال موقعي الحالي", request_location=True)
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return kb