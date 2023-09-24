def solution(input_string):
    i = 1
    while i<len(input_string):
        if input_string[i]==input_string[i-1]:
            input_string= input_string[:i] + input_string[i + 1:]
        else:
            i+=1

    count = {}
    for s in input_string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    answer = []
    for cnt in count:
        if count[cnt] >1:
            answer.append(cnt)
    answer.sort()
    return ''.join(answer) if answer else "N"
