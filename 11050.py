def factorial(n):
    i = 1
    cnt = 1
    while cnt < n:
        i *= cnt + 1
        cnt += 1
    return i
n, k = map(int, input().split(" "))
ans = factorial(n) // (factorial(k) * factorial(n - k))
print(ans)
