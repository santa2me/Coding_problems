def solution(s):
    answer = ''
    for char in s.lower():
        if not answer and char.isalpha():
            char = char.upper()
        elif answer and answer[-1] == " " and char.isalpha():
            char = char.upper()
            
        answer += char
    return answer