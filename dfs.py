graph = {}

n = int(input("Enter number of vertices: "))

for _ in range(n):
    vertex = int(input("\nEnter a vertex: "))
    graph[vertex]=[]
    num_n = int(input("Enter number of neighbors of vertex "+str(vertex)+" :"))

    for _ in range(num_n):
        neighbor = int(input("Enter neighbor: "))
        graph[vertex].append(neighbor)

visited = set()

def dfs(vertex):
    if vertex not in visited:
        print(vertex,end=' ')
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(neighbor)

start = int(input("Enter start vertex: "))
print("\nDFS Tracersal: ")
dfs(start)