import time
def gridtraveller(x,y,memo={}):
    key=str(x)+','+str(y)
    if key in memo:
        return memo[key]
    if x==0 or y==0:
        return 0
    if x==1 and y==1:
        return 1
    
    memo[key]=gridtraveller(x-1, y, memo)+gridtraveller(x, y-1, memo)
    return memo[key]

if __name__ == '__main__':
    start_time = time.time()
    x=int(input())
    y=int(input())
    print(gridtraveller(x,y))
    end_time = time.time()
    print(end_time-start_time)
    