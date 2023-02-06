import pandas as pd
import vehicle_data_per_frame


def add_vertex(v):
    global graph
    global vertices_no
    global vertices

    if v in vertices:
        print('Vertex exists')
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)


def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices

    if v1 not in vertices:
        print('Vertex does not exist')
    elif v2 not in vertices:
        print('Vertex does not exist')
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e


if __name__ == "__main__":
    a = vehicle_data_per_frame.create_list()
    max_x = 32.8084  # 10m to feet
    max_y = 98.4252 - 32.8084  # 30m to feet -> 20m to feet
    for i in range(len(a)):
        print(i, "/", len(a))
        frame = None
        graph = []
        vertices = []
        vertices_no = 0
        x = 2
        y = 3
        skip = 0
        occurrence = len(a[i]) // 7
        column_name = []
        if occurrence == 1:
            frame = a[i][1]
            add_vertex(a[i][0])
            column_name.append(a[i][0])

        while occurrence > 1 and skip <= (occurrence - 1) * 7:
            add_vertex(a[i][0 + skip])
            column_name.append(a[i][0 + skip])
            skip += 7

        if occurrence > 1:
            for j in range(0, occurrence - 1):
                init = 0 + (j * 7)
                init_frame = 1 + (j * 7)
                init_x = 2 + (j * 7)
                init_y = 3 + (j * 7)
                skip = 7
                for k in range(j + 1, occurrence):
                    frame = a[i][init_frame]
                    if a[i][init] != a[i][init+skip]:
                        if abs(a[i][init_x] - a[i][init_x+skip]) <= max_x and \
                                abs(a[i][init_y] - a[i][init_y+skip]) <= max_y:
                            add_edge(a[i][init], a[i][init+skip], 1)

                            add_edge(a[i][init+skip], a[i][init], 1)
                        skip += 7

        path = f'./testestetst/{frame}_output.csv'
        df = pd.DataFrame.from_records(graph)
        df.columns = column_name
        df.index = column_name
        df.to_csv(path, index=True)
