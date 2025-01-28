S = input()

answre = True

if (len(S) % 2 != 0):
    answre = False

for i in range(len(S)):
    if i % 2 == 1:
        if S[i] != S[i - 1]:
            answre = False

from collections import defaultdict

d = defaultdict(int)

for i in range(len(S)):
    d[S[i]] += 1
    if d[S[i]] > 2:
        answre = False
        break

if (answre):
    print("Yes")
else:
    print("No")