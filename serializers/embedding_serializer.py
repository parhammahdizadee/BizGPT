class EmbeddingSerializer(object):
    def __init__(self, *initial_data, **kwargs):
        self.title = None
        self.embedding = None

        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
