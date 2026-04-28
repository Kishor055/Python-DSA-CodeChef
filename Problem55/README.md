Longest Repeating Character Replacement (Python)

📌 Problem Statement

Given a string "s" of uppercase English letters and an integer "k", you can perform at most "k" operations.
In each operation, you can change any character to another uppercase letter.

Return the length of the longest substring that can be made of the same character after at most "k" changes.

---

🧠 Key Idea

We use a sliding window to maintain a substring where:

(window length - max frequency of any character) ≤ k

This ensures we can convert all characters in the window to the most frequent one using at most "k" changes.

---

⚡ Approach (Sliding Window)

- Use two pointers ("left", "right")
- Maintain a frequency dictionary
- Track the count of the most frequent character ("max_freq")
- If replacements exceed "k", shrink the window

---

💻 Python Implementation

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

---

🧪 Examples

Example 1

Input: s = "ABBA", k = 2
Output: 4
Explanation: Convert both 'A' → 'B' → "BBBB"

Example 2

Input: s = "ADBD", k = 1
Output: 3
Explanation: Convert 'B' → 'D' → "ADDD"

---

⏱️ Complexity Analysis

Type| Complexity
Time Complexity| O(n)
Space Complexity| O(1)

- Single pass through string
- Constant space (26 letters)

---

🚀 Interview Tips

- Don’t recompute max frequency every time (optimization trick!)
- Focus on window validity condition
- This is a classic LeetCode / GFG sliding window problem

---

🧩 Variations

- Longest substring with at most "k" distinct characters
- Minimum window substring
- Longest repeating character without replacement

---

📎 Practice Link

https://practice.geeksforgeeks.org/problems/longest-repeating-character-replacement/1

---

👨‍💻 Author Note

Great problem to master sliding window + greedy optimization—very common in coding interviews.

---