class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_len = 0
        hashmap = {}
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == k:
                max_len = i + 1
            
            if (prefix_sum - k) in hashmap:
                max_len = max(max_len, i - hashmap[prefix_sum - k])
            
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i
        
        return max_len