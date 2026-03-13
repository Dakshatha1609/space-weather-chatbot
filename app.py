import streamlit as st

from models.llm import load_llm
from utils.rag_utils import load_documents, split_documents, build_vector_index, retrieve_context
from utils.web_search import search_web

st.set_page_config(page_title="Space Weather Knowledge Assistant", layout="wide")
st.title("Space Weather Knowledge Assistant")

st.write(
"This assistant answers questions about solar activity, geomagnetic storms and space weather using a knowledge base and live web information."
)

st.write("System Features:")
st.write("RAG based document retrieval")
st.write("Live web search fallback")
st.write("Concise and detailed response modes")

llm = load_llm()

docs = load_documents()

chunks = split_documents()

index, chunks = build_vector_index(chunks)

st.sidebar.header("Chat Settings")

mode = st.sidebar.selectbox(
    "Response Mode",
    ["Concise", "Detailed"]
)

st.sidebar.header("Knowledge Base")

st.sidebar.write("Documents loaded:", len(docs))
st.sidebar.write("Text chunks created:", len(chunks))

st.sidebar.header("Live Space Weather Updates")

if st.sidebar.button("Get Latest Updates"):

    news_query = "latest solar storm solar flare space weather news"

    web_info = search_web(news_query)

    prompt = f"""
Summarize the following information about recent space weather activity.

Information:
{web_info}
"""

    response = llm.invoke(prompt)

    st.sidebar.write("Recent Space Weather Activity")
    st.sidebar.write(response.content)

st.sidebar.header("Example Questions")

st.sidebar.write("What is space weather?")
st.sidebar.write("What is a solar flare?")
st.sidebar.write("What is the Kp index?")
st.sidebar.write("How do geomagnetic storms affect satellites?")
st.sidebar.write("Is there a solar storm today?")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


query = st.chat_input("Ask a question about space weather")


if query:

    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.write(query)


    contexts = retrieve_context(query, chunks)

    context_text = " ".join(contexts)

    if context_text.strip() == "":
        context_text = search_web(query)

    if mode == "Concise":
        instruction = "Answer briefly in two or three sentences."
    else:
        instruction = "Provide a detailed explanation."


    prompt = f"""
You are a scientific assistant specializing in space weather.

Context:
{context_text}

Question:
{query}

Instruction:
{instruction}
"""


    response = llm.invoke(prompt)

    answer = response.content


    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.expander("Retrieved Knowledge Sources"):

        if len(contexts) == 0:
            st.write("Information retrieved from live web search")
        else:
            for i, ctx in enumerate(contexts):
                st.write("Source", i + 1)
                st.write(ctx)
                st.write("")