def solution(k, tangerine):
    size_counts = {}
    
    for size in tangerine:
        if size in size_counts:
            size_counts[size] += 1
        else:
            size_counts[size] = 1

    sorted_counts = sorted(size_counts.values(), reverse=True)
    
    box = []
    kinds = 1
    for count in sorted_counts:
        if k > count:
            box.append(count)
            kinds += 1
            k -= count
        else:
            box.append(k)
            break
    
    return kinds
