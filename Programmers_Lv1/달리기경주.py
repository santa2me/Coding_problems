def solution(players, callings):
    answer = []
    player_pos = {p:idx for idx,p in enumerate(players)}
    
    for c in callings:
        idx = player_pos[c]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        player_pos[players[idx]] = idx
        player_pos[players[idx-1]] = idx - 1

    return players