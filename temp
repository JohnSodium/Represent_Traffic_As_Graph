import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import count_lc
from scipy.linalg import fractional_matrix_power

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


lc_frame = count_lc.get_Swap_Frame()
prev_frame = None
node_data = None

lc_frame = lc_frame[:10]
for i in range(len(lc_frame)):
    print(lc_frame[i])
    feature_vector = pd.read_csv(f"./new_input_feature_matrix_20maxy/"
                                 f"{lc_frame[i]}_features_with_label.csv")
    G = nx.Graph(name="G")

    vehicle_list = []
    edges = []

    source_features = []
    target_features = []
    node_features = []

    for j in range(len(feature_vector)):
        print(j, '/', len(feature_vector))
        cur_frame = int(feature_vector["Frame"][j])
        if cur_frame != prev_frame:
            node_data = pd.read_csv(f"./adjacency_matrix/{cur_frame}_output.csv")

            # Find connections between vehicles using the adjacency matrix
            for index, row in node_data.iterrows():
                for k in range(1, len(row.index)):
                    if k == 1 and int(row[0]) not in vehicle_list:  # only add vehicle_id once
                        vehicle_list.append(int(row[0]))
                    # Create an edge when there is a connection between two vehicles
                    if row[k] == 1:
                        # print(int(row[0]), int(row.index[k]))
                        edges.append((int(row[0]), int(row.index[k])))

                        # Obtain features for the source node
                        separate_by_id_source = feature_vector[feature_vector['Vehicle_ID'] == row[0]]
                        separate_by_frame_source = separate_by_id_source[separate_by_id_source['Frame'] == cur_frame]

                        source_features.append(separate_by_frame_source.values.tolist())

                        # Obtain features for the target node
                        separate_by_id_target = feature_vector[feature_vector['Vehicle_ID'] == int(row.index[k])]
                        separate_by_frame_target = separate_by_id_target[separate_by_id_target['Frame'] == cur_frame]

                        target_features.append(separate_by_frame_target.values.tolist())

            # End of the iteration, previous frame becomes current frame
            prev_frame = cur_frame

    # Concatenate source_features and target_features
    for j in range(len(source_features)):
        for k in source_features[j]:
            node_features.append(k)
        for k in target_features[j]:
            node_features[len(node_features) - 1] = node_features[len(node_features) - 1] + k

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
    plt.figure(3, figsize=(12, 12))
    nx.draw_circular(G, with_labels=True, font_weight='bold')
    plt.show()

