def solution(s):
    sum = 0
    z = 0
    while s != '0b1':
        s = s.replace('0b','')
        a = s.count('0')
        s = bin(s.count('1'))
        sum += 1
        z += a
    return [sum, z]

'''def solution(s):
    answer = [0,0]
    
    while(s != '1'):
        cnt = s.count('0')
        n = len(s)-cnt
        s = str(bin(n))[2:]
        answer[0] += 1
        answer[1] += cnt
        
    return answer'''
    
    
    
    
    
    
    