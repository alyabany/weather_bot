from aiogram import Router , F
from aiogram.types import Message , CallbackQuery
from aiogram.fsm.context import FSMContext

from core.keyboards.weather_kb import weather_kb
from core.states import WeatherStates
from core.services.weather_api import get_weather_lat_lon
from core.states import WeatherStates

router = Router()

@router.callback_query(F.data == 'weather')
async def weather_callback(cb: CallbackQuery , state: FSMContext):
    await cb.message.answer(
        "اختر من الخيارات التالية للحصول على معلومات الطقس:", reply_markup=weather_kb())
    await state.set_state(WeatherStates.menu)


@router.callback_query(F.data == 'current_weather')
async def current_weather_callback(cb: CallbackQuery , state: FSMContext):
    await cb.message.answer("الرجاء إرسال دائرة العرض (Latitude):")
    await state.set_state(WeatherStates.waiting_lat)

    
    
@router.message(WeatherStates.waiting_lat)
async def waiting_lat_handler(msg: Message , state: FSMContext):
    await state.update_data(lat=msg.text) 
    await state.set_state(WeatherStates.waiting_lon)
    await msg.answer("الرجاء إرسال خط الطول (Longitude):")
@router.message(WeatherStates.waiting_lon)
async def waiting_lon_handler(msg: Message , state: FSMContext):
    await state.update_data(lon=msg.text)
    data = await state.get_data()
    lat = data['lat']
    lon = data['lon']
    weather_data = get_weather_lat_lon(lat, lon)
    if not weather_data:
        await msg.answer("عذراً، لم أتمكن من جلب بيانات الطقس. يرجى التحقق من الإحداثيات والمحاولة مرة أخرى.")
        return
    await msg.answer(
        f"الطقس الحالي:\n{weather_data}", reply_markup=weather_kb())
    await state.clear()