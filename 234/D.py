import heapq

N , K = map(int,input().split())
P_list = list(map(int,input().split()))

que = []
heapq.heapify(que)

for i in range(K):
    heapq.heappush(que,P_list[i])

print(que[0])

for i in range(K , N):
    x = heapq.heappop(que)

    heapq.heappush(que,max(P_list[i], x))

    print(que[0])

