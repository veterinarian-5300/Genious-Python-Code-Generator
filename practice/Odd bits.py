t=int(input())

def decimalToBinary(n):
    return bin(n).replace("0b","")

for i in range(t):
    n=int(input())
    k=int(decimalToBinary(n))
    if(k>=0):
        print(k)

        


