# Algorithm: BFS
# Data structure: 2-dim list 
# 좌상단부터 탐색하며 0이 아닌 수를 만나면 현재 노드를 큐에 추가하고 BFS를 시작한다. 현재 노드를 방문함 리스트에 추가
# 이웃한 방향의 집들 중 같은 수의 집을 만나면 방문함 리스트에 추가하고 해당 좌표를 큐에 추가

n = int(input())
grid = []
visited = []
queue = []
answer = []
for i in range(n):
    tmp = list(map(int, input()))
    grid.append(tmp)

for y in range(n):
    for x in range(n):
        if grid[y][x] != 0:
            target = grid[y][x]
            queue.append((x, y))
            visited = [(x, y)]
            while queue:
                cur_x, cur_y = queue.pop(0)
                grid[cur_y][cur_x] = 0
                if cur_x - 1 >= 0 and grid[cur_y][cur_x - 1] == target and (cur_x - 1, cur_y) not in visited:  # left
                    queue.append((cur_x - 1, cur_y))
                    visited.append((cur_x - 1, cur_y))
                if cur_x + 1 < n and grid[cur_y][cur_x + 1] == target and (cur_x + 1, cur_y) not in visited:  # right
                    queue.append((cur_x + 1, cur_y))
                    visited.append((cur_x + 1, cur_y))
                if cur_y - 1 >= 0 and grid[cur_y - 1][cur_x] == target and (cur_x, cur_y - 1) not in visited:  # up
                    queue.append((cur_x, cur_y - 1))
                    visited.append((cur_x, cur_y - 1))
                if cur_y + 1 < n and grid[cur_y + 1][cur_x] == target and (cur_x, cur_y + 1) not in visited:  # down
                    queue.append((cur_x, cur_y + 1))
                    visited.append((cur_x, cur_y + 1))
            answer.append(len(visited))

print(len(answer))
for n in sorted(answer):
    print(n)
