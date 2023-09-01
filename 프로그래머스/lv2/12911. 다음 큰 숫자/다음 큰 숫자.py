def solution(n):
    b = bin(n).replace('0b', '0')
    m = b.rfind('01')
    k = b[m+2:].count('1')
    b = b[:m] + '10' + '0'*(len(b)-m-2-k) + '1'*k
    answer = int(b, 2)
    return answer