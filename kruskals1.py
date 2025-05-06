def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # Path compression
    return parent[node]

def union(parent, u, v):
    parent[v] = u

def kruskal(n, edges):
    parent = {}
    for u, v, _ in edges:
        parent[u] = u
        parent[v] = v

    edges.sort(key=lambda x: x[2])  # Sort by weight

    mst = []
    total_cost = 0

    for u, v, w in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            mst.append((u, v, w))
            total_cost += w
            union(parent, root_u, root_v)

    print("Edges in Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)
    print("Total Cost:", total_cost)

# Input from user
edges = []
n = int(input("Enter number of edges: "))
for _ in range(n):
    u = input("Enter first node: ")
    v = input("Enter second node: ")
    w = int(input("Enter weight: "))
    edges.append((u, v, w))

kruskal(n, edges)
