import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers.user_private import user_private_router
from app.handlers.group_chat import user_group_router


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv("TG_TOKEN"))
    dp = Dispatcher()
    dp.include_router(user_private_router)
    dp.include_router(user_group_router)
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
      asyncio.run(main())
    except KeyboardInterrupt:
        print("bot dont active")