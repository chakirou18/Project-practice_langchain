"""WHAT YOU FILL IN
  TODO 1: write your own SYSTEM_PROMPT string that scopes the agent to a
    single domain of your choosing and tells it to refuse or redirect
    anything outside that domain (no persona/voice requirement here,
    just the scope + refusal instruction).
  TODO 2: invoke the agent with two test prompts, one inside your domain
    and one clearly outside it, and print both responses so you can see
    whether the refusal actually held."""

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from deepagents import create_deep_agent
from models import model

# TODO 1 filled in
SYSTEM_PROMPT = (
    "You only answer questions about houseplants: care, watering, light, "
    "pests, soil, and propagation. If asked about anything outside "
    "houseplants, say you can't help with that and redirect the "
    "conversation back to houseplants."
)


agent = create_deep_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    name="Homework_Agent",
)


# TODO 2 filled in
def run_test_prompts():
    prompts = [
        "Why are the leaves on my pothos turning yellow?",#start i=1
        "What's a good way to organize my closet?",#i=2
    ]
    for i, prompt in enumerate(prompts, start=1):
        result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
        print(f"=== Test prompt {i}: {prompt} ===")
        print(result["messages"][-1].content)
        print()


run_test_prompts()
