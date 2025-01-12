N , D = map(int,input().split())

T = [None] * N
L = [None] * N

for i in range(N):
    T[i], L[i] = map(int,input().split())

for i in range(1 , D + 1):
    maxLength = 0
    for j in range(N):
        maxLength = max(maxLength, T[j] * (L[j] + i))
    print(maxLength)
