import json
import os


def convert_pokemon_hex_to_dictionary(hex_string: str) -> dict:
    """
    Convert a hex string to a dictionary.

    First 12 bits are the Pokemon ID.
    Next 5 bits are the form ID.
    Next 1 bit is the best buddy flag.
    Next 2 bit is the shadow/purified flag.
    Next 10 bits are the fast move ID.
    Next 10 bits are the first charged move ID.
    Next 10 bits are the second charged move ID.
    Next 14 bits are the combat power.

    Parameters
    ----------
    hex_string : str
        The hex string.

    Returns
    -------
    dict
    """
    binary_string = bin(int(hex_string, 16))[2:].zfill(64)

    # extract the values
    pokemon_id = int(binary_string[:12], 2)
    form_id = int(binary_string[12:17], 2)
    best_buddy = int(binary_string[17], 2)
    shadow_purified = int(binary_string[18:20], 2)
    fast_move_id = int(binary_string[20:30], 2)
    first_charged_move_id = int(binary_string[30:40], 2)
    second_charged_move_id = int(binary_string[40:50], 2)
    combat_power = int(binary_string[50:], 2)

    pokemon_name = get_pokemon_by_id(pokemon_id).get("species", "Unknown")
    form_name = None if form_id == 0 else get_pokemon_by_id(pokemon_id, form_id).get("name", "Unknown")

    best_buddy = bool(best_buddy)
    if shadow_purified == 0:
        shadow_purified = "Normal"
    elif shadow_purified == 1:
        shadow_purified = "Shadow"
    else:
        shadow_purified = "Purified"

    fast_move_name = get_move_by_id(fast_move_id).get("uniqueId", "None")
    first_charged_move_name = get_move_by_id(first_charged_move_id).get("uniqueId", "None")
    second_charged_move_name = get_move_by_id(second_charged_move_id).get("uniqueId", "None")

    return {
        "pokemon_name": pokemon_name,
        "form_name": form_name,
        "combat_power": combat_power,
        "best_buddy": best_buddy,
        "shadow_purified": shadow_purified,
        "fast_move_name": fast_move_name,
        "first_charged_move_name": first_charged_move_name,
        "second_charged_move_name": second_charged_move_name,
    }


def convert_pokemon_name_to_id(pokemon_name: str) -> int:
    """
    Convert the Pokemon name to an ID.

    Parameters
    ----------
    pokemon_name : str
        The name of the Pokemon.

    Returns
    -------
    int
    """
    pokemon_data = read_pokemon_data()

    for pokemon in pokemon_data:
        if pokemon_data[pokemon]["species"] == pokemon_name:
            return pokemon_data[pokemon]["pokedex_number"]


def convert_move_name_to_id(move_name: str) -> int:
    """
    Convert the move name to an ID.

    Parameters
    ----------
    move_name : str
        The name of the move.

    Returns
    -------
    int
    """
    moves_data = read_moves_data()

    for move in moves_data:
        if moves_data[move]["uniqueId"] == move_name or moves_data[move]["uniqueId"] == move_name + "_FAST":
            return moves_data[move]["uuid"]


def convert_form_name_to_id(pokemon_id: int, form_name: str) -> int:
    """
    Convert the form name to an ID.

    Parameters
    ----------
    pokemon_id : int
        The ID of the Pokemon.
    form_name : str
        The name of the form.

    Returns
    -------
    int
    """
    pokemon_data = read_pokemon_data()

    for pokemon in pokemon_data:
        if pokemon_data[pokemon]["pokedex_number"] == pokemon_id and pokemon_data[pokemon]["name"] == form_name:
            return pokemon_data[pokemon]["form_number"]


def convert_shadow_purified_to_id(shadow_purified: str) -> int:
    """
    Convert the shadow/purified to an ID.

    Parameters
    ----------
    shadow_purified : str
        The shadow/purified flag.

    Returns
    -------
    int
    """
    if shadow_purified.lower() == "normal":
        return 0
    elif shadow_purified.lower() == "shadow":
        return 1
    elif shadow_purified.lower() == "purified":
        return 2


