from openai import OpenAI
from swarm import Swarm, Agent

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required, but unused
)


client = Swarm(client=client)  # client is an instance of the Swarm class


def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="agent A",
    model="llama3.2",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="agent B",
    model="llama3.2",
    instructions="Only speak in Haikus. and writes a haiku for the user.",
)


def run_demo_loop(agent_a, context_variables=None, stream=False, debug=False) -> None:
    # client = Swarm(client=ollama_client)
    print("Starting Ollama Swarm CLI 🐝")

    messages = []
    agent = agent_a

    while True:
        user_input = input("\033[90mUser\033[0m: ")
        messages.append({"role": "user", "content": user_input})

        response = client.run(
            agent=agent,
            messages=messages,
            context_variables=context_variables or {},
            stream=stream,
            debug=debug,
        )

        res = response.messages
        print(res[-1]["content"])

        messages.extend(response.messages)
        agent = response.agent


if __name__ == "__main__":
    run_demo_loop(agent_a)
