n = int(input())
arr = []
stack = [1]
ans = "+\n"

for i in range(n):
    arr.append(int(input()))

i = 2  # for stack
for target in arr:
    while stack == [] or stack[-1] < target:
        stack.append(i)
        i += 1
        ans += "+\n"
    
    if stack == []:
        stack.append(i)
        i += 1
        ans += "+\n"
    elif stack[-1] < target:
        dif = target - stack[-1]
        i += dif
        ans += "+\n" * dif
        

    if stack[-1] == target:
        del stack[-1]
        ans += "-\n"
    elif stack[-1] > target:
        print("NO")
        quit()

ans = ans[:-1]
print(ans)