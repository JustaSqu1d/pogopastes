import json

import streamlit as st

from parser import format_pokemon_name, format_move_name, convert_pokemon_to_hex, convert_pokemon_name_to_id, convert_move_name_to_id, convert_form_name_to_id, convert_shadow_purified_to_id


def get_pokemon_image(pokemon_species: str) -> str:
    new_pokemon_string = (pokemon_species
                          .lower()
                          .replace(" ", "-")
                          .replace("(", "")
                          .replace(")", "")
                          .replace("alolan","alola")
                          .replace("hisuian", "hisui")
                          .replace("galarian", "galar")
                          .replace("--", "-")
                          .replace("mega-x", "megax")
                          .replace("mega-y","megay")
                          )

    match new_pokemon_string:
        case "pikachu-doctor":
            new_pokemon_string = "pikachu"
        case "pikachu-flying-01":
            new_pokemon_string = "pikachu"
        case "pikachu-flying-okinawa":
            new_pokemon_string = "pikachu"
        case "pikachu-gofest-2024-mtiara":
            new_pokemon_string = "pikachu"
        case "pikachu-horizons":
            new_pokemon_string = "pikachu"
        case "pikachu-pop-star":
            new_pokemon_string = "pikachu"
        case "pikachu-rock-star":
            new_pokemon_string = "pikachu"
        case "nidoran-male":
            new_pokemon_string = "nidoranm"
        case "nidoran-female":
            new_pokemon_string = "nidoranf"
        case "mr-mime":
            new_pokemon_string = "mrmime"
        case "mr-mime-galar":
            new_pokemon_string = "mrmime-galar"
        case "mewtwo-a":
            new_pokemon_string = "mewtwo"
        case "ho-oh":
            new_pokemon_string = "hooh"
        case "cherrim-sunny":
            new_pokemon_string = "cherrim-sunshine"
        case "mime-jr":
            new_pokemon_string = "mimejr"
        case "porygon-z":
            new_pokemon_string = "porygonz"
        case "darmanitan-galar-standard":
            new_pokemon_string = "darmanitan-galar"
        case "darmanitan-galar-zen":
            new_pokemon_string = "darmanitan-galarzen"
        case "meowstic-female":
            new_pokemon_string = "meowstic-f"
        case "pumpkaboo-average":
            new_pokemon_string = "pumpkaboo"
        case "gourgeist-average":
            new_pokemon_string = "gourgeist"
        case "zygarde-complete-ten-percent":
            new_pokemon_string = "zygarde-10"
        case "type-null":
            new_pokemon_string = "typenull"
        case "jangmo-o-jangmo-o":
            new_pokemon_string = "jangmoo"
        case "hakamo-o-hakamo-o":
            new_pokemon_string = "hakamoo"
        case "kommo-o-kommo-o":
            new_pokemon_string = "kommoo"
        case "tapu-koko":
            new_pokemon_string = "tapukoko"
        case "tapu-lele":
            new_pokemon_string = "tapulele"
        case "tapu-bulu":
            new_pokemon_string = "tapubulu"
        case "tapu-fini":
            new_pokemon_string = "tapufini"
        case "necrozma-dawn-wings":
            new_pokemon_string = "necrozma-dawnwings"
        case "necrozma-dusk-mane":
            new_pokemon_string = "necrozma-duskmane"
        case "mr-rime":
            new_pokemon_string = "mrrime"
        case "indeedee-male":
            new_pokemon_string = "indeedee"
        case "indeedee-female":
            new_pokemon_string = "indeedee-f"
        case "zacian-crowned-sword":
            new_pokemon_string = "zacian-crowned"
        case "zacian-hero":
            new_pokemon_string = "zacian"
        case "zamazenta-crowned-shield":
            new_pokemon_string = "zamazenta-crowned"
        case "zamazenta-hero":
            new_pokemon_string = "zamazenta"
        case "urshifu-single-strike":
            new_pokemon_string = "urshifu"
        case "urshifu-rapid-strike":
            new_pokemon_string = "urshifu-rapidstrike"
        case "calyrex-ice-rider":
            new_pokemon_string = "calyrex-ice"
        case "calyrex-shadow-rider":
            new_pokemon_string = "calyrex-shadow"
        case "oinkologne-male":
            new_pokemon_string = "oinkologne"
        case "oinkologne-female":
            new_pokemon_string = "oinkologne-f"
        case "greattusk-great-tusk":
            new_pokemon_string = "greattusk"
        case "screamtail-scream-tail":
            new_pokemon_string = "screamtail"
        case "brutebonnet-brute-bonnet":
            new_pokemon_string = "brutebonnet"
        case "fluttermane-flutter-mane":
            new_pokemon_string = "fluttermane"
        case "slitherwing-slither-wing":
            new_pokemon_string = "slitherwing"
        case "sandyshocks-sandy-shocks":
            new_pokemon_string = "sandyshocks"
        case "irontreads-iron-treads":
            new_pokemon_string = "irontreads"
        case "ironbundle-iron-bundle":
            new_pokemon_string = "ironbundle"
        case "ironhands-iron-hands":
            new_pokemon_string = "ironhands"
        case "ironjugulis-iron-jugulis":
            new_pokemon_string = "ironjugulis"
        case "ironmoth-iron-moth":
            new_pokemon_string = "ironmoth"
        case "ironthorns-iron-thorns":
            new_pokemon_string = "ironthorns"
        case "wochien-wo-chien":
            new_pokemon_string = "wochien"
        case "chienpao-chien-pao":
            new_pokemon_string = "chienpao"
        case "tinglu-ting-lu":
            new_pokemon_string = "tinglu"
        case "chiyu-chi-yu":
            new_pokemon_string = "chiyu"
        case "roaringmoon-roaring-moon":
            new_pokemon_string = "roaringmoon"
        case "ironvaliant-iron-valiant":
            new_pokemon_string = "ironvaliant"

    return f"https://play.pokemonshowdown.com/sprites/gen5/{new_pokemon_string}.png"


