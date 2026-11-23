import json
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Load files
with open("hetionet-v1.0.json", "r") as f:
    graph_data = json.load(f)

with open("hetionet-v1.0-metagraph.json", "r") as f:
    metagraph = json.load(f)

# # Inspect structure
# print(type(graph_data), graph_data.keys())
# print("\nMetagraph:", metagraph.keys())

# # To understand graph
# print("\nFirst node:", graph_data["nodes"][0])
# print("\nFirst edge:" ,graph_data["edges"][0])
# print("\nNode types:", metagraph["metanode_kinds"])
# print("\nRelationship types:", metagraph["metaedge_tuples"])

nodes = pd.DataFrame(graph_data["nodes"])
edges = pd.DataFrame(graph_data["edges"])

# Number of nodes & edges
print("Nodes:", len(nodes))
print("Edges:", len(edges))

# Table view of distribution of types of nodes & edges
node_counts = nodes["kind"].value_counts()
edge_counts = edges["kind"].value_counts()
print(node_counts)
print(edge_counts)

# Plots distribution of types of nodes & edges
node_counts.plot(kind="bar", figsize=(10, 5))
plt.ylabel("Number of Nodes")
plt.title("Distribution of Node Types")
plt.xticks(rotation=45)  # make x-axis labels readable
plt.tight_layout()
plt.show()

edge_counts.plot(kind="bar", figsize=(10, 5))
plt.ylabel("Number of Edges")
plt.title("Distribution of Relationship Types")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
