'''from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    target = (sum1 + sum2)/2
    
    if (sum1+sum2)%2 != 0:
        return -1
    
    leng = 2*len(queue1)
    
    if sum1 == target:
        return 0
    
    cnt = 0
    
    while sum1 != target:
        
        if sum1 > target:
            n = queue1.popleft()
            queue2.append(n)
            sum1 -= n
            
        else:
            n = queue2.popleft()
            queue1.append(n)
            sum1 += n
            
        if not queue1 or not queue2:
            return -1
            
        cnt += 1
        
        if cnt > leng:
            return -1
        
    return cnt'''

from collections import deque

def solution(queue1, queue2):
    answer = -1
    max_moving = len(queue1) + len(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)

    for cnt in range(0, max_moving * 2):
        if sum1 == sum2:
            answer = cnt
            break
        elif sum1 > sum2:
            item = q1.popleft()
            sum1 -= item
            q2.append(item)
            sum2 += item
        else:
            item = q2.popleft()
            sum2 -= item
            q1.append(item)
            sum1 += item

    return answer