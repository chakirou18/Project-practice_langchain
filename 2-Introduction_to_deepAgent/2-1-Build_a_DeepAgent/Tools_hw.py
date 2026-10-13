
"""
WHAT YOU FILL IN
  TODO 1: write your own custom tool with the @tool decorator. Pick any
    topic, store a small lookup (a dict is fine, no API needed) of facts
    about it, and return one back based on the argument the model passes.
  TODO 2: write a system prompt that gives the agent a persona of your
    choosing and tells it to use your tool before answering."""


#Un avertissement (warning) sert à signaler un problème potentiel sans nécessairement arrêter l'exécution du programme.
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)#DeprecationWarning(a ignorer): Catégorie des avertissements liés à des fonctionnalités obsolètes

from langchain_core.tools import tool

from deepagents import create_deep_agent
from models import model

RETRO_GAME_FACTS = {
    "PAC-MAN": "Pac-Man's ghosts each follow a distinct movement pattern: Blinky chases you directly, Pinky ambushes ahead of you, Inky is erratic, and Clyde mostly wanders off on his own.",
    "TETRIS": "Tetris was created in 1984 by Alexey Pajitnov on an Elektronika 60, a Soviet computer with no graphics mode, so the first version rendered pieces with text characters.",
    "DONKEY KONG": "Donkey Kong (1981) was Nintendo's first game to feature a character with a real story-driven goal, and it introduced Mario, originally named 'Jumpman.'",
    "STREET FIGHTER II": "Street Fighter II (1991) popularized the six-button fighting game layout and the concept of a 'combo,' both of which most fighting games still use today.",
}


# TODO 1 filled in
@tool# le décorateur
def lookup_retro_game_fact(game: str) -> str:#->str: indique la fonction retourne une chaine de caratères, game: Paramètre qui reçoit le nom du jeu
    """Return one trivia fact about a classic arcade or console game. Call
    with a lowercase game name, e.g. 'pac-man' or 'tetris'."""# docstring: documentation de la fonction
    key = game.strip().lower() # strip(): supprime les espaces au début et a la fin de la chaine, lower(): convertit la chaine en miniscule
    if key in RETRO_GAME_FACTS:
        return RETRO_GAME_FACTS[key]
    return f"No trivia on file for '{game}'. Known games: {', '.join(RETRO_GAME_FACTS)}."


# TODO 2 filled in

SYSTEM_PROMPT = """You are the Arcade Ref, a play-by-play sports commentator
who somehow ended up calling retro video game trivia instead of an actual
game. Treat every question like it's the final round of a championship:
build hype, call out the "play" (the fact you found) like a highlight reel
moment, and never just flatly state trivia. Always call
lookup_retro_game_fact before answering; if the game isn't in your
lookup, announce that "the judges have no record of this contender" and
list the games you do know."""


agent = create_deep_agent(
    model=model,
    name="Homework_Agent",
    tools=[lookup_retro_game_fact],
    system_prompt=SYSTEM_PROMPT,
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Give me the scoop on TETRIS."}]}
)

print(result["messages"][-1].content)
