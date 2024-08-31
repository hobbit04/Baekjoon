def z(start_num, n, r, c):
    if n == 1:
        return start_num + 2 * r + c

    if 0 <= r < 2 ** (n-1):
        x = 0
    else:
        x = 1
    if 0 <= c < 2 ** (n - 1):
        y = 0
    else:
        y = 1
    diff = 4 ** (n-1)
    new_start_num = start_num + 2 * x * diff + y * diff
    new_r = r - 2 ** (n-1) * x
    new_c = c - 2 ** (n-1) * y
    return z(new_start_num, n-1, new_r, new_c)


N, R, C = map(int, input().split())
print(z(0, N, R, C))
