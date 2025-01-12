import math

S = input()

count_operations = len(S)
i = 0

while i < (len(S) - 1):
    if S[i] == "0" and S[i + 1] == "0":
        count_operations -= 1
        i += 1
    i += 1

print(count_operations)