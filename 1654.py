
def v1():
    k, n = map(int, input().split(" "))
    lan = []
    for i in range(k):
        lan.append(int(input()))

    ans = max(lan)
    pre = ans
    while True:
        num = 0
        for i in range(k):
            num += lan[i] // ans
        if num == n:
            print(ans)
            break
        elif num > n:
            if pre == ans:
                print(ans)
                break
            pre = ans
            ans = (max(lan) + ans) // 2
        else:
            pre = ans
            ans //= 2

def v2():
    k, n = map(int, input().split(" "))
    lan = []
    for i in range(k):
        lan.append(int(input()))

    ans = max(lan)
    while True:
        num = 0
        for i in range(k):
            num += lan[i] // ans
        if num >= n:
            print(ans)
            break
        
        else:
            ans-=1



v1()

v2()