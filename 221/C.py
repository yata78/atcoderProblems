N = input()

ans = 0

for bitnum in range(1 << len(N)):
    A=[]
    B=[]

    for shift in range(len(N)):

        if bitnum>> shift & 1 == 0:
            A.append[N[shift]]
        else:
            B.append[N[shift]]
    
    if A == [] or B == []:
        continue
    
    A.sort(reverse=True)
    B.sort(reverse=True)

    A_join = "".join(A)
    B_join = "".join(B)

    tmp_ans = int(A_join) * int(B_join)

    ans = max(ans,tmp_ans)

print(ans)