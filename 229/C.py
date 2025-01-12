N , W = map(int,input().split())

A = [None] * N
B = [None] * N

cheeseList = []

for i in range(N):
    A[i] , B[i] = map(int,input().split())
    cheeseList.append([A[i], B[i]])

cheeseList.sort(reverse = True)
sumGram = 0
sumDelicious = 0

for i in range(N):
    if cheeseList[i][1] <= W - sumGram:
        sumDelicious += cheeseList[i][0] * cheeseList[i][1]
        sumGram += cheeseList[i][1]
    else:
        sumDelicious += cheeseList[i][0] * (W - sumGram )
        break
    
print(sumDelicious)
