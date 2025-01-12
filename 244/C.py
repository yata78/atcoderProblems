N = int(input())

Used = [False]*(2 * N + 2)

print(1)

Used[1] = True

for i in range(N + 1):
    x = int(input())
    Used[x] = True

    if x == 0:
        exit()

    for k in range(1, 2 * N + 2):
        if Used[k] == False:
            print(k)
            Used[k] = True
            break