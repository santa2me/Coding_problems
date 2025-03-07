def solution(numbers, hand):
    answer = ''
    # keypad = [[3*j + i + 1 for i in range(3)] for j in range(3)]
    # keypad.append([-1,0,-2])
    l_key = {1:0, 4:1, 7:2}
    r_key = {3:0, 6:1, 9:2}
    m_key = {2:0, 5:1, 8:2, 0:3}
    
    l_pos = [3,0]
    r_pos = [3,2]
    middle = [1,1]
    
    for n in numbers:
        if n in l_key:
            answer += "L"
            l_pos[0] = l_key[n]
            l_pos[1] = 0
        elif n in r_key:
            answer += "R"
            r_pos[0] = r_key[n]
            r_pos[1] = 2
        else:
            middle[0] = m_key[n]
            l_diff = abs(l_pos[0]-middle[0]) + abs(l_pos[1]-middle[1])
            r_diff = abs(r_pos[0]-middle[0]) + abs(r_pos[1]-middle[1])
            
            if l_diff < r_diff:
                answer += "L"
                l_pos[0] = middle[0]
                l_pos[1] = middle[1]
            elif r_diff < l_diff:
                answer += "R"
                r_pos[0] = middle[0]
                r_pos[1] = middle[1]
            else:
                if hand=="left":
                    answer += "L"
                    l_pos[0] = middle[0]
                    l_pos[1] = middle[1]
                else:
                    answer += "R"
                    r_pos[0] = middle[0]
                    r_pos[1] = middle[1]
    return answer
            
    
#     for n in numbers:
#         for i, rows in enumerate(keypad):
#             if n in rows:
#                 j = rows.index(n)
        
#         if j==0:
#             answer += "L"
#             l_pos[0] = i
#         elif j==2:
#             answer += "R"
#             r_pos[0] = i
#         else:
#             l_diff = abs(l_pos[0]-i) + abs(l_pos[1]-j)
#             r_diff = abs(r_pos[0]-i) + abs(r_pos[1]-j)
            
#             if l_diff < r_diff:
#                 l_pos[0] = i
#                 l_pos[1] = j
#                 answer += "L"
#             elif r_diff < l_diff:
#                 r_pos[0] = i
#                 r_pos[1] = j
#                 answer += "R"
#             else:
#                 if hand=="right":
#                     r_pos[0] = i
#                     r_pos[1] = j
#                     answer += "R"
#                 else:
#                     l_pos[0] = i
#                     l_pos[1] = j
#                     answer += "L"
                    
                
                
                
    #     i,j = keypad_pos.index(n)
    #     print(i,j)

            
            


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
#기댓값: "LRLLLRLLRRL"