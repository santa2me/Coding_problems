def solution(park, routes):
    h, w = len(park), len(park[0])
    pos_i,pos_j = next((r, row.index("S")) for r, row in enumerate(park) if "S" in row)
    
    direction = {"E":(0,1), "W":(0,-1), "S":(1,0), "N":(-1,0)}

    for route in routes:
        valid = True
        n = int(route[-1])
        i,j = direction[route[0]]
        
        current_i, current_j = pos_i, pos_j
        
        for _ in range(n):
            move_i, move_j = pos_i+i, pos_j+j
            if not (0 <= move_i < h and 0 <= move_j < w):
                valid = False
                break
                
            if park[move_i][move_j] == "X":
                valid = False
                break
            
            pos_i, pos_j = move_i, move_j
            
        if valid:
            pos_i, pos_j = move_i, move_j
        else:
            pos_i, pos_j = current_i, current_j
               
    return [pos_i, pos_j]

solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])