def canSum(target, numbers ):
    if target in numbers:
        return True
    if target ==0:
        return True
    if target <0:
        return False
    for n in numbers:
        rem=target-n;
        if canSum(rem,numbers):
            return True
        
    return False


if __name__ == '__main__':
    print(canSum(10,[2,4]))
    print(canSum(3,[1,2]))
    print(canSum(7, [2, 3])) # True
    print(canSum(7, [5, 3, 4, 7])) # True
    print(canSum(7, [2, 4])) # False
    print(canSum(8, [2, 3, 5])) # True
