from sentence_transformers import SentenceTransformer
import markdown
import re

from database.query_builder import QueryBuilder
from serializers.embedding_serializer import EmbeddingSerializer

model = SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')


def markdown_to_text(markdown_content):
    html = markdown.markdown(markdown_content)
    text = re.sub(r'###', '', html)

    return text.strip()


def text_to_embeddings(text):
    embedding = model.encode(text)
    return embedding


def markdown_to_embedding(file_name):

    dict_embeddings = dict()
    query_builder = QueryBuilder('embeddings')

    with open(file_name, 'r', encoding='utf-8') as file_data:
        markdown_content = file_data.read()
        text_content = markdown_to_text(markdown_content)
        converted_embeddings = text_to_embeddings(text_content)
        dict_embeddings.update({markdown_content: converted_embeddings.tolist()})
        serializer_object = EmbeddingSerializer(
            title=text_content,
            embedding=converted_embeddings.tolist()
        )
        query_builder.insert(serializer_object)


markdown_to_embedding('laws_data.md')
