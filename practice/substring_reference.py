def subString(sString,memo={}):
# start 
    ans=0
    ls=len(sString)
    xa=[0] * ls
    xb=[0] * ls
    for i in range(len(sString)):
        if 'x' in sString:
            xa[i]=1
        if 'o' in sString:
            xb[i]=1
    
    hash = []

    curr_substr = ""
    for i in range(ls):
     
        # if we found occurrence of "x".
        if (xa[i]):
         
            # then go through all the positions
            # to find occurrence of "o".
            for j in range( i, ls):
             
                # if we do found "o" at index
                # j then add it to already
                # existed substring.
                if (not xb[j]):
                    curr_substr += sString[j]
 
                # if we found occurrence of "o".
                if (xb[j]):
                 
                    # now add string "o" to
                    # already existed substring.
                 
                    curr_substr += sString[j]
                     
                    # If current substring is not
                    # included already.
                    if curr_substr not in hash:
                        ans += 1
 
                    # put any non negative integer
                    # to make this string as already
                    # existed.
                    hash.append(curr_substr)
 
            # make substring null.
            curr_substr = ""
 
    # return answer.
    print(ans);
# end

if __name__ == "__main__":
    tcase=int(input())
    while tcase > 0:
        length=input()
        str= input()
        subString(str)
        tcase-=1