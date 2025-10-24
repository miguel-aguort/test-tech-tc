from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import SQLiteVec
import sqlite3

# Step 1: Create a connection to the SQLite database
connection = sqlite3.connect("./data/tmp/vec.db")

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = SQLiteVec(
    table="state_union", 
    db_file="./data/tmp/vec.db", 
    embedding=embedding_function, 
    connection=connection
)

vector_store.add_texts(texts=["Ketanji Brown Jackson is awesome", "foo", "bar"])
connection.commit()

data = vector_store.similarity_search("Ketanji Brown Jackson", k=4)

connection.close()