pokemon_species_list = []

with open("pogopastes/gamedata/pokemon.json", "r") as f:
    pokemon_gamemasters = json.load(f)
    for pokemon in pokemon_gamemasters:
        pokemon_species_list.append(
            format_pokemon_name(pokemon_gamemasters[pokemon]["species"], pokemon_gamemasters[pokemon]["name"]))

moves_list = []

with open("pogopastes/gamedata/moves.json", "r") as f:
    moves_gamemasters = json.load(f)
    for move in moves_gamemasters:
        moves_list.append(format_move_name(moves_gamemasters[move]["uniqueId"]))

moves_list = sorted(moves_list)

st.title("Create a team")
st.write("---")

left, right = st.columns([1, 1])

with left:
    with st.container():
        sub_left, sub_right = st.columns(2)
        with sub_right:
            pokemon1_species = st.selectbox("Pokémon 1",
                                            options=pokemon_species_list,
                                            index=None,
                                            placeholder="Select a Pokémon",
                                            key="pokemon1_species")
            pokemon1_cp = st.number_input("CP", placeholder="CP", min_value=0, max_value=10000, step=1,
                                          key="pokemon1_cp")
            pokemon1_shadow = st.selectbox("Is it a shadow?", placeholder="Normal, Shadow, or Purified?",
                                           options=["Normal", "Shadow", "Purified"], index=0, key="pokemon1_shadow")
            pokemon1_fast_move = st.selectbox("Fast Move", options=moves_list, index=None, placeholder="Select a move",
                                              key="pokemon1_fast_move")
            pokemon1_charge_move1 = st.selectbox("Charge Move 1", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon1_charge_move1")
            pokemon1_charge_move2 = st.selectbox("Charge Move 2", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon1_charge_move2")
        with sub_left:
            if pokemon1_species:
                st.image(get_pokemon_image(pokemon1_species), width=170)

    st.write("---")

    with st.container():
        sub_left, sub_right = st.columns(2)
        with sub_right:
            pokemon2_species = st.selectbox("Pokémon 2",
                                            options=pokemon_species_list,
                                            index=None,
                                            placeholder="Select a Pokémon",
                                            key="pokemon2_species")
            pokemon2_cp = st.number_input("CP", placeholder="CP", min_value=0, max_value=10000, step=1,
                                          key="pokemon2_cp")
            pokemon2_shadow = st.selectbox("Is it a shadow?", placeholder="Normal, Shadow, or Purified?",
                                           options=["Normal", "Shadow", "Purified"], index=0, key="pokemon2_shadow")
            pokemon2_fast_move = st.selectbox("Fast Move", options=moves_list, index=None, placeholder="Select a move",
                                              key="pokemon2_fast_move")
            pokemon2_charge_move1 = st.selectbox("Charge Move 1", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon2_charge_move1")
            pokemon2_charge_move2 = st.selectbox("Charge Move 2", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon2_charge_move2")
        with sub_left:
            if pokemon2_species:
                st.image(get_pokemon_image(pokemon2_species), width=170)

    st.write("---")

    with st.container():
        sub_left, sub_right = st.columns(2)
        with sub_right:
            pokemon3_species = st.selectbox("Pokémon 3",
                                            options=pokemon_species_list,
                                            index=None,
                                            placeholder="Select a Pokémon",
                                            key="pokemon3_species")
            pokemon3_cp = st.number_input("CP", placeholder="CP", min_value=0, max_value=10000, step=1,
                                          key="pokemon3_cp")
            pokemon3_shadow = st.selectbox("Is it a shadow?", placeholder="Normal, Shadow, or Purified?",
                                           options=["Normal", "Shadow", "Purified"], index=0, key="pokemon3_shadow")
            pokemon3_fast_move = st.selectbox("Fast Move", options=moves_list, index=None, placeholder="Select a move",
                                              key="pokemon3_fast_move")
            pokemon3_charge_move1 = st.selectbox("Charge Move 1", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon3_charge_move1")
            pokemon3_charge_move2 = st.selectbox("Charge Move 2", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon3_charge_move2")
        with sub_left:
            if pokemon3_species:
                st.image(get_pokemon_image(pokemon3_species), width=170)

with right:
    with st.container():
        sub_left, sub_right = st.columns(2)
        with sub_right:
            pokemon4_species = st.selectbox("Pokémon 4",
                                            options=pokemon_species_list,
                                            index=None,
                                            placeholder="Select a Pokémon",
                                            key="pokemon4_species")
            pokemon4_cp = st.number_input("CP", placeholder="CP", min_value=0, max_value=10000, step=1,
                                          key="pokemon4_cp")
            pokemon4_shadow = st.selectbox("Is it a shadow?", placeholder="Normal, Shadow, or Purified?",
                                           options=["Normal", "Shadow", "Purified"], index=0, key="pokemon4_shadow")
            pokemon4_fast_move = st.selectbox("Fast Move", options=moves_list, index=None, placeholder="Select a move",
                                              key="pokemon4_fast_move")
            pokemon4_charge_move1 = st.selectbox("Charge Move 1", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon4_charge_move1")
            pokemon4_charge_move2 = st.selectbox("Charge Move 2", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon4_charge_move2")
        with sub_left:
            if pokemon4_species:
                st.image(get_pokemon_image(pokemon4_species), width=170)

    st.write("---")

    with st.container():
        sub_left, sub_right = st.columns(2)
        with sub_right:
            pokemon5_species = st.selectbox("Pokémon 5",
                                            options=pokemon_species_list,
                                            index=None,
                                            placeholder="Select a Pokémon",
                                            key="pokemon5_species")
            pokemon5_cp = st.number_input("CP", placeholder="CP", min_value=0, max_value=10000, step=1,
                                          key="pokemon5_cp")
            pokemon5_shadow = st.selectbox("Is it a shadow?", placeholder="Normal, Shadow, or Purified?",
                                           options=["Normal", "Shadow", "Purified"], index=0, key="pokemon5_shadow")
            pokemon5_fast_move = st.selectbox("Fast Move", options=moves_list, index=None, placeholder="Select a move",
                                              key="pokemon5_fast_move")
            pokemon5_charge_move1 = st.selectbox("Charge Move 1", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon5_charge_move1")
            pokemon5_charge_move2 = st.selectbox("Charge Move 2", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon5_charge_move2")
        with sub_left:
            if pokemon5_species:
                st.image(get_pokemon_image(pokemon5_species), width=170)

    st.write("---")

    with st.container():
        sub_left, sub_right = st.columns(2)

        with sub_right:
            pokemon6_species = st.selectbox("Pokémon 6",
                                            options=pokemon_species_list,
                                            index=None,
                                            placeholder="Select a Pokémon",
                                            key="pokemon6_species")
            pokemon6_cp = st.number_input("CP", placeholder="CP", min_value=0, max_value=10000, step=1,
                                          key="pokemon6_cp")
            pokemon6_shadow = st.selectbox("Is it a shadow?", placeholder="Normal, Shadow, or Purified?",
                                           options=["Normal", "Shadow", "Purified"], index=0, key="pokemon6_shadow")
            pokemon6_fast_move = st.selectbox("Fast Move", options=moves_list, index=None, placeholder="Select a move",
                                              key="pokemon6_fast_move")
            pokemon6_charge_move1 = st.selectbox("Charge Move 1", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon6_charge_move1")
            pokemon6_charge_move2 = st.selectbox("Charge Move 2", options=moves_list, index=None,
                                                 placeholder="Select a move", key="pokemon6_charge_move2")

        with sub_left:
            if pokemon6_species:
                st.image(get_pokemon_image(pokemon6_species), width=170)

st.write("---")

if (pokemon1_species and pokemon1_cp and pokemon1_shadow and pokemon1_fast_move and pokemon1_charge_move1 and pokemon1_charge_move2 and
    pokemon2_species and pokemon2_cp and pokemon2_shadow and pokemon2_fast_move and pokemon2_charge_move1 and pokemon2_charge_move2 and
    pokemon3_species and pokemon3_cp and pokemon3_shadow and pokemon3_fast_move and pokemon3_charge_move1 and pokemon3_charge_move2 and
    pokemon4_species and pokemon4_cp and pokemon4_shadow and pokemon4_fast_move and pokemon4_charge_move1 and pokemon4_charge_move2 and
    pokemon5_species and pokemon5_cp and pokemon5_shadow and pokemon5_fast_move and pokemon5_charge_move1 and pokemon5_charge_move2 and
    pokemon6_species and pokemon6_cp and pokemon6_shadow and pokemon6_fast_move and pokemon6_charge_move1 and pokemon6_charge_move2):

    pokemon1_hex = convert_pokemon_to_hex(
        pokemon1_species, pokemon1_cp, pokemon1_shadow, pokemon1_fast_move, pokemon1_charge_move1, pokemon1_charge_move2)
    pokemon2_hex = convert_pokemon_to_hex(
        pokemon2_species, pokemon2_cp, pokemon2_shadow, pokemon2_fast_move, pokemon2_charge_move1, pokemon2_charge_move2)
    pokemon3_hex = convert_pokemon_to_hex(
        pokemon3_species, pokemon3_cp, pokemon3_shadow, pokemon3_fast_move, pokemon3_charge_move1, pokemon3_charge_move2)
    pokemon4_hex = convert_pokemon_to_hex(
        pokemon4_species, pokemon4_cp, pokemon4_shadow, pokemon4_fast_move, pokemon4_charge_move1, pokemon4_charge_move2)
    pokemon5_hex = convert_pokemon_to_hex(
        pokemon5_species, pokemon5_cp, pokemon5_shadow, pokemon5_fast_move, pokemon5_charge_move1, pokemon5_charge_move2)
    pokemon6_hex = convert_pokemon_to_hex(
        pokemon6_species, pokemon6_cp, pokemon6_shadow, pokemon6_fast_move, pokemon6_charge_move1, pokemon6_charge_move2)

    url_string = "https://localhost:8701/team?id=" + pokemon1_hex + "-" + pokemon2_hex + "-" + pokemon3_hex + "-" + pokemon4_hex + "-" + pokemon5_hex + "-" + pokemon6_hex
    url_string = url_string.replace("0x", "")

    st.write("Share link:")
    st.code(url_string, language="js")
