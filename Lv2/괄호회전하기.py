def solution(s):
    answer = 0
    s2, l = s*2, len(s)
    
    dict_s = {"{" : "}", "[" : "]", "(" : ")"}
    for i in range(l):
        check = []
        moved_s = s2[i:i+l]
        valid = True
        
        for char in moved_s:
            if char in dict_s:  # Opening bracket
                check.append(char)
            else:  # Closing bracket
                if check and dict_s[check[-1]] == char:
                    check.pop()
                else:
                    valid = False
                    break 
        
        if valid and not check:
            answer += 1

    return answer

solution("[](){}")