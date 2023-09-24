def solution(n):
    s = [0]*(n+1)
    s[1] = 1
    for i in range(2,n+1):
        s[i] = (s[i-1]+s[i-2])%1234567
        
    return s[n]
