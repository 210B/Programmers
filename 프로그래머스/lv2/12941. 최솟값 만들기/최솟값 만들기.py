def solution(A,B):
    sum = 0
    A.sort()
    B.sort()
    
    for i in range(len(A)):
        sum +=A[i]*B[len(A)-i-1]
    
    return sum