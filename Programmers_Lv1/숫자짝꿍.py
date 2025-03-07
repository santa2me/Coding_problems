def solution(X, Y):
    answer = ''
    X_count = {}
    Y_count = {}
    
    for x in X:
        X_count[x] = X_count.get(x,0) + 1
    
    for y in Y:
        Y_count[y] = Y_count.get(y,0) + 1

    # Build the result in reverse order
    result = []
    for i in range(9, -1, -1):
        char = str(i)
        if char in X_count and char in Y_count:
            count = min(X_count[char], Y_count[char])
            result.append(char * count)

    if not result:  # No common digits
        return "-1"
    
    answer = ''.join(result)
    if answer == '0' * len(answer):  # All digits are zeros
        return "0"

    return answer


## First Try ## - timely inefficient
# def solution(X, Y):
#     answer = ''
#     X_count = {}
#     Y_count = {}
    
#     for x in X:
#         X_count[x] = X_count.get(x,0) + 1
    
#     for y in Y:
#         Y_count[y] = Y_count.get(y,0) + 1
    
#     for i in range(10):
#         if str(i) in X_count.keys() and str(i) in Y_count.keys():
#             answer += str(i) * min(X_count[str(i)], Y_count[str(i)])
        
#     if not answer:
#         return "-1"
#     elif int(answer)==0:
#         return "0"
#     else:
#         return ''.join(sorted(answer, reverse = True))

## Method 2: without dictionary
# for i in range(9,-1,-1) :
#         answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
