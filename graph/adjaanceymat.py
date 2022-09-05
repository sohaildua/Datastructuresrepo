import pprint
row_num = 6
col_num = 6
adjacency_matrix = []
for i in range(row_num):
    row = []
    for j in range(col_num):
        row.append(0)
    adjacency_matrix.append(row)

edges = [(1, 2), (2, 4), (2, 3), (3, 4), (4, 5), (3, 6), (5, 6)]
for edge in edges:
    row = edge[0]

    col = edge[1]
    adjacency_matrix[row - 1][col - 1] = 1
    adjacency_matrix[col - 1][row - 1] = 1

print("The edges in the graph are:")
print(edges)
print("The adjacency matrix is:")
pprint.pprint(adjacency_matrix)