N = int(input())

lList = []
rList = []

count = 0

for i in range(N):
    t,l,r = map(int,input().split())
    if t == 1:
        lList.append(l)
        rList.append(r)
    elif t == 2:
        lList.append(l)
        rList.append(r - 0.1)
    elif t == 3:
        lList.append(l + 0.1)
        rList.append(r)
    elif t == 4:
        lList.append(l + 0.1)
        rList.append(r - 0.1)

for i in range(N):
    for j in range(i + 1, N):
        if lList[i] <= lList[j] <= rList[i]:
            count += 1
        elif lList[i] <= rList[j] <= rList[i]:
            count += 1
        elif lList[j] <= lList[i] <= rList[i]:
            count += 1
        elif lList[j] <= rList[i] <= rList[j]:
            count += 1

print(count)

