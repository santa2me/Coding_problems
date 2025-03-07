def solution(bandage, health, attacks):
    current_health = health #초기체력
    current_time = 0
    
    t,x,y = bandage #시전시간, 초당 회복량, 추가 회복량
    success = 0 #연속 성공시간
    
    for attack_t, damage in attacks:
        time = t
        while time > 0: #붕대감기 시전시간
            if current_time == attack_t: #공격시간
                current_health -= damage
                success = 0
        
                if current_health <= 0: #죽음
                    return -1
                
                current_time += 1
                break
            else:
                current_health += x
                current_time += 1
                success += 1
                
                if success == t: #연속붕대감기 성공
                    current_health += y #추가 회복량
                    success = 0

                if current_health > health: #maximum health일경우 보정
                    current_health = health

    return current_health