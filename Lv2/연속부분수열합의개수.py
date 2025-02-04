def solution(elements):
    sums, n = [], len(elements)
    elements += elements[:-1]
    for i, a in enumerate(elements):
        SUM = a
        sums.append(SUM)
        for b in elements[i + 1:i + n]:
            SUM += b
            sums.append(SUM)

    return len(list(set(sums)))

# from itertools import combinations
# def solution(elements):
#     answer = 0
#     sum_of_nums = []
    
#     for i in range(1,len(elements)):
#         temp_sum = combinations(elements,i)
        
#         for s in temp_sum:
#             if s not in sum_of_nums:
#                 sum_of_nums.append(s)
            
#     return len(sum_of_nums)

solution([7, 9, 1, 1, 4])