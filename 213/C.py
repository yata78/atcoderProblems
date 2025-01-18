H,W,N = map(int,input().split())

answer = []
A_set = set()
B_set = set()

for i in range(N):
    A , B = map(int,input().split())
    answer.append([A,B])
    A_set.add(A)
    B_set.add(B)

A_list = list(A_set)
B_list = list(B_set)

A_list.sort()
B_list.sort()

A_dict = {}
B_dict = {}

for i in range(len(A_list)):
    A_dict[A_list[i]] = i + 1

for i in range(len(B_list)):
    B_dict[B_list[i]] = i + 1

for a, b in answer:
    answer_A = A_dict[a]
    answer_B = B_dict[b]
    print(answer_A,answer_B)
