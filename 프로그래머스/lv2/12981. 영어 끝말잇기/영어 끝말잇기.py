def solution(n, words):
    i = 1
    cnt = 0
    while i<len(words):
        for j in range(0,i-1):
            if words[i] == words[j]:
                cnt = i
                return [i%n+1,i//n+1]
        if words[i][0] != words[i-1][-1]:
            cnt = i
            return [i%n+1,i//n+1]
        else:
            i+=1
    if i == len(words):
        return [0,0]

'''                
def solution(n, words):

    for i in range(1,len(words)):
        if words[i] in words[0:i]:
            return [i%n+1, i//n+1]
        elif words[i][0] != words[i-1][-1]:
            return [i%n+1, i//n+1]
            
    return [0,0]'''