import pandas as pd
import numpy as np


lc_data = pd.read_csv("swapdata_0515-0530.csv")

for i in range(len(lc_data)):
    print(i, "/", len(lc_data))
    count = 0
    frame_no = lc_data["Frame"][i]
    lc_vehicle_id = lc_data["ID"][i]

    vehicle_id = []
    frame = []
    local_x = []
    local_y = []
    v_vel = []
    v_acc = []
    lane_id = []
    label = []

    for j in range(50, 0, -1):
        d = {}

        cur_frame = frame_no - j
        input_features = pd.read_csv(f"./input_Feature_matrix/{cur_frame}_feature_matrix_output.csv")
        adjacency = pd.read_csv(f"./adjacency_matrix/{cur_frame}_output.csv")

        for l, (index, row) in enumerate(input_features.iterrows()):
            vector = []
            for k in range(1, len(row)):
                vector.append(row[k])
            d[row[0].astype(int)] = vector

        for k, (index, row) in enumerate(adjacency.iterrows()):
            # print(row)
            # print(d.items())
            for m in range(1, len(row)):
                if row[0] == lc_vehicle_id:
                    # print(row[0], row.index[m])
                    # print(d.keys())
                    temp = row.index[m]
                    key_lookup = int(temp)  # make this into an integer or not able to be found in dict
                    if key_lookup in d.keys():
                        values = d[key_lookup]
                        vehicle_id.append(key_lookup)
                        for n in range(len(values)):
                            if n == 0:
                                frame.append(values[0])
                            elif n == 1:
                                local_x.append(values[1])
                            elif n == 2:
                                local_y.append(values[2])
                            elif n == 3:
                                v_vel.append(values[3])
                            elif n == 4:
                                v_acc.append(values[4])
                            elif n == 5:
                                lane_id.append(values[5])

                        # print(lc_vehicle_id, key_lookup)
                        if row[m] == 0 and lc_vehicle_id != key_lookup:
                            label.append("2")
                        elif int(lc_vehicle_id) == int(key_lookup):
                            label.append("1")
                        else:
                            label.append("0")

                    # print(vehicle_id, status)

    data = np.array(list(zip(vehicle_id, frame, local_x, local_y, v_vel, v_acc, lane_id, label)))
    df = pd.DataFrame.from_records(data, columns=["Vehicle_ID", "Frame", "Local_X", "Local_Y", "V_Vel", "V_Acc",
                                                  "Lane_ID", "Label"])
    path = f'./new_input_feature_matrix_20maxy/{frame_no}_features_with_label.csv'
    df.to_csv(path, index=False)

