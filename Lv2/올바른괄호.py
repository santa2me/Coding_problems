def solution(s):
    answer = True
    
    if s[0] == ")":
        return False
    elif s[-1] == "(":
        return False
    
    for i,c in enumerate(s):
        if c=="(":
            idx = s.index(")")
            s.replace(c," ")
            s.replace(s[idx], " ")

    print(answer)
    return True if not answer else False 

solution("()()")