def convert_pokemon_to_hex(species_name, cp, shadow, fast_move, charge_move1, charge_move2):
    """
    Convert the Pokemon data to a hex string.

    Parameters
    ----------
    species_name : str
        The name of the species.
    cp : int
        The combat power.
    shadow : bool
        The shadow flag.
    fast_move : str
        The fast move.
    charge_move1 : str
        The first charged move.
    charge_move2 : str
        The second charged move.

    Returns
    -------
    str
    """
    pokemon_name, species_name = unformat_pokemon_name(species_name)

    pokemon_id = convert_pokemon_name_to_id(pokemon_name)
    form_id = convert_form_name_to_id(pokemon_id, species_name) if species_name else 0
    shadow_purified = convert_shadow_purified_to_id(shadow)

    fast_move_name = unformat_move_name(fast_move)
    first_charged_move_name = unformat_move_name(charge_move1)
    second_charged_move_name = unformat_move_name(charge_move2)

    fast_move_id = convert_move_name_to_id(fast_move_name)
    first_charged_move_id = convert_move_name_to_id(first_charged_move_name)
    second_charged_move_id = convert_move_name_to_id(second_charged_move_name)

    return convert_raw_pokemon_to_hex(pokemon_id, form_id, False, shadow_purified, fast_move_id, first_charged_move_id,
                                      second_charged_move_id, cp)


def convert_raw_pokemon_to_hex(pokemon_id, form_id, best_buddy, shadow_purified, fast_move_id, first_charged_move_id,
                               second_charged_move_id, combat_power) -> str:
    """
    Convert the Pokemon data to a hex string.

    Parameters
    ----------
    pokemon_id : int
        The ID of the Pokemon.
    form_id : int
        The ID of the form.
    best_buddy : bool
        The best buddy flag.
    shadow_purified : int
        The shadow/purified flag.
    fast_move_id : int
        The ID of the fast move.
    first_charged_move_id : int
        The ID of the first charged move.
    second_charged_move_id : int
        The ID of the second charged move.
    combat_power : int
        The combat power of the Pokemon.

    Returns
    -------
    str
    """
    binary_string = ''.join([
        format(pokemon_id, '012b'),
        format(form_id, '05b'),
        str(int(best_buddy)),
        format(shadow_purified, '02b'),
        format(fast_move_id, '010b'),
        format(first_charged_move_id, '010b'),
        format(second_charged_move_id, '010b'),
        format(combat_power, '014b')
    ])

    return hex(int(binary_string, 2))


def read_pokemon_data() -> dict:
    """
    Read the Pokemon data from the file.

    Returns
    -------
    dict
    """
    path = os.path.dirname(__file__)
    with open(path + "/gamedata/pokemon.json", "r") as f:
        return json.load(f)


def read_moves_data() -> dict:
    """
    Read the moves data from the file.

    Returns
    -------
    dict
    """
    path = os.path.dirname(__file__)
    with open(path + "/gamedata/moves.json", "r") as f:
        return json.load(f)


def get_pokemon_by_id(pokemon_id: int, form_id: int = -1) -> dict:
    """
    Get the pokemon by ID.

    Parameters
    ----------
    pokemon_id : int
        The ID of the pokemon.

    Returns
    -------
    dict

    If the Pokemon is not found, it will return an empty dictionary.
    """

    pokemon_data = read_pokemon_data()

    for pokemon in pokemon_data:
        pokedex_number = pokemon_data[pokemon]["pokedex_number"]
        form_number = pokemon_data[pokemon]["form_number"]
        if pokedex_number == pokemon_id:
            if form_id == -1 or form_number == form_id:
                return pokemon_data[pokemon]

    return {}


def get_move_by_id(move_id: int) -> dict | None:
    """
    Get the move by ID.

    Parameters
    ----------
    move_id : int
        The ID of the move.

    Returns
    -------
    dict | None

    If the move is not found, it will return an empty dictionary.
    """
    moves_data = read_moves_data()
    for move in moves_data:
        if moves_data[move]["uuid"] == move_id:
            return moves_data[move]

    return {}


def format_pokemon_name(pokemon_name: str, form_name: str) -> str:
    """
    Format the Pokemon name.

    Parameters
    ----------
    pokemon_name : str
        The name of the Pokemon.
    form_name : str
        The name of the form.

    Returns
    -------
    str
    """
    new_pokemon_name = pokemon_name.replace("_", " ").title()
    if form_name and pokemon_name != form_name:
        new_form_name = form_name.replace("ALOLA", "alolan").replace(pokemon_name, "").replace("_", " ").title().strip()
        return f"{new_pokemon_name} ({new_form_name})"
    else:
        return new_pokemon_name


