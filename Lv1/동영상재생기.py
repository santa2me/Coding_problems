def min_sec(time):
    time = time.split(":")
    return 60*int(time[0]) + int(time[1])


def opening_check(video_len ,pos, start, end):
    if start <= pos <= end:
        return end
    return pos

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = min_sec(video_len)
    pos = min_sec(pos)
    op_start = min_sec(op_start)
    op_end = min_sec(op_end)
    
    for c in commands:
        pos = opening_check(video_len, pos, op_start, op_end)
        
        if c=="prev":
            pos -= 10
            if pos < 0:
                pos = 0
        elif c=="next":
            pos += 10
            if pos > video_len:
                pos = video_len
                
    pos = opening_check(video_len, pos, op_start, op_end)
    
    mins = str(pos//60)
    sec = str(pos%60)
    
    if len(mins) == 1:
        mins = "0" + mins
    if len(sec) == 1:
        sec = "0" + sec
        
    answer = mins+":"+sec
    return answer

# def seconds_to_time(seconds):
#     minutes, seconds = divmod(seconds, 60)
#     return f"{minutes:02d}:{seconds:02d}


# if command == "prev":
#     current_pos = max(0, current_pos - 10)
# elif command == "next":
#     current_pos = min(video_len, current_pos + 10)