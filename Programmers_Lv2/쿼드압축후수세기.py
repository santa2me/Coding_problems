def solution(arr):
    def compress(x, y, size):
        first = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:  # 값이 하나라도 다르면 쪼개기
                    half = size // 2
                    compress(x, y, half)  # 좌상
                    compress(x, y + half, half)  # 우상
                    compress(x + half, y, half)  # 좌하
                    compress(x + half, y + half, half)  # 우하
                    return

        # 모든 값이 같다면 압축 가능
        result[first] += 1  

    result = [0, 0]  # [0의 개수, 1의 개수]
    compress(0, 0, len(arr))
    return result

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])