from collections import deque

N = int(input())
S = input()

que = deque()

que.append(N)

for i in range(N - 1, -1, -1):
    if S[i] == 'R':
        que.appendleft(i)
    else:
        que.append(i)
    
print(*que)