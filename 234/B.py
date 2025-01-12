import math

N = int(input())

x = [None] * (N + 1)
y = [None] * (N + 1)

for i in range(N):
    x[i], y[i] = map(int,input().split())

maxLength = 0

for i in range(N):
    for j in range(i + 1, N):
        maxLength = max(maxLength , math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j])** 2))

print(maxLength)