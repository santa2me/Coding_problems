def solution(today, terms, privacies):
    answer = []
    t_year, t_month, t_date = map(int, today.split("."))
    
    
    #약관종류/유효기간 정리
    term = {}
    for t in terms:
        t = t.split()
        term[t[0]] = int(t[-1]) 
    
    for i,p in enumerate(privacies):
        available = term[p[-1]]
        year, month, date = map(int, p.split()[0].split("."))
        
        if available > 12:
            year += (available//12)
            available %= 12
            
        check = month+available
        if check > 12:
            year += 1
            
        month = check%12
        
        if month==0:
            month = 12
            
        if date==1:
            date = 28
            month -= 1
        else:
            date -= 1
        
        if (year, month, date) < (t_year, t_month, t_date):
            answer.append(i+1)
        
    return answer