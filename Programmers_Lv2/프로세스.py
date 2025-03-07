    # process = {idx:priority for idx, priority in enumerate(priorities)}
    # sorted_process = dict(sorted(process.items(), key=lambda x: x[1], reverse=True))

# from collections import deque

# def solution(priorities, location):
#     queue = deque([(idx, priority) for idx, priority in enumerate(priorities)])
#     sorted_priorities = sorted(priorities, reverse=True)
#     execution_order = 0  # Count how many processes have been executed

#     while queue:
#         idx, priority = queue.popleft()
        
#         # If it's the highest priority, execute it
#         if priority == sorted_priorities[0]:
#             execution_order += 1
#             sorted_priorities.pop(0)  # Remove the executed priority
            
#             # If it's the target process, return its execution order
#             if idx == location:
#                 return execution_order
#         else:
#             # Otherwise, put it back in the queue
#             queue.append((idx, priority))


def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

solution([1, 1, 9, 1, 1, 1], 0)