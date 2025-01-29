# Data structure: Adjacent graph using dictionary
# e.g. {(1, 1): [(2, 1)], ...}
# Algorithm: BFS using distance dictionary

import sys

n, m = map(int, input().split())
graph = {}

# Construct adjacent graph
for i in range(n):
    line = sys.stdin.readline()

    for j in range(m):
        if line[j] == '1':
            graph[(i, j)] = []
for i in range(n):
    for j in range(m):
        if (i, j) not in graph:
            continue

        left = (i, max(j-1, 0))
        right = (i, min(j+1, m-1))
        up = (max(i-1, 0), j)
        down = (min(i+1, n-1), j)

        if left in graph and left != (i, j):
            graph[(i, j)].append(left)
        if right in graph and right != (i, j):
            graph[(i, j)].append(right)
        if up in graph and up != (i, j):
            graph[(i, j)].append(up)
        if down in graph and down != (i, j):
            graph[(i, j)].append(down)

# Do BFS using stack
queue = [(0, 0)]
distances = { (0, 0): 1 }

while queue:
    node = queue.pop(0)
    if node == (n-1, m-1):
        print(distances[node])
        break
    for neighbor in graph[node]:
        if neighbor not in distances:
            distances[neighbor] = distances[node] + 1
            queue.append(neighbor)