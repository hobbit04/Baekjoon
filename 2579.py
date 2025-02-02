# Data structure: List
# Algorithm: Dynamic programming
# 역순으로 계산. 

n = int(input())

stairs = []

for i in range(n):
    stairs.append(int(input()))

points = [0] * n
for i in range(n-1, 0, -1):
    if i == n-1:
        points[i] = stairs[i]
    elif i == n-2:
        points[i] = stairs[i] + stairs[i+1]
    else:
        points[i] = max(stairs[i] + points[i+2], stairs[i] + points[i+1])
    print(i, points[i])
print(points[0])