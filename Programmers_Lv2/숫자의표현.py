def solution(n):
    answer = 0
    i = (n//2) + 1
    while i >= 1:
        sum_i = i
        for j in range(i+1,n):
            sum_i += j
            if sum_i > n:
                break
            elif sum_i == n:
                answer += 1
                break
        i -= 1
    return answer+1
solution(15)