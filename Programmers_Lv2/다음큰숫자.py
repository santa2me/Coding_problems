def solution(n):
    count_n = bin(n).count("1")
    
    while True:
        n = n + 1
        count_i = bin(n).count("1")
        if count_i == count_n:
            return n