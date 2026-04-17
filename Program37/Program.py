class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0
        
        # Step 1: Find candidate
        for num in arr:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Verify candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        
        return -1