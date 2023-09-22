'''def solution(s):
    stack = []
    answer = ''
    for i in range(len(s)):
        if s[i] =='(':
            stack.append(1)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False'''
    

def solution(s):
    sum = 0
    for i in range(len(s)):
        if s[i] == '(':
            sum += 1
        else:
            if sum == 0:
                return False
            else:
                sum -= 1
    if sum == 0:
        return True
    else:
        return False
            