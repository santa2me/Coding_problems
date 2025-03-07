def solution(s):
    int_s = list(map(int, s.split()))
    return f"{min(int_s)} {max(int_s)}"

#str(min(s)) + " " + str(max(s))