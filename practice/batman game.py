import sys
import math
w, h = [int(i) for i in input().split()]
w=w-1
h=h-1
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
x=x0
y=y0
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if (bomb_dir =='U' or bomb_dir == 'UR' or bomb_dir == 'UL'):
        if (bomb_dir == 'UR'):
            x=x + math.ceil((w-x)/2)
            print(x, '1 ')
        elif (bomb_dir == 'UL'):
            x=math.ceil((x-0)/2)
            print(x, '2 ')
        y=math.ceil((y-0)/2)
        print(y, '3 ')
    elif (bomb_dir =='D' or bomb_dir == 'DR' or bomb_dir == 'DL'):
        if (bomb_dir == 'DR'):
            x=x + math.ceil((w-x)/2)
            print(x, '4 ')
        if (bomb_dir == 'DL'):
            x=math.ceil((x-0)/2)
            print(x, '5 ')
        y=y + math.ceil((h-y)/2)
        print(y, '6 ')
    elif (bomb_dir == 'R'):
        x=x + math.ceil((w-x)/2)
        print(x, '7 ')
    elif (bomb_dir == 'L'):
        x=math.ceil((x-0)/2)
        print(x, '8 ')

    print(x,y,'0')
