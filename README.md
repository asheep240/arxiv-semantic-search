# arxiv-semantic-search
## Web Application
### https://gpt-scholar.streamlit.app

## Intro
Research is often an inefficient, time-consuming endeavor. When approaching new concepts, obtaining background knowledge requires a student or researcher to read through many long papers before they can begin their own work. This is an application to provide graduate students and researchers with an efficient means of obtaining answers to questions during the course of their research. A user can input a natural language query, and by reading data from papers most relevant to the query and contextualizing it, the program provides a response explaining in natural language the answer to the question. Especially when researchers are not familiar with the complexities of issues that have already been answered, this will expedite research processes by removing the need to comb through extensive databases for research papers, and will significantly reduce the time required to gain preliminary knowledge, making research more accessible.

## How it works

This project uses an OpenAI API to return a natural language response to a natural language user query based on context from matched arXiv/bioRxiv papers. Papers are stored using a Pinecone database. The relevancy of papers is calculated using the distance of embeddings generated as numpy arrays for the question and each paper. The most relevant papers are then fed through the OpenAI API and used to provide context for the engine's response to the user query. The response to the query is also cached, so inputting the same question twice without clearing the cache will yield the same response. This response and the references are printed, and the user's query is added to a temporary history.


