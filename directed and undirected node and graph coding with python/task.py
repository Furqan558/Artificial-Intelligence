def find_path(graph, start, end, path=[]):
    path = path + [start]
    # make a list to check if the node is visited or not and if the node is visited
    # then it means it has completed nodes check at that level
    all_paths = []
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:

            newpath = find_path(graph, node, end, path)
            if newpath:
                all_paths.append(newpath)
    return all_paths


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'F'],
         'D': ['C', 'E'],
         'E': ['F'],
         'F': ['C', 'E']}

print(find_path(graph, 'A', 'D'))
