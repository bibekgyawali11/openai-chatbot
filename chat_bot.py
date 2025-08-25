import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Get API key from environment
API_KEY = os.getenv("API_KEY")

client = AsyncOpenAI(api_key=API_KEY)

async def chat_with_gpt(prompt):
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

async def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = await chat_with_gpt(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    asyncio.run(main())