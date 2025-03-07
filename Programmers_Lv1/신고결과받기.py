def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported = {id:0 for id in id_list}
    users = {id:[] for id in id_list}

    for r in set(report):
        user, report_id = r.split()
        
        users[user].append(report_id)
        reported[report_id] += 1
    
    banned = [id for id, n in reported.items() if n >= k]
    
    for id in banned:
        for u,v in users.items():
            if id in v:
                idx = id_list.index(u)
                answer[idx] += 1

    return answer