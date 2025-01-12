def nibun(x , A):
    left = 0
    right = N - 1

    while 1 < right - left:
        middle = (left + right) // 2

        if x > A[middle]:
            left = middle
        else:
            right = (middle + right) // 2
    
    return right

N , Q = map(int,input().split())

A = list(map(int,input().split()))
A.sort()