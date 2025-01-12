N , D = map(int,input().split())
S = list(map(str,input()))

for i in range(D):
    i = N - 1
    while (True):
        if S[i] == '@':
            S[i] = '.'
            break
        else:
            i -= 1

ans = ""
for i in range(len(S)):
    ans += S[i]

print(ans)