from sentence_transformers import SentenceTransformer


def load_embedding_model():
    """
    Load sentence transformer embedding model
    """
    try:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        return model

    except Exception as e:
        print(f"Embedding model error: {e}")
        return None


def embed_text(model, text):
    """
    Convert text into vector embedding
    """
    try:
        return model.encode(text)

    except Exception as e:
        print(f"Embedding generation error: {e}")
        return None