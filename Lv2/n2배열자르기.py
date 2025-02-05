def solution(n, left, right):
    
#     grids = [[i] * i + [j for j in range(i+1, n+1)] for i in range(1,n+1)]
    
#     grid = sum(grids,[])
    
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]