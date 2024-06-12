def find666(num):
    d = 10
    cnt = 0
    l = len(str(num))
    i = 0
    while i < l:
 
        if "666" in str(num):
            cnt += 1
        else:
            cnt = 0
        
        if cnt == 3:
            return True
        d *= 10
        i += 1
    return False

n = int(input())
i = 0
num = 666
while True:
    
    if find666(num):
        i += 1
    if i == n:
        print(num)
        break
    num += 1

