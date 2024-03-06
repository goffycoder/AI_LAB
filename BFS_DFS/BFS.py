import collections

def tsp_bfs(graph, start):
    queue = collections.deque([(start, [start], 0)])
    min_cost = float('inf')
    while queue:
        current, path, cost = queue.popleft()
        if len(path) == N:
            if graph[current][start]:
                min_cost = min(min_cost, cost + graph[current][start])
        else:
            for i in range(N):
                if i not in path and graph[current][i]:
                    new_path = path + [i]
                    new_cost = cost + graph[current][i]
                    queue.append((i, new_path, new_cost))
    return min_cost

# Measure execution time for BFS
start_time = time.time()
bfs_cost = tsp_bfs(graph, start_node)
bfs_time = time.time() - start_time

print("BFS Cost:", bfs_cost)
print("BFS Execution Time:", bfs_time)
