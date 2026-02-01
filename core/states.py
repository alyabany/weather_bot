from aiogram.fsm.state import StatesGroup, State
class MainMenu(StatesGroup):
    menu = State()

class WeatherStates(StatesGroup):
    menu = State()

    waiting_lat = State()
    waiting_lon = State()

    waiting_city = State()
    waiting_location = State()