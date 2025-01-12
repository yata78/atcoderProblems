N = int(input())
A = list(map(int,input().split()))
X = int(input())

sumValue = 0

for i in range(N):
    sumValue += A[i]

inList = X // sumValue
siguma = X - sumValue * inList

count = 0

for i in range(N):
    if siguma - A[i] >= 0:
        siguma -= A[i]
        count += 1
    else:
        count += 1
        break

print(inList * N + count)
