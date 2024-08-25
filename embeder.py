import json

from sentence_transformers import SentenceTransformer
import markdown
import re

from database.query_builder import QueryBuilder
from serializers.embedding_serializer import EmbeddingSerializer
from model.model import EmbeddingModels
model = SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')


def markdown_to_text(markdown_content):
    html = markdown.markdown(markdown_content)
    sentences = re.split('<h3>', html)
    sentence_list = list()
    for sentence in sentences:
        text = re.sub(r'<h3>', '', sentence)
        text = re.sub(r'</h3>', '', text)
        text = re.sub(r'\n', '', text)

        sentence_list.append(text.strip())
    sentence_list.pop(0)
    return sentence_list


def text_to_embeddings(text):
    embedding = model.encode(text)
    return embedding


def markdown_to_embedding(file_name):
    query_builder = QueryBuilder(EmbeddingModels.__table_name__)

    with open(file_name, 'r', encoding='utf-8') as file_data:
        markdown_content = file_data.read()
        text_content = markdown_to_text(markdown_content)
        for sentence in text_content:
            converted_embeddings = text_to_embeddings(sentence)
            embedding_json = json.dumps(converted_embeddings.tolist())
            serializer_object = EmbeddingSerializer(
                embedding=embedding_json
            )
            query_builder.insert(serializer_object)


markdown_to_embedding('laws_data.md')
