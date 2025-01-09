def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    #최소 몇번의 키를 눌러야 keymap의 알파벳을 얻을 수 있는지 dictionary 형태로 저장장
    for keys in keymap:
        for i in range(len(keys)):
            key = keys[i]
            if key in key_dict.keys():
                key_dict[key] = min(i+1, key_dict[key])
            else:
                key_dict[key] = i+1
    
    #target의 키가 keymap에 있는지 확인
    for target in targets:
        count = 0
        for t in target:
            if t in key_dict.keys():
                count += key_dict[t]
            else:
                count = 0
                break
        
        if count != 0:
            answer.append(count)
        else:
            answer.append(-1)
        
    return answer 