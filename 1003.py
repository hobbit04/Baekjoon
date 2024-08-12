def fibonacci(n):
    if n == -1:
        return 1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    if n-1 in memory:
        a = memory[n-1]
    else:
        a = fibonacci(n-1)
    if n-2 in memory:
        b = memory[n-2]
    else:
        b = fibonacci(n-2)

    memory[n] = a + b
    return a + b


t = int(input())
memory = {}
for i in range(t):
    num = int(input())
    a = fibonacci(num - 1)
    memory[num-1] = a

    b = fibonacci(num)
    memory[num] = b
    print(a, b)
    print(memory)


#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
