x = [None] * 3
y = [None] * 3

for i in range(3):
    x[i],y[i] = map(int,input().split())

if x[0] == x[1]:
    x = x[2]
elif x[1] == x[2]:
    x = x[0]
else:
    x = x[1]

if y[0] == y[1]:
    y = y[2]
elif y[1] == y[2]:
    y = y[0]
else:
    y = y[1]

print(x , y)