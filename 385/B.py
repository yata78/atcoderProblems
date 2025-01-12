H,W,X,Y = map(int,input().split())

S = [list(input()) for i in range(H)]

T = input()

X -=1
Y -=1

homeCount = 0

for i in range(len(T)):
    if T[i] == "L" and S[X][Y - 1] != "#":
        Y -= 1 
    if T[i] == "R" and S[X][Y + 1] != "#":
        Y += 1
    if T[i] == "U" and S[X - 1][Y] != "#":
        X -= 1
    if T[i] == "D" and S[X + 1][Y] != "#":
        X += 1
    if S[X][Y] == "@":
        homeCount += 1
        S[X][Y] = "."

print(X + 1,Y + 1,homeCount)