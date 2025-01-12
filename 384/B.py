N , R = map(int,input().split())

nowScore = R

for i in range(N):
    D , A = map(int,input().split())
    if D == 1:
        if nowScore >= 1600 and nowScore <= 2799:
            nowScore += A
    if D == 2:
        if nowScore >= 1200 and nowScore <= 2399:
            nowScore += A
    
print(nowScore)