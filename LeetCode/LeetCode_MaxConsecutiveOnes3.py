def longestOnes(nums,k):
    max_1, zero_count = 0, 0
    zero_idx = []

    for i,n in enumerate(nums):
        if n==1 and zero_count == k:
            max_1 = max(max_1, i-zero_idx[-(k+1)])
        elif n==0:
            zero_count += 1
            zero_idx.append(i)
            if zero_count == k:
                max_1 = max(max_1, i-zero_idx[-k])
            elif zero_count > k:
                max_1 = max(max_1, i-zero_idx[-(k+1)])
                zero_count -= 1
            
        
    
    print(max_1)

longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)