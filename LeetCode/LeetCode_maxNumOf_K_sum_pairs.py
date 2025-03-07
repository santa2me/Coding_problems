from collections import Counter
class Solution:
    def maxOperations(nums,k):
        pairs = Counter(nums)
        count = 0

        for key,value in pairs.items():
            x = k-key
            if x in pairs and x != k//2 and pairs[x] > 0 and value > 0:
                sub = min(value,pairs[x])
                count += sub
                pairs[key] -= sub
                pairs[x] -= sub
            elif x in pairs and x==k//2 and k%2==0:
                count += value//2
        return count
    
    maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3)