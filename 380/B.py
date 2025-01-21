S = input()

countList = []
count = 0
for i in range(1, len(S)):
    if S[i] == '-':
        count += 1
    else:
        countList.append(count)
        count = 0

print(*countList)