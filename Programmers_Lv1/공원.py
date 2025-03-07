def solution(mats, park):
    # Sort mats in descending order
    mats.sort(reverse=True)
    
    rows, cols = len(park), len(park[0])
    
    # Function to check if a mat of size k x k can fit at (r, c)
    def can_place(k, r, c):
        if r + k > rows or c + k > cols:
            return False
        for i in range(r, r + k):
            for j in range(c, c + k):
                if park[i][j] != "-1":
                    return False
        return True
    
    # Iterate over each mat size
    for mat in mats:
        for r in range(rows):
            for c in range(cols):
                if can_place(mat, r, c):
                    return mat
    
    # If no mat can fit
    return -1




# def solution(mats, park):
#     answer = 0
#     park = [["1"]+ row + ["1"] for row in park] #side barrier

#     available_i, available_j = 0,0
#     max_w, max_h = 0, 0
#     max_w_mat = {}
#     for i, row in enumerate(park):
#         for j, mat in enumerate(row):
#             if mat == "-1":
#                 max_w += 1
#             else:
#                 if max_w > 0:
#                     max_w_mat[i,j-1] = max_w
#                     max_w = 0
    
    
#     print(max_w_mat)
#     filtered_max_w = {k:v for k,v in max_w_mat.items() if v != 1}
#     print(filtered_max_w)
    
#     for (i,j), w in filtered_max_w.items():
#         for idx in range(w,0,-1):
#             print(idx)
            
#         print(i,j,w)
# return answer