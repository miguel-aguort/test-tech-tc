from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import SQLiteVec
import sqlite3
import sqlite_vec

connection = sqlite3.connect(":memory:")
# Issues working in azure: 
connection.row_factory = sqlite3.Row
connection.enable_load_extension(True)
sqlite_vec.load(connection)

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = SQLiteVec(
    table="state_union",
    db_file=":memory:",
    embedding=embedding_function,
    connection=connection
)

vector_store.add_texts(["Ketanji Brown Jackson is awesome", "foo", "bar"])
vector_store.add_texts(["Carlos Jackson is perfect", "foo", "bar"])
vector_store.add_texts(["Cristina Ramirez is smart", "foo", "bar"])
vector_store.add_texts(["Octavio Perez is cute", "foo", "bar"])
data = vector_store.similarity_search("Ketanji Brown Jackson", k=4)

print(data)