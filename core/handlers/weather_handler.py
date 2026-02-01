from aiogram import Router , F
from aiogram.types import Message , CallbackQuery
from aiogram.fsm.context import FSMContext

from core.keyboards.weather_kb import location_kb, weather_kb
from core.states import WeatherStates
from core.services.weather_api import *
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


@router.callback_query(F.data == 'city_weather')
async def city_weather_callback(cb: CallbackQuery , state: FSMContext):
    await cb.message.answer("الرجاء إرسال اسم المدينة:")
    await state.set_state(WeatherStates.waiting_city)
    @router.message(WeatherStates.waiting_city)
    async def waiting_city_handler(msg: Message , state: FSMContext):
        city_name = msg.text
        lat , lon = get_weather_city(city_name)
        if not lat or not lon:
            await msg.answer("عذراً، لم أتمكن من العثور على المدينة. يرجى التحقق من الاسم والمحاولة مرة أخرى.")
            return
        weather_data = get_weather_lat_lon(lat, lon)
        if not weather_data:
            await msg.answer("عذراً، لم أتمكن من جلب بيانات الطقس. يرجى المحاولة مرة أخرى.")
            return
        await msg.answer(
            f"الطقس الحالي في {city_name}:\n{weather_data}", reply_markup=weather_kb())
        await state.clear()


@router.callback_query(F.data == 'my_location_weather')
async def my_location_weather_callback(cb: CallbackQuery , state: FSMContext):
    await cb.message.answer("الرجاء الضغط على زر إرسال موقعي الحالي:", reply_markup=location_kb())
    await state.set_state(WeatherStates.waiting_location)
@router.message(WeatherStates.waiting_location, F.location)
async def location_handler(msg: Message , state: FSMContext):
    latitude = msg.location.latitude
    longitude = msg.location.longitude
    weather_data = get_weather_lat_lon(latitude, longitude)
    if not weather_data:
        await msg.answer("عذراً، لم أتمكن من جلب بيانات الطقس. يرجى المحاولة مرة أخرى.")
        return
    await msg.answer(
        f"الطقس الحالي في موقعك:\n{weather_data}", reply_markup=weather_kb())
    await state.clear()

