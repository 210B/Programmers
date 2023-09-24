from math import sqrt

def solution(brown, yellow):
    a = sqrt(brown*brown/4-4*yellow-2*brown+4)
    return [brown/4+a/2+1,brown/4-a/2+1]