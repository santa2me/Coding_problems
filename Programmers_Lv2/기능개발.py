import math
def solution(progresses, speeds):
    answer = []
    
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    
    publish, count = days[0], 1
    
    for i in range(1,len(days)):
        if days[i] <= publish:
            count += 1
        else:
            answer.append(count)
            publish = days[i]
            count = 1
    
    answer.append(count)
    return answer