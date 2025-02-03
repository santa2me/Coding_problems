def solution(n,a,b):
    answer = 0
    
    while a!=1 and b!=2:
        if a%2:
            a += 1
        if b%2:
            b += 1
        
        a //= 2
        b //= 2
        
        answer += 1

    return answer
solution(8, 4, 7)