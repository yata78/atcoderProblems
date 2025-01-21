N , K = map(int,input().split())
S = input()

listStr = []

strAp = S[0]

for i in range(1 , N):

    if (i == N):
        if strAp[-1] == S[i]:
            strAp += S[i]
            listStr.append[strAp]
        else:
            listStr.append[strAp]
            listStr.append[S[i]]
    else:
        if strAp[-1] == S[i]:
            strAp += S[i]
        else:
            listStr.append(strAp)
            strAp = S[i]

print(*listStr) 