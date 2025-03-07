def solution(board, moves):
    answer = 0
    board_cols = [[board[row][col] for row in range(len(board)) if board[row][col] != 0] for col in range(len(board[0]))]

    # transposed = [list(row) for row in zip(*board)]
    # transposed_non_zeros = [[val for val in row if val != 0] for row in zip(*board)]
    # print(transposed)
    
    basket = []

    for m in moves:
        pos = board_cols[m-1]
        if pos:
            if basket and basket[-1] == pos[0]:
                pos.pop(0)
                basket.pop()
                answer += 2
            else:
                basket.append(pos.pop(0))
        
    return answer