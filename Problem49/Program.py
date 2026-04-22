class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        Sn = n * (n + 1) // 2
        S2n = n * (n + 1) * (2 * n + 1) // 6
        
        S = sum(arr)
        S2 = sum(x * x for x in arr)
        
        diff = S - Sn
        diff_sq = S2 - S2n
        
        sum_xy = diff_sq // diff
        
        repeating = (diff + sum_xy) // 2
        missing = repeating - diff
        
        return [repeating, missing]