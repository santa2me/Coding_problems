def solution(clothes):
    answer = 0
    
    clothes_dict = {}
    for item, category in clothes:
        clothes_dict.setdefault(category, []).append(item)
    
    
    for idx, items in enumerate(clothes_dict.values()):
        prod_c = 1
        m = len(items)
        answer += m
        prod_c *= m
        
        if len(clothes_dict.keys()) > 1 and idx > 0:
            answer += prod_c
        

    return answer

#clothes_dict.setdefault(category, []).append(item)
#clothes_dict[category] = clothes_dict.get(category, []) + [item]

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])