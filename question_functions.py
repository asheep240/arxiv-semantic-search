import os

import openai
from collections import defaultdict
from openai.embeddings_utils import get_embedding, distances_from_embeddings
import streamlit as st

openai.api_key = os.environ["OPENAI_API_KEY"]


@st.cache_data
def create_context(question, df, max_len=1800, size="ada"):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """

    # Get the embeddings for the question
    q_embeddings = get_embedding(text=question, engine="text-embedding-ada-002")

    # Get the distances from the embeddings
    df["distances"] = distances_from_embeddings(q_embeddings, df["embedding"].values, distance_metric="cosine")

    returns = []
    metadata = defaultdict(list)

    cur_len = 0

    # Sort by distance and add the text to the context until the context is too long
    for i, row in df.sort_values("distances", ascending=True).iterrows():
        # Add the length of the text to the current length
        cur_len += row["n_tokens"] + 4

        # If the context is too long, break
        if cur_len > max_len:
            break

        # Else add it to the text that is being returned
        returns.append(row["abstract"])
        metadata["title"].append(row["title"])
        metadata["date"].append(row["date"])
        # metadata["authors"].append(row["authors"])
        metadata["short_id"].append(row["short_id"])

    # Return the context
    return "\n\n###\n\n".join(returns), metadata


@st.cache_data
def answer_question(
    df,
    model="text-davinci-003",
    question="Am I allowed to publish model outputs to Twitter, without a human review?",
    max_len=1800,
    size="ada",
    debug=False,
    max_tokens=500,
    stop_sequence=None,
):
    """
    Answer a question based on the most similar context from the dataframe texts
    """
    context, metadata = create_context(
        question,
        df,
        max_len=max_len,
        size=size,
    )
    # If debug, print the raw model response
    if debug:
        print("Context:\n" + context)
        print("\n\n")

    try:
        # Create a completions using the question and context
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful graduate professor."},
                {
                    "role": "user",
                    "content": f"Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
                },
            ],
        )
        print(response)

        return response["choices"][0]["message"]["content"].strip(), metadata

    except Exception as e:
        print(e)
        return ""
