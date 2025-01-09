def solution(lottos, win_nums):
    answer = []
    #점수별 등수수
    order = {6:1, 5:2, 4:3, 3:4, 2:5, 0:6}
    zeros = lottos.count(0)
    correct = 0
    for num in lottos:
        if num in win_nums:
            correct += 1
    
    answer.extend([order[zeros+correct], order[correct]])
    return answer

solution("1D2S#10S")