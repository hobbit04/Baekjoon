# Algorithm: Graph, DFS
# Data structure: neighbor list
com_num = int(input())
node_num = int(input())

graph = {}
for i in range(com_num):
    graph[i+1] = []  # initialize graph

for i in range(node_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

infected = [1]

stack = [1]
while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if neighbor not in infected:
            infected.append(neighbor)
            stack.append(neighbor)

print(len(infected) - 1)