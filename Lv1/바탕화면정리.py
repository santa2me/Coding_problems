def solution(wallpaper):
    lux, luy = -1,-1
    rdx = []
    rdy = []
    for i,wall in enumerate(wallpaper):
        for j in range(len(wall)):
            if lux == -1 and wall[j] == "#":
                lux = i

            if wall[j] == "#":
                rdy.append(j+1)
    rdy = int(max(rdy))
    
    for j in range(len(wallpaper[0])):
        for i in range(len(wallpaper)):
            if luy == -1 and wallpaper[i][j] == "#":
                luy = j
            if wallpaper[i][j] == "#":
                rdx.append(i+1)
    
    rdx = int(max(rdx))
                
    return [lux, luy, rdx, rdy]

# def solution(wall):
#     a, b = [], []
#     for i in range(len(wall)):
#         for j in range(len(wall[i])):
#             if wall[i][j] == "#":
#                 a.append(i)
#                 b.append(j)
#     return [min(a), min(b), max(a) + 1, max(b) + 1]

solution([".#...", "..#..", "...#."])