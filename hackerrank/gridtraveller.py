def gridtraveller(x,y,memo):
    if x==0 or y==0: return 0
    if x==1 and y==1: return 1
    if (memo[x][y]!=0): return memo[x][y]
    memo[x][y]=(memo[x-1][y]+memo[x][y-1]);
    return memo[x][y];

if __name__ == '__main__':
    x=int(input())
    y=int(input())
    arr=[]
    for i in range(y+1):
        col = []
        for j in range(x+1):
            col.append(0)
        arr.append(col)

    print(gridtraveller(x,y,arr))
