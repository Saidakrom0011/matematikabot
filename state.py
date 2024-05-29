from aiogram.dispatcher.filters.state import StatesGroup, State


class LevelState(StatesGroup):
    question = State()
    answer = State()


class LevelState1(StatesGroup):
    question = State()
    answer = State()