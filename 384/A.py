N , c1, c2 = map(str,input().split())
S = input()

answer = ""

for i in range(int(N)):
    if S[i] == c1:
        answer += c1
    else:
        answer += c2

print(answer)