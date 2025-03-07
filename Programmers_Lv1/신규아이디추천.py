def solution(new_id):
    answer = ''
    possible = ["_", "-", "."]
    
    for s in new_id.lower():
        if s.isdigit() or s.isalpha() or s in possible:
            if answer and s == "." and answer[-1] == ".":
                continue

            answer += s
    
    if answer and answer[0]==".":
        answer = answer[1:]
    if answer and answer[-1]==".":
        answer = answer[:-1]
    
    if not answer:
        answer += "a"
    
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1]==".":
            answer = answer[:-1]
    if len(answer) < 3:
        answer += answer[-1] * (3-len(answer))

    return answer