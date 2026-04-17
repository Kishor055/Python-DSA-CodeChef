class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1  # total numbers should be 1 to n
        
        total_sum = n * (n + 1) // 2
        arr_sum = sum(arr)
        
        return total_sum - arr_sum