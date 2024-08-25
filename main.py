from fastapi import FastAPI
from pydantic import BaseModel
from database.query_builder import QueryBuilder
from model.model import EmbeddingModels
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer('sentence-transformers/bert-base-nli-mean-tokens')


class SentenceSerializer(BaseModel):
    sentence: str


@app.post("/search")
async def search(sentence: SentenceSerializer):
    # here should convert to vector embedding and compare to database

    encoded_sentence = model.encode(sentence)

    # TODO: complete the logic of search
    # finding closest to sentence that was given as input logic
    query = QueryBuilder()
    query.select()

    return {f"to "}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
