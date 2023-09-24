def solution(n):
    count_one_n = bin(n).count('1')
    
    while True:
        n += 1
        count_one_next = bin(n).count('1')
        
        if count_one_next == count_one_n:
            return n

''' 일부 테케 시간초과
def solution(n):
    p = str(bin(n)[2:])
    index = p.find('01')
    s = list(bin(n)[2:])
    
    if index == -1:
        index = 0
        s = ['0'] + s
    
    s[index] = '1'
    s[index+1] = '0'
    num1 = ''.join(s[:index+1])
    num2 = ''.join(s[index+1:])
    n = num2.count('1')
    num3 = (len(num2)-n)*'0'+n*'1'
    
    return int('0b'+num1+num3, 2)'''