def solution(s):
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
                stack.append(s[i])
        elif stack[-1] == s[i]:
                stack.pop()
        else:
            stack.append(s[i])
    
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer

'''일부 테케 시간 초과
def solution(s):
    i = 0
    s = list(s)

    while i + 1 < len(s):
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            i = 0
        else:
            i += 1

    if not s: 
        return 1
    else:
        return 0'''