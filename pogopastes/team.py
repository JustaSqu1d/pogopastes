import streamlit as st

from images import get_image_asset
from parser import convert_pokemon_hex_to_dictionary, format_pokemon_name, format_move_name, read_pokemon_data, \
    pokepaste_stringify


def render_pokemon(st, poke_dict):
    name_string = format_pokemon_name(poke_dict["pokemon_name"], poke_dict["form_name"])
    st.write(f"### {name_string}")

    st.write(f"**CP: {poke_dict['combat_power']}**")

    st.write(f"**{format_move_name(poke_dict['fast_move_name'])}**")

    st.divider()

    st.write(f"**{format_move_name(poke_dict['first_charged_move_name'])}**")

    if poke_dict["second_charged_move_name"] != "None":
        st.write(f"**{format_move_name(poke_dict['second_charged_move_name'])}**")


def get_pokemon_image(pokemon_name, form_name=None):
    pokemon_data = read_pokemon_data()

    for pokemon in pokemon_data.values():
        pokemon_info = pokemon

        if pokemon_info["species"] == pokemon_name:
            if form_name:
                if pokemon_info["name"] == form_name:
                    showdown_id = pokemon_info["showdown_id"]
                    return f"https://play.pokemonshowdown.com/sprites/gen5/{showdown_id}.png"
            else:
                showdown_id = pokemon_info["showdown_id"]
                return f"https://play.pokemonshowdown.com/sprites/gen5/{showdown_id}.png"

    return None


def render_pokemon_images(st, poke_dict, left, right):
    st.image(get_pokemon_image(poke_dict["pokemon_name"], poke_dict["form_name"]), width=128)

    with left:
        if poke_dict["shadow_purified"] == "Shadow":
            st.image(get_image_asset("shadow"), width=32)
        elif poke_dict["shadow_purified"] == "Purified":
            st.image(get_image_asset("purified"), width=32)

    with right:
        if poke_dict["best_buddy"]:
            st.image(get_image_asset("best_buddy"), width=32)


team = st.query_params.get("id")

if not team:
    team_id = st.text_input("Team ID", key="team")

    if team_id:
        st.page_link(f"https://pgpaste.squ1d.dev/team?id={team_id}", label="View team", icon=":material/link:")

else:
    st.title("Pokemon Team")
    st.write(f"Team ID: `{team}`")
    st.divider()

    teams = team.split("-")

    left, right = st.columns(2)
    with left:
        for entry in teams[:3]:
            try:
                poke_dict = convert_pokemon_hex_to_dictionary(entry)
            except:
                st.write("Invalid team.")
                break

            sub_left, sub_middle, sub_right = st.columns([3, 2, 5])

            with sub_right:
                render_pokemon(st, poke_dict)

            with sub_left:
                render_pokemon_images(st, poke_dict, sub_left, sub_middle)

            st.divider()

    with right:
        for entry in teams[3:]:
            try:
                poke_dict = convert_pokemon_hex_to_dictionary(entry)
            except:
                st.write("Invalid team.")
                break

            sub_left, sub_middle, sub_right = st.columns([3, 2, 5])

            with sub_right:
                render_pokemon(st, poke_dict)

            with sub_left:
                render_pokemon_images(st, poke_dict, sub_left, sub_middle)

            st.divider()

    st.divider()
    st.write("[Pokepaste](https://pokepast.es) format:")
    st.code(pokepaste_stringify(team), language="python")
