# Data structure: List
# Algorithm: Dynamic programming(Devide and Conquer)
# 1: 1
# 2: 1+2
# 3: max(1+3, 2+3)
# 4: max(1+2+4, 1+3+4)
# n: max(n + n-2, n + n-1 + n-3)

n = int(input())

stairs = []

for i in range(n):
    stairs.append(int(input()))

score = [0] * n

for i in range(n):
    if i == 0:
        score[i] = stairs[i]
    elif i == 1:
        score[i] = stairs[i-1] + stairs[i]
    elif i == 2:
        score[i] = max(stairs[i-2] + stairs[i], stairs[i-1] + stairs[i])
    else:
        score[i] = max(score[i-2] + stairs[i], score[i-3] + stairs[i-1] + stairs[i])
print(score[-1])
