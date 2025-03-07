from collections import deque
class RecentCounter:

    def __init__(self):
        self.request = deque()
        

    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request[0] < t - 3000:  # Remove outdated requests
            self.request.popleft()
        return len(self.request)  # Count of valid requests

# Debugging Test Case
if __name__ == "__main__":
    obj = RecentCounter()
    inputs = [1, 100, 3001, 3002]  # From the problem statement
    results = []
    
    for t in inputs:
        result = obj.ping(t)
        results.append(result)
        print(f"ping({t}) -> {result}")  