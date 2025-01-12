from collections import defaultdict

N = int(input())

A = list(map(int,input().split()))

allCount = N * (N - 1) // 2

my_dict = defaultdict(int)

for i in range(N):
    my_dict[A[i]] += 1

for x in my_dict.values():
    if x > 1:
        allCount -= (x * (x - 1) // 2)

print(allCount)