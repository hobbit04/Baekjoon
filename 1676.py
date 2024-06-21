def factorial(n):
    ans = 1
    while(n > 0):
        ans *= n
        n -= 1
    return ans

n = str(factorial(int(input())))
length = len(n)
cnt_zero = 0
i = length - 1
while i >= 0:
    if n[i] == '0':
        cnt_zero += 1
    else:
        print(cnt_zero)
        break
    i -= 1