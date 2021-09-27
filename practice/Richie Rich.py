T=int(input())
k=[]
for i in range(T):
    a,b,x=[int(x) for x in input().split()]
    k.append(int((b-a)/x))

print(*k, sep='\n')
