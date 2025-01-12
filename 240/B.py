N = int(input())

a = list(map(int,input().split()))

ans = set()

for i in range(N):
    ans.add(a[i])

print(len(ans))