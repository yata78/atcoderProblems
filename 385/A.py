sort_list = sorted(list(map(int, input().split())))

if (sort_list[0] == sort_list[1] and sort_list[1] == sort_list[2]):
    print("Yes")
elif (sort_list[0] + sort_list[1] == sort_list[2]):
    print("Yes")
else:
    print("No")