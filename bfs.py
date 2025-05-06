from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for _ in range(n):
    vertex = int(input("\nEnter a vertex: "))
    graph[vertex]=[]
    num_n = int(input("Enter number of neighbors of vertex "+str(vertex)+" :"))

    for _ in range(num_n):
        neighbor = int(input("Enter neighbor :"))
        graph[vertex].append(neighbor)

visited = set()

def bfs(start):
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

start_n = int(input("\nEnter start vertex:"))
print("\nBFS Traversal: ")
bfs(start_n)