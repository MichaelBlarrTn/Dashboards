import streamlit as st

st.title("Tag 2 wird interaktiv"
         "")

is_adult = st.checkbox(label="Volljährig")


if is_adult:
    st.write("Benutzer ist volljährig")
else:
    st.write("Benutzer ist nicht volljährig")

klickbox = st.button("Click mich")

farbe = st.radio("Wähle eine Farbe", ["rot, blau, lila"])
st.write(f"Die ausgewählte Farbe ist:{farbe}")


