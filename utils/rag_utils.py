import os
import faiss
import numpy as np

from models.embeddings import load_embedding_model, embed_text

embedding_model = load_embedding_model()

documents = []
index = None
chunks_store = []

def load_documents(folder="data"):
    global documents

    documents = []

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                documents.append(f.read())

    return documents

def split_documents():
    global documents
    chunks = []

    for doc in documents:

        sentences = doc.split(". ")

        temp_chunk = ""

        for sentence in sentences:

            if len(temp_chunk) + len(sentence) < 400:
                temp_chunk += sentence + ". "
            else:
                chunks.append(temp_chunk.strip())
                temp_chunk = sentence + ". "

        if temp_chunk:
            chunks.append(temp_chunk.strip())

    return chunks

def build_vector_index(chunks):
    global index
    global chunks_store

    chunks_store = chunks

    vectors = []

    for chunk in chunks:
        vec = embed_text(embedding_model, chunk)
        vectors.append(vec)

    vectors = np.array(vectors).astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    return index, chunks_store

def retrieve_context(query, chunks, k=3):

    query_vec = embed_text(embedding_model, query)

    query_vec = np.array([query_vec]).astype("float32")

    distances, indices = index.search(query_vec, k)

    results = []

    for i in indices[0]:
        results.append(chunks_store[i])

    return results