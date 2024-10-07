import streamlit as st

st.set_page_config(page_title="PoGO Pastes", page_icon=":material/content_paste:", layout="wide")

create_page = st.Page("home.py", title="Create a team")
delete_page = st.Page("team.py", title="View a team")

pg = st.navigation([create_page, delete_page])
pg.run()