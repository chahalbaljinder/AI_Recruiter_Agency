from swarm import Swarm, Agent
from dotenv import load_dotenv


load_dotenv()

client = Swarm()


def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="agent B",
    instructions="You are a helpful agent",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="agent B",
    instructions="Only speak in Haikus. and writes a haiku for the user.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

print(response.messages[-1]["content"])
