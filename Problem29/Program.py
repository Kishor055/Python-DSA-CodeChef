# User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        start = 0
        current_sum = 0

        for end in range(len(arr)):
            current_sum += arr[end]

            # shrink window if sum exceeds target
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1

            # check if we found the target
            if current_sum == target:
                return [start + 1, end + 1]  # 1-based indexing

        return [-1]