S = input()

S = '?' + S

#chokudaiの長さ + 1
H = 9

W = len(S)

S_List = [0] * 9 for i in range(len(S) + 1)

mod = 10**9 + 7

for i in range( N + 1):
    S_List[i][0] = 1

for i in range( N + 1):
    for k in range( 1, 9):
        if S[i] == T[k]:
            dp[i][k] = dp[i - 1][k] + dp[i][k - 1]
        else:
            dp[i][k] = dp[i - 1][k]
    dp[i][k] %= mod

print(dp[N][8])
