n = int(input())

for _ in range(n):
    r, s = input().split()
    r = int(r)
    for c in s:
        print(c * r, end='')
    print()
