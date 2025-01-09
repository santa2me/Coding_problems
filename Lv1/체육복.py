def solution(n, lost, reserve):
    answer = n - len(lost)
    count = 0
    for l in lost:
        if l in reserve:
            count += 1
            reserve.remove(l)
            lost.remove(l)
            
    answer += count
    
    for l in sorted(lost):
        if l-1 in sorted(reserve):
            reserve.remove(l-1)
            answer += 1
        elif l+1 in sorted(reserve):
            reserve.remove(l+1)
            answer += 1
        else:
            continue

    print(answer)      
    return answer

solution(5, [5, 3], [4, 2])