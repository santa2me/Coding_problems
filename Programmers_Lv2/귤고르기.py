from collections import Counter
def solution(k, tangerine):
    answer = 0
    #count_t = {t:tangerine.count(t) for t in tangerine}
    count_t = Counter(tangerine)
    
    for v in sorted(count_t.values(), reverse=True):
        if k-v > 0:
            k -= v
            answer += 1
            if k <= 0:
                return answer
        else:
            return answer + 1
    return answer

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])