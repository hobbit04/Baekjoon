def dfs(a, b):
    visited[b][a] = 1


t = int(input())

for _ in range(t):
    ans = 0
    m, n, k = map(int, input().split())
    # todo: make (n x m) list

    farm = [[0 for i in range(m)] for j in range(n)]

    # todo: get coordination of '1'
    for i in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    # todo: while bfs, if 1 is found and not marked as visited, do dfs and add all the coord in to visited list.

    visited = [[0 for i in range(m)] for j in range(n)]  # will be marked as 1 if it is visited
    for y in range(n):
        for x in range(m):
            if farm[y][x] == 1 and visited[y][x] == 0:
                dfs(x, y)
                ans += 1

    # the number of occur of dfs is the answer
    print(ans)
