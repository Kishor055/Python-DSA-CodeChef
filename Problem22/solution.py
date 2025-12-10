class Solution:
    def count_non_minimum(self, nums):
        # Find the minimum value in the array
        M = min(nums)
        
        # Count how many elements are NOT equal to the minimum
        # These are the elements we must convert to M
        operations = sum(1 for x in nums if x != M)
        
        return operations
