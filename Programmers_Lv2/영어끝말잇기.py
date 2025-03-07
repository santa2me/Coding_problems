def solution(n, words):
    answer = [0,0]
    used = []
    j = 0
    for i,w in enumerate(words):
        if i%n == 0:
            j += 1
    
        if not used:
            used.append(w)
        elif used and used[-1][-1] == w[0] and w not in used:
            used.append(w)
        
        else:
            answer[0] = i%n+1
            answer[1] = j
            break
    return answer

solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])