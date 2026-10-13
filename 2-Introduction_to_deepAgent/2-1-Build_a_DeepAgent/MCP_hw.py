""" TODO 1: build and return the filtered list of MCP tools to use from a server and filter of your own choosing.
TODO 2: write a question suited to your chosen server's own domain, not Lab 1's "what is MCP..." question."""

import asyncio
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from deepagents import create_deep_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from models import model


# TODO 1 filled in: a different public MCP server than the lab's,
# DeepWiki, which answers questions about any public GitHub repo.
"""une fonction asyncrone est une fonction qui peut etre suspendue et reprise plus tard.
Normalement, dans une exécution synchrone, Python attend qu'une opération se termine avant de passer à l'instruction suivante.
Avec la programmation asynchrone, Python peut suspendre la fonction en attente et permettre à d'autres tâches asynchrones de progresser."""
async def build_tools(): # async: fonction asynchrones, await: attend la fin de l'exécution d'une fonction asynchrone
    client = MultiServerMCPClient({
        "deepwiki": {
            "transport": "http",
            "url": "https://mcp.deepwiki.com/mcp",
        }
    })
    tools = await client.get_tools()

    ALLOWED = {"ask_question"}# ALLOWED: ensemble des outils autorisés, ici "ask_question"
    return [t for t in tools if t.name in ALLOWED]


# TODO 2 filled in
QUESTION = (
    "Use the DeepWiki tool to ask the langchain-ai/deepagents GitHub repo: "
    "what filesystem backends does deepagents support?"
)


async def main():
    tools = await build_tools()
    agent = create_deep_agent(model=model, tools=tools)
    result = await agent.ainvoke({"messages": [{"role": "user", "content": QUESTION}]})
    print(result["messages"][-1].content)


asyncio.run(main())
