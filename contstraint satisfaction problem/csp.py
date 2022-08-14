graph = [
    ["A", -1, "D", "E"],
    ["B", "C", -1, -1],
    [-1, -1, "F", -1]
]
rows = len(graph)
cols = len(graph[0])
p = ["x", "y", "z"]
q = ["a", "b"]
r = ["s"]

# graph
for row in range(rows):
    for col in range(cols):
        print(graph[row][col])
