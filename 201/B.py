N = int(input())
S = [None] * (N + 1)
T = [None] * (N + 1)

list1 = []

for i in range(N):
    S[i], T[i] = map(str,input().split())
    list1.append([int(T[i]), S[i]])

list1.sort(reverse=True)

print(list1[1][1])

