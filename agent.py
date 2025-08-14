from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio

load_dotenv(override=True)


BillingAgent = Agent(
    name="Billing Agent",
    handoff_description="Specialist agent for billing questions",
    instructions="You are provide help with billing issues, be extra diligent with your work and explain your action clearly."
)

ShippingAgent = Agent(
    name="Shipping Agent",
    handoff_description="Specialist agent for shipping questions",
    instructions="You are provide help with shipping issues, always summarize your work at the end of conversation."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's question",
    handoffs = [BillingAgent, ShippingAgent]
)

async def main():
    user_input = input("Hi, welcome to the support chatbot. Please enter your question: ")
    result = await Runner.run(triage_agent, user_input)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())