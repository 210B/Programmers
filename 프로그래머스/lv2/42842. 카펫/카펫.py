from math import sqrt

def solution(brown, yellow):
    a = sqrt(brown*brown/4-4*yellow-2*brown+4)
    return [brown/4+a/2+1,brown/4-a/2+1]

'''
def solution(brown, yellow):
    total = brown + yellow
    for height in range(3, int(total**0.5) + 1):
        if total % height == 0:
            width = total // height
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
'''
