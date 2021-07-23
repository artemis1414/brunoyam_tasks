def bfs(graph, start):
    queue = [start]
    visited = []
    while queue:
        for top in queue:
            if top not in visited:
                queue = queue + graph[top]
                visited.append(top)
            queue.remove(top)

    return visited


graph = {'0': ['1', '2', '3'], '1': ['0', '4', '5'], '2': ['0', '4', '6'], '3': ['0', '6'], '4': ['1', '2', '9'],
         '5': ['1', '7'], '6': ['2', '3'], '7': ['5', '8'], '8': ['7'], '9': ['4']}

print(bfs(graph, '9'))
