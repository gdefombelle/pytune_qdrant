from qdrant_client.http.models import PointStruct
from .client import client
from uuid import uuid4

def upsert_image_vector(vector: list[float], metadata: dict, collection="piano_images"):
    """Stocke un vecteur image CLIP + metadata dans Qdrant."""
    payload = {"type": "image", **metadata}
    client.upsert(
        collection_name=collection,
        points=[
            PointStruct(
                id=str(uuid4()),
                vector=vector,
                payload=payload
            )
        ]
    )

def search_similar_images(vector: list[float], top_k=5, collection="piano_images", filters=None):
    """Recherche d’images visuellement proches (embedding CLIP)."""
    return client.search(
        collection_name=collection,
        query_vector=vector,
        limit=top_k,
        query_filter=filters
    )
