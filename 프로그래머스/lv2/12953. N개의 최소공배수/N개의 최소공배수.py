import math

def solution(arr):
    lcm = arr[0]
    
    for num in arr[1:]:
        lcm = (lcm * num) // math.gcd(lcm, num)
    
    return lcm

'''
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return a * b // get_gcd(a, b)

def solution(arr):
    lcm = arr[0]
    for num in arr[1:]:
        lcm = get_lcm(lcm, num)
    return lcm'''