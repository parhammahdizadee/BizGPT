import datetime


class EmbeddingModels:
    __table_name__ = 'embeddings'
    id = "id"
    title = "title"
    embedding = "embedding"
    created_at = "created_at"


def __init__(self):
    self.id = None
    self.title = None
    self.embedding = None
    self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
