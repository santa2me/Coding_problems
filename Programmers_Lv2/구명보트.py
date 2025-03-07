def solution(people, limit):
    answer = 0
    p_sorted = sorted(people, reverse=True)
    
    for p in p_sorted:
        if p + p_sorted[-1] <= limit:
            answer += 1
            p_sorted.pop()
        else:
            answer += 1
solution([70, 80, 50], 100)