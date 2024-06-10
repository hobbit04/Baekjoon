n = int(input())

words = list()

# 중복제거 및 리스트 생성
for i in range(n):
    a = input()
    if a in words:
        continue
    words.append(a)

l = len(words)
# 글자수 정렬
lengths = list()
ans = list()

for i in range(l):
    if len(words[i]) in lengths:
        continue
    lengths.append(len(words[i]))  # 단어의 길이들을 저장한다. 
lengths.sort()
for i in lengths:
    for j in range(l):
        if len(words[j]) == i:
            ans.append(words[j])

# 사전식 정렬 - 글자수가 같은 단어들끼리 따로 리스트를 만들고 각각 정렬후 이어붙인다?
new_ans = list()

cnt = 0
for i in lengths:
    temp = list()

    for j in range(l):
        if len(ans[j]) == i:
            temp.append(ans[j])
    temp.sort()
    for k in range(len(temp)):
        print(temp[k])
