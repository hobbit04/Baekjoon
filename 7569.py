import numpy as np

m, n, h = map(int, input().split())

box = np.zeros((h, n, m), dtype=int)
for i in range(h):
    for j in range(n):
        s = input().split()
        for k in range(m):
            box[i, j, k] = s[k]

print(box)
