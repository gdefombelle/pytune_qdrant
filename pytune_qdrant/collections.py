from qdrant_client.http.models import VectorParams, Distance
from .client import client

def ensure_text_collection(name="semantic_memory", size=1536):
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=size, distance=Distance.COSINE)
        )
