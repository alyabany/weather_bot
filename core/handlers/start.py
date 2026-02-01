# core/handlers.py
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from core.keyboards.main_menu import main_menu
from core.states import MainMenu
from core.handlers.weather_handler import router as weather_router

router = Router()

def register_handlers(dp):
    dp.include_router(router)  
    dp.include_router(weather_router)


@router.message(F.text == "/start")
async def cmd_start(msg: Message, state: FSMContext):
    await msg.answer(
        "اهلاً وسهلاً \n اختر من القائمة التالية: ",
        reply_markup=main_menu()
    )
    await state.set_state(MainMenu.menu)
    
@router.callback_query(F.data == 'main_menu')
async def main_menu_callback(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text(
        "اهلاً وسهلاً \n اختر من القائمة التالية: ",
        reply_markup=main_menu()
    )
    await state.set_state(MainMenu.menu)
@router.message(F.text == "/help")
async def cmd_help(msg: Message):
    await msg.answer("مرحباً ! 👋\n\nالمساعدة: يمكنك استخدام الأوامر التالية:\n/start - لبدء التشغيل\n/help - للحصول على المساعدة")
