import streamlit as st
import pandas as pd
import json

if "dc_df" not in st.session_state:
    with open("dc_characters.json", "r") as file:
        data = json.load(file)
       
        st.session_state.dc_df = pd.DataFrame(data["character_data"])

df = st.session_state.dc_df

st.title("DC Character Stats Explorer")

character_names = list(df["name"].sort_values())

selected_char = st.selectbox("Select a Character:", character_names)

character_info = df[df["name"] == selected_char].iloc[0]

st.write("Lifting Weight: " + str(character_info["lifting_weight"]))
st.write("Speed: " + str(character_info["speed"]))
if "notes" in character_info and pd.notna(character_info["notes"]) and character_info["notes"] != "":
    st.write("Notes:" + str(character_info["notes"]))