def solution(n):
    divisor = 1234567
    fib_list = [0, 1]
    
    #피보나치 수열
    for _ in range(2, n+1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    
    return fib_list[n]%divisor
solution(5)