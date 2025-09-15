from qdrant_client.http.models import VectorParams, Distance
from .client import client

def ensure_image_collection(name="piano_images", size=512):
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=size, distance=Distance.COSINE)
        )
