def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

n = int(input())
ans = list()
for i in range(n):
    a, b = map(int, input().split())
    ans.append(int(factorial(b) / (factorial(b-a) * factorial(a))))
    

for i in range(n):
    print(ans[i])



#시간제한 0.5초