n=int(input("enter your secret number  "))
l=0
m=n
u=2*n-1
for i in range(n):
    a=n
    for j in range(i):
        print(a,end=' ')
        a=a-1
    for k in range(i,u-i):
        print(a,end=' ')
    for l in range(u-i,u):
        a+=1
        print(a,end=' ')
    print()
    
for i in range(n,u):
    a=n
    m=m-1
    for j in range(m):
        print(a,end=' ')
        a=a-1
    for k in range(m,u-m):
        print(a+1,end=' ')
    for l in range(u-m,u):
        a+=1
        print(a,end=' ')

    print()
