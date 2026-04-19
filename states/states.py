from aiogram.fsm.state import StatesGroup, State

class BotStates(StatesGroup):
    aiMode = State()
    pdfMode = State()