N = int(input())
S = input()

ans = True

for i in range(int((N + 1) / 2) - 1):
    if S[i] != '1':
        ans = False

if S[int((N + 1) /2) - 1] != '/':
    print(S[int((N + 1) / 2)])
    ans = False

for i in range(int((N + 1) / 2), N):
        if S[i] != '2':
            ans = False

if (ans):
    print("Yes")
else:
    print("No")