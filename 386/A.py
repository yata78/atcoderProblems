countList = list(map(int,input().split()))

A_COUNT = countList.count(countList[0])
B_COUNT = countList.count(countList[1])
C_COUNT = countList.count(countList[2])

if A_COUNT == 1 and B_COUNT == 3:
    print("Yes")
elif A_COUNT == 3 and B_COUNT == 1:
    print("Yes")
elif A_COUNT == 2 and B_COUNT == 2 and countList[0] != countList[1]:
    print("Yes")
elif A_COUNT == 3 and B_COUNT == 3:
    print("Yes")
elif A_COUNT == 2 and B_COUNT == 2 and C_COUNT == 2:
    print("Yes")
else:
    print("No")