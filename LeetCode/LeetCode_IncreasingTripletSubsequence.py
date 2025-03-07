
def increasingTriplet(nums):
    i = nums[0]

    for i in range(len(nums)-2):
        num = nums[i]
        for j in range(1,len(nums)-1):
            if num < nums[j]:
                if any(nums[j] < nums[k] for k in range(j, len(nums))):
                    return True
                else:
                    continue
    return False
    
increasingTriplet([2,1,0,2,0,2,0,2,0,2,0,1])