def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    
    return dp[n]


# import itertools
# def solution(n):
#     answer = 1
#     a,b = 1, 2
#     dict_1 = {}
#     for i in range(n-1,-1,-1):
#         jump = [a]*i
        
#         while sum(jump) < n:
#             jump += [b]
            
#         if sum(jump) == n:
#             dict_1[i] = jump
    
#     for value in dict_1.values():
#         #possible = set((itertools.permutations(value)))
#         answer += len(set(itertools.permutations(value)))
#     return answer

solution(4)


#     for i in range(n-1,-1,-1):
#         jump = []
#         jump += [a]*i
#         for j in range(n//2):
#             jump += [b]

#             sum_j = sum(jump)
#             if sum_j == n:
#                 possible = set(itertools.permutations(jump, len(jump)))
#                 answer += len(possible)
#                 break
#             elif sum_j < n:
#                 continue
#             else:
#                  break