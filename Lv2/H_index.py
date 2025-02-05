def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    
    for i, c in enumerate(citations, start=1):
        if c >= i:
            h_index = i
        else:
            break

    return h_index

# def solution(citations):
#     h_index = {i: sum(1 for c in citations if c >= i) for i in range(1, max(citations) + 1)}
    
#     max_h_index = max((k for k, v in h_index.items() if k <= v), default=0)
    
    

#     return max_h_index



