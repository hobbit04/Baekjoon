def div_sum(num):
    ans = num
    num = str(num)
    for i in num:
        ans += int(i)
    return ans

n = int(input())
for i in range(n):
    if div_sum(i) == n:
        print(i)
        quit()
print(0)