def solution(n):
    return bin(n).count('1')

'''def solution(n):
    ans = 1
    
    while(n>2):
        if n%2 == 0:
            n = n//2
        else:
            n = n-1
            ans += 1

    return ans'''