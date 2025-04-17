import streamlit as st
from utils import  save_state_json

def welcome_page():
    st.title("Herzlich willkommen!")
    st.markdown("""
    Mit dieser App können Sie eine erste Einschätzung zu auffälligen Hautveränderungen erhalten und darauf basierend entscheiden, ob Sie einen Arzttermin vereinbaren möchten.

    **So funktioniert es:**
    1. **Identifikation** - Bitte geben Sie Ihre anonyme ID auf der folgenden Seite ein. 
    \n
    2. **Hochgeladenes Foto** – Erfassen Sie die betroffene Hautstelle. 
    \n
    3. **Mit dem KI-Assistenten chatten** – Interagieren Sie mit dem künstlich intelligenten Assistenten und entscheiden Sie darauf basierend, ob Sie einen Arzttermin vereinbaren möchten.
    """)
    if st.button("Zum Fragebogen"):
        st.session_state["page"] = "survey"
        save_state_json()

        st.rerun()