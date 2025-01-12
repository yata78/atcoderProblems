N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

time = [10 ** 15] * N

for i in range(N):

    next = (i + 1) % N

    time[next] = min(T[next], time[i] + S[i])

for i in range(N):
    next=(i+1)%N

    time[next] = min(T[next], time[i] + S[i])

for i in range(N):
    print(time[i])