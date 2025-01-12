import itertools

S, K = map(str,input().split())

K = int(K)
dic= set()

for p in itertools.permutations(range(len(S))):
    Stmp = ""

    for i in p:
        Stmp+=S[i]
    
    dic.add(Stmp)

Slist = list(dic)
Slist.sort()

print(Slist[K - 1])