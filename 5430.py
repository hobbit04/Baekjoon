from collections import deque

t = int(input())
ans = ""  # 정답 문자열
for i in range(t):
    p = input()  # 수행할 함수들의 문자열
    n = int(input())  # 수열의 길이
    arr = input()  # 대상 수열
    arr = arr[1:-1]
    arr = arr.split(',')
    if n == 0:
        dq = deque()
    else:
        dq = deque(arr)

    is_odd = False  # 홀수번 뒤집을지 짝수번 뒤집을지가 중요
    is_err = False

    for f in p:
        if f == "R":
            is_odd = not is_odd
        elif f == 'D' and len(dq) == 0:
            is_err = True
            break
        else:
            n -= 1
            if is_odd:
                dq.pop()
            else:
                dq.popleft()

    if is_err:
        ans += "error\n"
    else:
        if is_odd:
            dq.reverse()  # 뒤집은 상태로 출력
        ans += f"[{','.join(dq)}]"
        ans += "\n"

print(ans)
