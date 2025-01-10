def solution(survey, choices):
    answer = ''
    table = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    comparison = [("R","T"), ("C","F"), ("J","M"), ("A","N")]
    #앞이 비동의, 뒤 동의
    no = [3,2,1]
    yes = [5,6,7]
    
    for i, s in enumerate(survey):
        type1, type2 = s[0], s[1]
        choice = choices[i]
        if choice in no:
            table[type1] += no.index(choice) + 1
        elif choice in yes:
            table[type2] += yes.index(choice) + 1
    
    for x,y in comparison:
        if table[x] > table[y]:
            answer += x
        elif table[x] < table[y]:
            answer += y
        else:
            answer += x
            
    return answer

solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
기댓값 = "TCMA"