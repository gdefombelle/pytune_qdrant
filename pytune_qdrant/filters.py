from qdrant_client.http.models import Filter, FieldCondition, MatchValue

def make_filter(**kwargs) -> Filter:
    return Filter(
        must=[
            FieldCondition(
                key=k,
                match=MatchValue(value=v)
            ) for k, v in kwargs.items()
        ]
    )
