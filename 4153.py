ans = ""
while True:
    s = input()
    if s == "0 0 0":
        break
    num_list = list(map(int, s.split(" ")))
    num_list.sort()
    if num_list[0] ** 2 + num_list[1] ** 2 == num_list[2] ** 2:
        ans += "right\n"
    else:
        ans += "wrong\n"
print(ans)
