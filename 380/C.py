N , K = map(int,input().split())
S = input()

listStr = []

strAp = S[0]

for i in range(1 , N):

    if (i == (N - 1)):
        if strAp[-1] == S[i]:
            strAp += S[i]
            listStr.append(strAp)
        else:
            listStr.append(strAp)
            listStr.append(S[i])
    else:
        if strAp[-1] == S[i]:
            strAp += S[i]
        else:
            listStr.append(strAp)
            strAp = S[i]

count1 = 0
count = 0
for i in range(len(listStr)):
    count += 1
    if '1' in listStr[i]:
        count1 += 1
        if (count1 == K):
            break

listStr[count - 1] , listStr[count - 2] = listStr[count - 2] , listStr[count - 1]

print(''.join(listStr)) 