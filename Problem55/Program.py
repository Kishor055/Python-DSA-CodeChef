def characterReplacement(s: str, k: int) -> int:
    freq = [0] * 26  # For A-Z
    left = 0
    max_freq = 0
    result = 0

    for right in range(len(s)):
        index = ord(s[right]) - ord('A')
        freq[index] += 1

        # Update max frequency in window
        max_freq = max(max_freq, freq[index])

        # If replacements needed > k, shrink window
        while (right - left + 1) - max_freq > k:
            freq[ord(s[left]) - ord('A')] -= 1
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result


# Example usage
print(characterReplacement("ABBA", 2))  # Output: 4
print(characterReplacement("ADBD", 1))  # Output: 3