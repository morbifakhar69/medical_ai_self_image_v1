import streamlit as st
from tipi import calculate_scores
import json
from utils import  save_state_json
def submit_survey():
    st.session_state["survey_completed"] = True
    st.session_state["tipi_scores"] = calculate_scores(st.session_state["survey"])
    st.session_state["page"] = "chat"

def survey():
    if "survey" not in st.session_state:
        st.session_state["survey"] = {}

    file_path = "questionarre/deutsch_questionarre_slider.json"

    st.title("Identifikation")

    st.markdown("Bitte geben Sie Ihre ID ein")
   # name = st.text_input("ID", value=st.session_state["survey"].get("ID", ""))


    with st.form(key="my_form"):
        name = st.text_input("ID", value=st.session_state["survey"].get("ID", ""))


        # Abfrage nach Hautfarbe
       
    
        # Submit button
        submit_button = st.form_submit_button("Absenden")

    if submit_button:
        
        if name == "":
            st.error("Bitte geben Sie Ihre ID ein.")
        
        else:
            st.success("Vielen Dank für Ihre Antworten!")
            st.write("### Ihre Auswahl:")
        
            st.session_state["page"] = "chat"
            print('Survey Data: ',st.session_state["survey"] )
            save_state_json()
            st.rerun()
