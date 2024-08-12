ans = ""

while True:
    stack = list(0 for i in range(100))
    len = 1
    sentence = input()
    if sentence == ".":
        break
    for c in sentence:
        if c == '.':
            ans += "yes\n"
            break
        elif c == '[':
            stack += "["
            len += 1
        elif c == '(':
            stack += "("
            len += 1
        elif c == ']':
            if stack[len-1] != '[':
                ans += "no\n"
                break
            else:
                len -= 1
        elif c == ')':
            if stack[len-1] != '(':
                ans += "no\n"
                break
            else:
                len -= 1

print(ans)
        