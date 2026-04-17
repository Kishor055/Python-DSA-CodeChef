class Solution:
    def findDuplicates(self, arr):
        result = []
        
        for i in range(len(arr)):
            idx = abs(arr[i]) - 1
            
            if arr[idx] < 0:
                result.append(idx + 1)
            else:
                arr[idx] = -arr[idx]
        
        return result