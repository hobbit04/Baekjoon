n = int(input())
l = list([64, 32, 16, 8, 4, 2, 1])

def near_square(n):
    for i in l:
        if n < i:
            continue
        else:
            return i
        
def ans(n, cnt):
    if n == near_square(n):
        return cnt
    else:
        return ans(n - near_square(n), cnt + 1)
print(ans(n, 1))