# Algorithm: recursion
# Data structure: 2-dim list
#
n = int(input())

paper = []

white_count = 0
blue_count = 0
for i in range(n):
    paper.append(list(map(int, input().split())))

# print(paper)
def square(start_x, start_y, end_x, end_y, target):
    # 종료조건: 모든 칸이 0이거나 1일 때
    # 반환 형식: target(0 또는 1)의 수
    # 아니라면 4칸으로 나누어서 재귀호출
    length = end_x - start_x + 1  # length of a one side
    start_with = paper[start_x][start_y]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if paper[x][y] != start_with:
                return square(start_x, start_y, start_x + length // 2 - 1, start_y + length // 2 - 1, target) + \
                       square(start_x + length // 2, start_y, end_x, start_y + length // 2 - 1, target) + \
                       square(start_x, start_y + length // 2, start_x + length // 2 - 1, end_y, target) + \
                       square(start_x + length // 2, start_y + length // 2, end_x, end_y, target)
    if start_with == target:
        return 1
    else:
        return 0
print(square(0, 0, n - 1, n - 1, 0))
print(square(0, 0, n - 1, n - 1, 1))
