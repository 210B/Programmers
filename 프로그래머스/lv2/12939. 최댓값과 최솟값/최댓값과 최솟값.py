def solution(s):
    ls = list(map(int,s.split()))
    ls.sort()
    answer = str(ls[0]) + ' ' + str(ls[-1])
    return answer