class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders = []
        max_right = -1
        
        for i in range(n - 1, -1, -1):
            if arr[i] >= max_right:
                leaders.append(arr[i])
                max_right = arr[i]
        
        return leaders[::-1]