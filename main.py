import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import fractional_matrix_power

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


for i in range(0, 1):
    node_data = pd.read_csv(f"./adjacency_matrix/{i+400}_output.csv")

    G = nx.Graph(name="G")

    vehicle_list = []
    edges = []

    # Find connections between vehicles using the adjacency matrix
    for index, row in node_data.iterrows():

        for j in range(1, len(row.index)):
            if j == 1:  # only add vehicle_id once
                vehicle_list.append(row[0])

            # Create an edge when there is a connection between two vehicles
            if row[j] == 1:
                edges.append((int(row[0]), int(row.index[j])))

    # Create nodes based on the number of vehicles in the scene
    for j in range(len(vehicle_list)):
        G.add_node(vehicle_list[j], name=vehicle_list[j])

    # Add edges to the graph
    G.add_edges_from(edges)

    # See graph info
    print('Graph_Info:\n', nx.info(G))

    # Inspect the node features
    print('\nGraph Nodes: ', G.nodes.data())

    # Plot the graph
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
