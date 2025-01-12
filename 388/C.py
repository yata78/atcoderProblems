N = int(input())
A = list(map(int,input().split()))

count = 0
tmp = 0

for i in range(1 , N):
    count += tmp
    for j in range(tmp, i):
        if (A[i] // 2 >= A[j]):
            tmp += 1
        else:
            break

print(count + tmp)