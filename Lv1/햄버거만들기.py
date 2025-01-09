def solution(ingredient):
    answer = 0
    stack = []
    for ing in ingredient:
        stack.append(ing)
        # Check if the last 4 items match the hamburger pattern
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            # Remove the last 4 elements using pop
            for _ in range(4):
                stack.pop()
    return answer


##Few test cases timeout##
# def solution(ingredient):
#     answer = 0
#     stack = []
#     hamburger = [1,2,3,1]
    
#     for ing in ingredient:
#         stack.append(ing)
        
#         if stack[-4:] == hamburger:
#             answer += 1
#             stack = stack[:-4]

#     return answer


## First Try ##
#The issue with your current implementation using replace is that it repeatedly converts the list ingredient to a string 
# and checks for the pattern '1231'. This is inefficient for large inputs, and the performance degrades as the size of the 
# list increases due to string manipulations.
# Additionally, your implementation may fail tests due to overlapping or out-of-order elements when repeatedly replacing 
# substrings.
# To solve the problem efficiently and handle edge cases properly, a stack-based approach is recommended.


# def solution(ingredient):
#     answer = 0
#     ingredient = ''.join(map(str,ingredient))
#     hamburger = '1231'
    
#     while hamburger in ingredient:
#         ingredient = ingredient.replace(hamburger,"")
#         answer += 1
#     return answer
