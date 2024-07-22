def quick_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for num in arr[1:]:
        if num > pivot:
            right.append(num)
        elif num < pivot:
            left.append(num)
    answer = quick_sort(left)
    answer.append(pivot)
    answer += quick_sort(right)
    return answer


n = int(input())
num_arr = []
for i in range(n):
    num_arr.append(int(input()))

num_arr = quick_sort(num_arr)
for num in num_arr:
    print(num)

#
n = int(input())
num_arr = []
for i in range(n):
    input_num = int(input())
    if len(num_arr) == 0 or num_arr[0] < input_num:
        num_arr.append(input_num)
    else:
        tmp = [input_num]
        tmp += num_arr
        num_arr = tmp


for num in num_arr:
    print(num)

import sys
input = sys.stdin.readline

n=int(input())
li=[]

for i in range(n):
    li.append(int(input()))

for i in sorted(li):
    print(i)