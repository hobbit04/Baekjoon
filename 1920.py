def b_srch(li, tar):
    start = 0
    end = len(li) - 1

    while start <= end:
        mid = (start + end) // 2
        if li[mid] == tar:
            return 1
        elif li[mid] > tar:
            end = mid - 1
        elif li[mid] < tar:
            start = mid + 1
    return 0

n = int(input())
a = list(map(int, input().split(" ")))
a.sort()
m = int(input())
target = list(map(int, input().split(" ")))

for t in target:
    print(b_srch(a, t))
