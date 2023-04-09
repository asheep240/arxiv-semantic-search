import streamlit as st
import QuestionFunctions as qf
import pandas as pd
import time


st.set_page_config(
    page_title="GPT Scholar"
  )

clear_history = st.button("Clear History")

for i in range(len(st.session_state["history"])):
    num = ""
    num = num + str(i+1) + ". "
    next = st.session_state["history"][i]
    st.write(num + next)

if clear_history:
    st.session_state["history"] = []
    for i in range(len(st.session_state["history"])):
        num = ""
        num = num + str(i+1) + ". "
        next = st.session_state["history"][i]
        st.write(next)

