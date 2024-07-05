from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generation import gpt4

from app.filters.chat_types import ChatTypeFilter


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))
class Generate(StatesGroup):
    text = State()


@user_private_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Hello, I'm AI bot")
    await state.clear()

@user_private_router.message(Generate.text)
async def generate_error(message: Message):
    await message.answer("Please, write text")    


@user_private_router.message(F.text)
async def text(message: Message, state: FSMContext):
    await state.set_state(Generate.text)
    response = await gpt4(message.text)
    await message.answer(response.choices[0].message.content)
    await state.clear()



