from database.query_builder import QueryBuilder
from model.model import EmbeddingModels


class EmbeddingsDao:
    def __init__(self):
        self.db = QueryBuilder("embeddings")

    def insert_new_embedding(self, model: EmbeddingModels):
        try:
            self.db.insert(model)
        except Exception as error:
            raise error

