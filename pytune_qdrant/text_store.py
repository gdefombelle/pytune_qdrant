from qdrant_client.http.models import PointStruct
from .client import client
from uuid import uuid4

def upsert_text_chunk(text: str, embedding: list[float], metadata: dict, collection="semantic_memory"):
    payload = {"text": text, **metadata}
    client.upsert(
        collection_name=collection,
        points=[
            PointStruct(
                id=str(uuid4()),
                vector=embedding,
                payload=payload
            )
        ]
    )

def search_similar_text(embedding: list[float], top_k=5, collection="semantic_memory", filters=None):
    return client.search(
        collection_name=collection,
        query_vector=embedding,
        limit=top_k,
        query_filter=filters
    )
