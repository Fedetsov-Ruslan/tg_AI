from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generation import gpt4


router = Router()
class Generate(StatesGroup):
    text = State()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Hello, I'm AI bot")
    await state.clear()

@router.message(Generate.text)
async def generate_error(message: Message):
    await message.answer("Please, write text")    


@router.message(F.text)
async def text(message: Message, state: FSMContext):
    await state.set_state(Generate.text)
    response = await gpt4( message.text)
    await message.answer(response.choise[0].message.content)



