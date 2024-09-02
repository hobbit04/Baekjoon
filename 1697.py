from collections import deque


max_num = 100000
visited = [0] * (max_num + 1)


def bfs(num, target):
    q = deque()
    q.append(num)
    while q:
        x = q.popleft()
        if x == target:
            print(visited[x])
            return
        for pos in (x-1, x+1, 2*x):
            if 0 <= pos <= max_num and not visited[pos]:
                visited[pos] = visited[x] + 1
                q.append(pos)


n, k = map(int, input().split())
bfs(n, k)
