N = int(input())

ans = ""

tmp = N

while(tmp > 0):
    if (tmp % 2 == 0):
        ans = "B" + ans
        tmp //= 2
    else:
        ans = "A" + ans
        tmp -= 1

print(ans)
