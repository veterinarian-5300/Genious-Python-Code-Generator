def call():
    count = 0
    x,y,a,b=[int(x) for x in input().split()]
    if (x>y):
        if(a>b):
            x=x-a
            y=y-b
            
        else:
            y-=a
            x-=b
    else:
        if(b>a):
            x=x-a
            y=y-b
            count+=1
        else:
            y-=a
            x-=b
    print(x,y,a,b, sep="\n")

if __name__ == '__main__':
    n=int(input())
    for _ in range(n):
        call();   

