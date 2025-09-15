from qdrant_client import QdrantClient
from pytune_configuration.sync_config_singleton import SimpleConfig, config

config = config or SimpleConfig()

client = QdrantClient(
    host=config.QDRANT_HOST,
    port=config.QDRANT_PORT
)
