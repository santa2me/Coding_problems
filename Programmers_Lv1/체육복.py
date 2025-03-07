def solution(n, lost, reserve):
    commons = set(lost) & set(reserve)
    answer = n - len(lost) + len(commons)
    
    lost = [x for x in lost if x not in commons]
    reserve = [x for x in reserve if x not in commons]
    
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