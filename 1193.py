# 분자: 1, 12, 321, 1234, 54321, 123456, ...
# 분모: 1, 21, 123, 4321, 12345, 654321, ...
a = [1]
b = [1]
cnt = 1
n = int(input())

for i in range(n):
    if a[i] == cnt:
        a.append(cnt)
        cnt += 1
     