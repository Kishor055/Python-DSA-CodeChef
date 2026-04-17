class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 0
        farthest = 0
        end = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + arr[i])
            
            if i == end:
                jumps += 1
                end = farthest
                
                if end >= n - 1:
                    return jumps
                
                if end == i:
                    return -1
        
        return -1