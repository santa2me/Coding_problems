def solution(s):
    answer = []
    s = s[2:-2]
    sets = s.split("},{")
    s_list = [list(map(int, item.split(","))) for item in sets]
    
    s_list.sort(key=len)

    for item in sorted(s_list, key=len):
        if not answer:
            answer.extend(item)
        else:
            new = list(set(item) - set(answer))
            answer.extend(new)
    
    return answer