import streamlit as st

st.title("Dashboard: Kennzahlen 2024")



st.header("Finanzen")
st.metric(label="Umsatz", value="2,5 Mio €", delta="+5 %")
    
st.header("Kunden")
st.metric(label="Kundenanzahl", value="8.420", delta="+120")

st.header("Mitarbeitende")
st.metric(label="Zufriedenheit", value="87 %", delta="-2 %")

st.sidebar.title("Menue")
st.sidebar.link_button(label="Etwas Entspannung", url="http://www.youtube.de")
st.sidebar.link_button(label="Chef Button", url="http://www.markdown.de")



        

