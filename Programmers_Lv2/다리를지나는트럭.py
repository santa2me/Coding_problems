from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  
    current_weight = 0 
    truck_weights = deque(truck_weights) 

    while truck_weights or current_weight > 0:
        time += 1  
        
        current_weight -= bridge.popleft()
        
        if truck_weights and current_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

    return time


solution(2, 10, [7, 4, 5, 6])