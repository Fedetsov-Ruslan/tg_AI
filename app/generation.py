import os
import asyncio

from dotenv import load_dotenv
from openai import AsyncOpenAI


load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("AI_TOKEN"))

async def gpt4(questions):
    response = await client.chat.completions.create(
        messages=[
            {"role": "user",
             "content": str(questions)}],
        model="gpt-4o"
    )
    return response