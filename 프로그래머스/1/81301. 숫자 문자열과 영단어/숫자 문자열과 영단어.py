def solution(s):
    number = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    st = ''
    answer = ''
    for i in range(len(s)):
        if s[i].isnumeric():
            answer += s[i]
        else:
            st += s[i]
            if st in number:
                answer += str(number[st])
                st = ''
                
    return int(answer)