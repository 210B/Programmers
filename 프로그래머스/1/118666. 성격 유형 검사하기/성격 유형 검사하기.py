def solution(survey, choices):
    # R, T, F, C, M, J, A, N dictionary
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    # choices -4 regularization
    for i in range(len(choices)):
        score = choices[i] - 4
        if score < 0:
            scores[survey[i][0]] -= score
        else:
            scores[survey[i][1]] += score
    
    # get max among (R,T), (F,C), (M,J), (A,N)
    answer = ''
    key_list = list(scores.keys())
    value_list = list(scores.values())
    for i in range(0,8,2):
        if value_list[i] >= value_list[i+1]:
            answer += key_list[i]
        else:
            answer += key_list[i+1]
    
    return answer