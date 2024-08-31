from collections import deque
import math


def bfs(num, target):
    queue = deque()
    queue.append([(num, 0)])

    while queue:
        i, sec = queue.popleft()
        if i == target:
            return sec
        queue.append([(i-1, sec+1)])
        queue.append([(i+1, sec+1)])
        queue.append([(2*i, sec+1)])
        sec += 1


n, k = map(int, input().split())
print(bfs(n, k))
