import json
import os

import streamlit as st
from images import get_pokemon_image
from parser import format_pokemon_name, format_move_name, convert_pokemon_to_hex, pokepaste_stringify

pokemon_species_list = []

path = os.path.dirname(__file__)

with open(path + "/gamedata/pokemon.json", "r") as f:
    pokemon_gamemasters = json.load(f)
    for pokemon in pokemon_gamemasters:
        pokemon_species_list.append(
            format_pokemon_name(pokemon_gamemasters[pokemon]["species"], pokemon_gamemasters[pokemon]["name"]))

moves_list = []

skip_ids = ["HYDRO_PUMP_BLASTOISE", "SCALD_BLASTOISE", "WATER_GUN_BLASTOISE"]

with open(path + "/gamedata/moves.json", "r") as f:
    moves_gamemasters = json.load(f)
    for move in moves_gamemasters:
        if move in skip_ids:
            continue

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

if (
        pokemon1_species and pokemon1_cp and pokemon1_shadow and pokemon1_fast_move and pokemon1_charge_move1 and pokemon1_charge_move2 and
        pokemon2_species and pokemon2_cp and pokemon2_shadow and pokemon2_fast_move and pokemon2_charge_move1 and pokemon2_charge_move2 and
        pokemon3_species and pokemon3_cp and pokemon3_shadow and pokemon3_fast_move and pokemon3_charge_move1 and pokemon3_charge_move2 and
        pokemon4_species and pokemon4_cp and pokemon4_shadow and pokemon4_fast_move and pokemon4_charge_move1 and pokemon4_charge_move2 and
        pokemon5_species and pokemon5_cp and pokemon5_shadow and pokemon5_fast_move and pokemon5_charge_move1 and pokemon5_charge_move2 and
        pokemon6_species and pokemon6_cp and pokemon6_shadow and pokemon6_fast_move and pokemon6_charge_move1 and pokemon6_charge_move2):
    pokemon1_hex = convert_pokemon_to_hex(
        pokemon1_species, pokemon1_cp, pokemon1_shadow, pokemon1_fast_move, pokemon1_charge_move1,
        pokemon1_charge_move2)
    pokemon2_hex = convert_pokemon_to_hex(
        pokemon2_species, pokemon2_cp, pokemon2_shadow, pokemon2_fast_move, pokemon2_charge_move1,
        pokemon2_charge_move2)
    pokemon3_hex = convert_pokemon_to_hex(
        pokemon3_species, pokemon3_cp, pokemon3_shadow, pokemon3_fast_move, pokemon3_charge_move1,
        pokemon3_charge_move2)
    pokemon4_hex = convert_pokemon_to_hex(
        pokemon4_species, pokemon4_cp, pokemon4_shadow, pokemon4_fast_move, pokemon4_charge_move1,
        pokemon4_charge_move2)
    pokemon5_hex = convert_pokemon_to_hex(
        pokemon5_species, pokemon5_cp, pokemon5_shadow, pokemon5_fast_move, pokemon5_charge_move1,
        pokemon5_charge_move2)
    pokemon6_hex = convert_pokemon_to_hex(
        pokemon6_species, pokemon6_cp, pokemon6_shadow, pokemon6_fast_move, pokemon6_charge_move1,
        pokemon6_charge_move2)

    hexes = [pokemon1_hex, pokemon2_hex, pokemon3_hex, pokemon4_hex, pokemon5_hex, pokemon6_hex]
    hexes = sorted(hexes)

    url_string = "https://pgpaste.squ1d.dev/team?id=" + "-".join(hexes)
    url_string = url_string.replace("0x", "")

    st.write("Share link:")
    st.code(url_string, language="js")

    st.write("[Pokepaste](https://pokepast.es) format:")
    st.code(pokepaste_stringify("-".join(hexes)), language="python")

