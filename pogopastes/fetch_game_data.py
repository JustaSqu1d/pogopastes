import json

import requests

POKEMON_GAMEMASTERS_URL = "https://raw.githubusercontent.com/JustaSqu1d/celesteela-bot/refs/heads/master/celesteela-bot/gamedata/pokemon.json"
MOVES_GAMEMASTERS_URL = "https://raw.githubusercontent.com/JustaSqu1d/celesteela-bot/refs/heads/master/celesteela-bot/gamedata/moves.json"

if __name__ == "__main__":
    # read them to files
    pokemon_gamemasters = requests.get(POKEMON_GAMEMASTERS_URL).json()
    moves_gamemasters = requests.get(MOVES_GAMEMASTERS_URL).json()

    with open("pogopastes/gamedata/pokemon.json", "w") as f:
        json.dump(pokemon_gamemasters, f, indent=4)

    with open("pogopastes/gamedata/moves.json", "w") as f:
        json.dump(moves_gamemasters, f, indent=4)
