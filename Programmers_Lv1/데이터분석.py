def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    data_order = {"code":0, "date":1, "maximum":2, "remain":3}
    filtered = [row for row in data if row[data_order[ext]] < val_ext]
    
    answer = sorted(filtered, key = lambda row: row[data_order[sort_by]])

    #return(sorted(filter(lambda x:x[data_order[ext]] < val_ext,data),key=lambda x:x[data_order[sort_by]]))
    return answer