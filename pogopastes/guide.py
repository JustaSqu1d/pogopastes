import streamlit as st

from images import get_image_asset

st.write("# How to submit a team on Limitless?")

st.write("### 1. Go to the [Create a team](https://pgpaste.squ1d.dev/) page and enter your team.")

st.image(get_image_asset("guide/team_select"), width=800)

st.divider()

st.write("### 2. Scroll down and click on the `Copy Pokepaste text` button to copy the team sheet.")

st.image(get_image_asset("guide/copy_paste"), width=800)

st.divider()

st.write("### 3. Go to your Limitless tournament and complete the registration if you haven't already.")

st.image(get_image_asset("guide/limitless_register"), width=400)

st.divider()

st.write("### 4. Submit your team by clicking the \"Submit\" button.")

st.image(get_image_asset("guide/limitless_teamsheet"), width=400)

st.divider()

st.write("### 5. Paste your team sheet in the text box and click the \"Submit\" button.")

st.image(get_image_asset("guide/limitless_submit"), width=400, clamp=True)

st.divider()

st.write("### 6. You're done! Your team has been submitted.")