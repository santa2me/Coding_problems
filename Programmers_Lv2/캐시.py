def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities_lower = [c.lower() for c in cities]
    
    for city in cities_lower:
        if len(cache) >= cacheSize:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.insert(0,city)
            else:
                answer += 5
                if cache:
                    cache.pop()
                    cache.insert(0,city)
                elif len(cache) < cacheSize:
                    cache.insert(0,city)
        else:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.insert(0,city)
            else:
                cache.insert(0,city)
                answer += 5
            
    return answer

solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])

# from collections import deque

# def solution(cacheSize, cities):
#     if cacheSize == 0:  # If cache size is 0, all cities result in cache miss (5ms each)
#         return len(cities) * 5  

#     cache = deque(maxlen=cacheSize)  # Automatically removes oldest entry when full
#     answer = 0

#     for city in cities:
#         city = city.lower()  # Convert city to lowercase for case-insensitive check
#         if city in cache:
#             answer += 1  # Cache hit
#             cache.remove(city)  # Move the city to the front (most recently used)
#         else:
#             answer += 5  # Cache miss
        
#         cache.appendleft(city)  # Insert city at the front (LRU update)

#     return answer

# Handle cacheSize == 0 case early → Avoids unnecessary logic.
# Use deque(maxlen=cacheSize) → Automatically maintains cache size.
# Avoid redundant checks (if cache) → deque already handles it.
# More readable and efficient → O(N) complexity with deque optimizations.