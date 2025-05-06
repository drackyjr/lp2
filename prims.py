def prim_mst(graph, start):
    visited = set()
    mst = []
    total_cost = 0

    visited.add(start)

    while len(visited) < len(graph):
        min_edge = None
        min_weight = float('inf')

        for u in visited:
            for v, w in graph[u]:
                if v not in visited and w < min_weight:
                    min_edge = (u, v, w)
                    min_weight = w

        if min_edge:
            u, v, w = min_edge
            visited.add(v)
            mst.append((u, v, w))
            total_cost += w

    print("Minimum Spanning Tree Edges:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)
    print("Total Cost:", total_cost)

# Take user input for graph
graph = {}
n = int(input("Enter number of vertices: "))
for _ in range(n):
    node = input("Enter node name: ")
    graph[node] = []

e = int(input("Enter number of edges: "))
for _ in range(e):
    u = input("Enter first node: ")
    v = input("Enter second node: ")
    w = int(input("Enter weight of edge: "))
    graph[u].append((v, w))
    graph[v].append((u, w))

start_node = input("Enter starting node for Prim's Algorithm: ")
prim_mst(graph, start_node)