def unformat_pokemon_name(pokemon_name: str) -> tuple[str, str]:
    """
    Unformat the Pokemon name.

    Parameters
    ----------
    pokemon_name : str
        The name of the Pokemon.

    Returns
    -------
    tuple[str, str]
    """
    new_pokemon_name = pokemon_name.replace(" (", " ").replace("Alolan", "ALOLA").replace(" ", "_").replace(")", "")
    if "(" in pokemon_name:
        form_name = new_pokemon_name

        if "primal" in form_name.lower():
            form_name = "PRIMAL_" + form_name.split("_")[0]

        new_pokemon_name = new_pokemon_name.split("_")[0]
        return new_pokemon_name.strip().upper(), form_name.strip().upper()
    else:
        return pokemon_name.upper(), ""


def format_move_name(move_name: str | None) -> str | None:
    """
    Format the move name.

    Parameters
    ----------
    move_name : str
        The name of the move.

    Returns
    -------
    str
    """
    if not move_name:
        return move_name
    elif move_name == "FUTURESIGHT":
        return "Future Sight"
    elif move_name == "SUPER_POWER":
        return "Superpower"
    elif move_name == "AEROBLAST_PLUS_PLUS":
        return "Aeroblast++"
    elif move_name == "SACRED_FIRE_PLUS_PLUS":
        return "Sacred Fire++"
    elif move_name == "AEROBLAST_PLUS":
        return "Aeroblast+"
    elif move_name == "SACRED_FIRE_PLUS":
        return "Sacred Fire+"
    elif move_name == "MUD_SLAP_FAST":
        return "Mud-Slap"
    else:
        return move_name.replace("_FAST", "").replace("_", " ").title()


def unformat_move_name(move_name: str) -> str:
    """
    Unformat the move name.

    Parameters
    ----------
    move_name : str
        The name of the move.

    Returns
    -------
    str
    """
    if move_name == "Future Sight":
        return "FUTURESIGHT"
    elif move_name == "Superpower":
        return "SUPER_POWER"
    elif move_name == "Aeroblast++":
        return "AEROBLAST_PLUS_PLUS"
    elif move_name == "Sacred Fire++":
        return "SACRED_FIRE_PLUS_PLUS"
    elif move_name == "Aeroblast+":
        return "AEROBLAST_PLUS"
    elif move_name == "Sacred Fire+":
        return "SACRED_FIRE_PLUS"

    return move_name.replace(" ", "_").replace("-", "_").upper()


def pokepaste_stringify(poke_team_hex) -> str:
    """
    Convert the hex string to a Pokepaste string.

    Parameters
    ----------
    poke_team_hex : str
        The hex string of the Pokemon team.

    Returns
    -------
    str
    """
    poke_team_dict = []

    for poke_hex in poke_team_hex.split("-"):
        poke_team_dict.append(convert_pokemon_hex_to_dictionary(poke_hex))

    final_pokepaste_string = ""

    for team_member in poke_team_dict:
        regular_name = format_pokemon_name(team_member["pokemon_name"], team_member["form_name"])
        pokepaste_compliant_name = (regular_name
                                    .replace(" ", "-")
                                    .replace("(", "")
                                    .replace(")", "")
                                    .replace("Alolan", "Alola")
                                    .replace("Galarian", "Galar")
                                    .replace("Hisuian", "Hisui"))

        if team_member["shadow_purified"] == "Shadow":
            pokepaste_compliant_name += "-Shadow"
        elif team_member["shadow_purified"] == "Purified":
            pokepaste_compliant_name += "-Purified"

        if team_member["best_buddy"]:
            pokepaste_compliant_name += " @ Best Buddy Ribbon"

        combat_power = team_member["combat_power"]

        fast_move = format_move_name(team_member["fast_move_name"])
        first_charged_move = format_move_name(team_member["first_charged_move_name"])
        second_charged_move = format_move_name(team_member["second_charged_move_name"])

        final_pokepaste_string += f"{pokepaste_compliant_name}\nAbility: {combat_power}\n- {fast_move}\n- {first_charged_move}\n- {second_charged_move}\n- Protect"

    return final_pokepaste_string


if __name__ == "__main__":
    hex_string = convert_raw_pokemon_to_hex(493, 1, False, 0, 236, 31, 0, 1500)

    poke_dict = convert_pokemon_hex_to_dictionary(hex_string)

    poke_dict["pokemon_name"] = format_pokemon_name(poke_dict["pokemon_name"], poke_dict["form_name"])
    poke_dict["fast_move_name"] = format_move_name(poke_dict["fast_move_name"])
    poke_dict["first_charged_move_name"] = format_move_name(poke_dict["first_charged_move_name"])
    poke_dict["second_charged_move_name"] = format_move_name(poke_dict["second_charged_move_name"])

    print(poke_dict)
