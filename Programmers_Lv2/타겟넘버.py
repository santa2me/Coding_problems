#DFS
def solution(numbers, target):
    sub_num = (sum(numbers)-target) // 2
    def dfs(index, current_sum):
        nonlocal count
        if current_sum == sub_num:
            count += 1

        for i in range(index, len(numbers)):
            dfs(i + 1, current_sum + numbers[i])

    count = 0
    dfs(0, 0)
    return count


#모든 부분집합
# from itertools import combinations
# def solution(numbers, target):
#     answer = 0
#     sub_num = (sum(numbers)-target) // 2
    
#     for r in range(1, len(numbers) + 1):
#         for subset in combinations(numbers, r):
#             if sum(subset) == sub_num:
#                 answer += 1
#     return answer