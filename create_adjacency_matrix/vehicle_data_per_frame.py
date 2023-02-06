import pandas as pd

# NO NEED TO RUN THIS SEPARATELY


# combine multiple lists of data into one
def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list


def create_list():
    sorted_file = pd.read_csv('sorted.csv')
    count_file = pd.read_csv('count.csv')
    counter = -1
    data = []
    final_list = []
    frame = None

    for i in range(len(count_file)):
        flag = -1    # flag to indicate when all vehicles with the same Frame_ID is found
        for j in range(count_file["Occurrence"][i]):
            counter += 1    # Counter to know which entry to look at in sorted_file
            flag += 1
            # print(j, sorted_file["Frame_ID"][counter], counter)
            # Find the edge once all the vehicles with the same Frame_ID is found
            if flag == count_file["Occurrence"][i] - 1:
                # Go back and find every vehicle with the same Frame_ID. Subtract flag each time until 0
                for k in range(count_file["Occurrence"][i]):
                    # print(sorted_file["Vehicle_ID"][counter - flag])
                    data.append([
                        sorted_file["Vehicle_ID"][counter - flag],
                        sorted_file["Frame_ID"][counter - flag],
                        sorted_file["Local_X"][counter - flag],
                        sorted_file["Local_Y"][counter - flag],
                        sorted_file["v_Vel"][counter - flag],
                        sorted_file["v_Acc"][counter - flag],
                        sorted_file["Lane_ID"][counter - flag]
                    ])

                    if flag != 0:
                        flag -= 1
                ans = flatten(data)
                final_list.append(ans)
                data = []

    return final_list



