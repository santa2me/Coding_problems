# def solution(brown, yellow):
#     carpet = brown + yellow
#     possible = []
    
#     h = 1
#     while h <= (carpet//2):
#         if carpet%h == 0:
#             w = carpet//h
#             if w >= h and w != carpet:
#                 possible.append([carpet//h, h])
#         h += 1
    
#     if len(possible) > 1:
#         for w,h in possible:
#             if w*2 + (h-2)*2 == brown:
#                 return [w,h]
#     else:
#         return possible[0]

def solution(brown, yellow):
    carpet = brown + yellow
    
    for h in range(1, int(carpet ** 0.5) + 1):
        if carpet % h == 0:  
            w = carpet // h  
            if (w - 2) * (h - 2) == yellow: 
                return [w, h]
