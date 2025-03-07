def solution(arr1, arr2):
    n,m,p = len(arr1), len(arr2[0]), len(arr2)
    answer = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            answer[i][j] = sum(arr1[i][k] * arr2[k][j] for k in range(p))
    
    return answer