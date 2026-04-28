class Solution:
    def longestSubstr(self, s, k):
        freq = [0] * 26  # Frequency of A-Z
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            # Update frequency
            index = ord(s[right]) - ord('A')
            freq[index] += 1

            # Track most frequent character in current window
            max_freq = max(max_freq, freq[index])

            # If more than k replacements needed, shrink window
            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            # Update result
            result = max(result, right - left + 1)

        return result