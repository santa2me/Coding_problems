def solution(participant, completion):
    answer = ''
    name_count = {}
    
    for p in participant:
        name_count[p] = name_count.get(p,0) + 1
    
    for c in completion:
        name_count[c] -= 1
    
    for name, count in name_count.items():
        if count != 0:
            answer += name
    return answer

   # for p in participant:
    #     if p not in completion:
    #         answer += p
    #     else:
    #         completion.remove(p)
    # return answer