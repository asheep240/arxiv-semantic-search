import streamlit as st
import question_functions as qf
import pandas as pd


if __name__ == "__main__":
    st.set_page_config(page_title="GPT Scholar")
    archive = st.selectbox("Archive", ["Plasma Physics", "Biology"])

    if archive == "Plasma Physics":
        df = pd.read_pickle("./8500abstracts.pkl")

        st.title("ArXiV Semantic Search")

        if "history" not in st.session_state:
            st.session_state["history"] = []

        st.write("#### Input")
        userQuestion = st.text_input("Query")
        progress = st.progress(0)

        if st.button("Search"):
            answer, metadata = qf.answer_question(df, question=userQuestion)

            st.write("#### Question")
            st.write(userQuestion)
            st.session_state["history"].append(userQuestion)

            st.write("#### Answer")
            st.write(answer)

            st.write("#### References")
            for i in range(8):
                with st.expander(metadata["title"][i]):
                    st.write("Date: " + metadata["date"][i])
                    st.write("Short ID: " + metadata["short_id"][i])

    elif archive == "Biology":
        st.title("BioRxiv Semantic Search")
        st.text("Work in Progress!")
    #
    #     date1 = "/" + st.text_input("Search from: YYYY-MM-DD")
    #     date2 = "/" + st.text_input("to: YYYY-MM-DD")
    #     cursor = "/" + st.text_input("Starting at result #___:")
    #
    #     st.write("#### Input")
    #     userQuestion = st.text_input("Query")
    #     progress = st.progress(0)
    #
    #     if "history" not in st.session_state:
    #         st.session_state["history"] = []
    #
    #     if st.button("Search"):
    #         df, all_results = dbp.request(date1, date2, cursor, userQuestion)
    #         answer = qf.answer_bio_question(all_results, question=userQuestion)
    #
    #         st.write("#### Question")
    #         st.write(userQuestion)
    #         st.session_state["history"].append(userQuestion)
    #
    #         st.write("#### Answer")
    #         st.write(answer)
