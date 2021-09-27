if __name__ == '__main__':
    n=int(input())
    names=[]
    scores=[]
    for i in range(n):
        name=input()
        names.append(name)
        score=float(input())
        scores.append(score)
        
    mark=sorted(scores,reverse=True)
    maxi=mark[-1]
    a=-2
    if(mark[a]==maxi):
        a=a-1
    marks=mark[a]
    answer=[]
    for i in range(n):
        if(marks==scores[i]):
            answer.append(names[i])
            
    answer=sorted(answer)
    for _ in answer:
        print(_)