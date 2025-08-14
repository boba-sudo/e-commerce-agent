import os
from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio

load_dotenv(override=True)

async def main():
    agent = Agent(
        name="Support Agent",
        instructions="You are a support agent that can help with customer issues, always begin your respond with 5 emojis"
    )

    result = await Runner.run(agent, "I have a problem with my account")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())