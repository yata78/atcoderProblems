H , W = map(int,input().split())

def search(x , y):
    if g[x][y] == '#': return
    if g[x][y] = return
    g[x][y] = True

    search(x + 1, y)
    search(x - 1, y)
    search(x , y + 1)
    search(x , y - 1)