from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import SQLiteVec

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = SQLiteVec(
    table="state_union", db_file="../data/tmp/vec.db", embedding=embedding_function
)

vector_store.add_texts(texts=["Ketanji Brown Jackson is awesome", "foo", "bar"])

data = vector_store.similarity_search("Ketanji Brown Jackson", k=4)