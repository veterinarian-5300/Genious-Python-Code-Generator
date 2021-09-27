import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = input()
c = input()

if(c=='S'):
    print(w,' ',w[::-1],' ', w,' ',w[::-1],' ', w )
elif(c=='D'):
    print(w,'\n',w[::-1],'\n', w,'\n',w[::-1],'\n', w )
