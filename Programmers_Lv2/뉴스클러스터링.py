from collections import Counter
def solution(str1, str2):
    str1_list = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_list = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    c1 = Counter(str1_list)
    c2 = Counter(str2_list)
    
    if not str1_list and not str2_list:
        return 65536
    
    intersection = float(sum((c1&c2).values()))
    union = float(sum((c1|c2).values()))
    answer = int(intersection/union * 65536)
    return answer



# def solution(str1, str2):
#     answer = 65536
#     str1 = str1.lower()
#     str2 = str2.lower()
    
#     str1_count = {}
#     str2_count = {}
    
#     intersection = []
#     union = []
    
#     for i in range(len(str1) - 1):
#         s = str1[i:i+2]
#         if s.isalpha():
#             str1_count[s] = str1_count.get(s,0) + 1
            
#     for i in range(len(str2) - 1):
#         s = str2[i:i+2]
#         if s.isalpha():
#             str2_count[s] = str2_count.get(s,0) + 1
            
#     if not str1_count and not str2_count:
#         return answer
    
#     elif not str1_count and str2_count:
#         union.extend([s] * count for s,count in str2_count.items())
#         J = len(intersection) / len(union)
#         return int(J * answer)
    
#     elif not str2_count and str1_count:
#         union.extend([s] * count for s,count in str1_count.items())
#         J = len(intersection) / len(union)
#         return int(J * answer)
#     else:
#         for st, count in str1_count.items():
#             if st in str2_count:
#                 min_st = min(count, str2_count[st])
#                 intersection.extend([st] * min_st)

#                 max_st = max(count, str2_count[st])
#                 union.extend([st] * max_st)
#             else:
#                 union.extend([st] * count)

#         for st2, count in str2_count.items():
#             if st2 not in union:
#                 union.extend([st] * count)

#         J = len(intersection) / len(union)
#         return int(J * 65536)