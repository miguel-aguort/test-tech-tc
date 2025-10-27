from utils.components import node1, node2
from langgraph.graph import StateGraph, START, END

graph = StateGraph(str)
# Add the nodes
graph.add_node("node_1", node1)
graph.add_node("node_2", node2)

graph.add_edge(START, "node_1")
graph.add_edge("node_1", "node_2")
graph.add_edge("node_2", END)
graph = graph.compile()


input_data = "hello world!"
if __name__ == "__main__":
    response = graph.invoke(input_data)
    print(response)
