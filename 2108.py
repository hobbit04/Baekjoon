import statistics


def find_mean(n, arr):
    s = 0
    for i in arr:
        s += i
    return s / n


def find_mid(n, arr):
    arr.sort()
    return arr[n // 2]


def find_mode(arr):
    arr.sort()
    return statistics.mode(arr)


def find_range(arr):
    arr.sort()
    return arr[-1] - arr[0]

n = int(input())
num_arr = []
for i in range(n):
    num_arr.append(int(input()))

print(find_mean(n, num_arr))
print(find_mid(n, num_arr))
print(find_mode(num_arr))
print(find_range(num_arr))

