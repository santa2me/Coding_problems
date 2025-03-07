def solution(s):
    initial_len = len(s)
    zeros, count = 0,0

    while s!="1":
        s = s.replace("0","")
        c = len(s)
        zeros += initial_len - c
        
        s = bin(c)[2:]
        initial_len = len(s)
        count += 1
    return [count, zeros]

solution("110010101001")