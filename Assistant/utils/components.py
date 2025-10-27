from langgraph.graph import StateGraph, START, END
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import SQLiteVec
import sqlite3
import sqlite_vec

def node1(str, vector_db):
  docs = vector_db.similarity_search(str, k=2)
  results = [doc.page_content for doc in docs]
  return "\n\n".join(results)

def node2(str):
  return "Prompt: " + str

def init_graph(vector_db):
  graph = StateGraph(str)
  # Add the nodes
  graph.add_node("node_1", lambda s: node1(s, vector_db))
  graph.add_node("node_2", node2)

  graph.add_edge(START, "node_1")
  graph.add_edge("node_1", "node_2")
  graph.add_edge("node_2", END)
  return graph.compile()


# input_data = "hello world!"
# if __name__ == "__main__":
#     app = init_graph()
#     response = app.invoke(input=input_data)
#     print(response)