def howSum(target, number, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return 0

    for n in number:
        rem=target-n
        result=howSum(rem,number,memo)
        if result != 0:
            result = result.append(n)
            memo[target]=result
            return memo[target]

    memo[target]=0    
    return 0

if __name__ == '__main__':
    print(howSum(10,[2,4]))
    print(howSum(3,[1,2]))
    print(howSum(7, [2, 3])) # True
    print(howSum(7, [5, 3, 4, 7])) # True
    print(howSum(7, [2, 4])) # False
    print(howSum(8, [2, 3, 5])) # True


