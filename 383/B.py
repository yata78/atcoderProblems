H , W , D = map(int,input().split())
S = (input()) for i in range(H)

ans = 0

for i1 in range(H):
    for j1 in range(W):
        if (S[i1][j1] == "#"):
            continue
        for i2 in range(i1, H):
            for j2 in range(j1, W):
                if (S[i2][j2] == "#" or (i1 == i2 and j1 == j2)):
                    continue
                tmp = 0
                for i in range(H):
                    for j in range(W):
                        if (S[i][j] == '.' and ((abs(i - i1) + abs(j - j1) <= D) or (abs(i - i2) + abs(j - j2) <= D))):
                            tmp = tmp + 1
                ans = max(ans, tmp)

print(ans)
