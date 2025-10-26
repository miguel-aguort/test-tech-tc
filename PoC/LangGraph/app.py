from utils.components import node1, node2
from langgraph.graph import Graph

# Create a new Graph
workflow = Graph()

# Add the nodes
workflow.add_node("node_1", node1)
workflow.add_node("node_2", node2)

# Add the Edges
workflow.add_edge("node_1", "node_2")
workflow.set_entry_point("node_1")
workflow.set_finish_point("node_2")

#Run the workflow
app = workflow.compile()

input_data = "hello world!"
if __name__ == "__main__":
    response = app.invoke(input=input_data)
    print(response)