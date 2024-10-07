import streamlit as st
from parser import convert_pokemon_hex_to_dictionary


team = st.query_params.get("id")

if not team:
    st.write("No team found.")

else:
    st.title("Pokemon Team")
    st.write(f"Team ID: `{team}`")

    teams = team.split("-")

    left, right = st.columns(2)
    with left:
        for team in teams[:3]:
            poke_dict = convert_pokemon_hex_to_dictionary(team)
            st.json(poke_dict)

    with right:
        for team in teams[3:]:
            poke_dict = convert_pokemon_hex_to_dictionary(team)
            st.json(poke_dict)