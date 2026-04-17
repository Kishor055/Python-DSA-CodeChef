## 📌 Longest Subarray with Sum K

## 🧩 Problem Statement

Given an array `arr[]` (can contain **positive, negative, and zero values**) and an integer `k`, find the **length of the longest subarray** whose sum equals `k`.

If no such subarray exists, return `0`.

---

## 📥 Input

* Integer array `arr[]`
* Integer `k`

---

## 📤 Output

* Length of the **longest subarray** with sum = `k`

---

## 📘 Examples

### Example 1

**Input:**
`arr = [10, 5, 2, 7, 1, -10], k = 15`

**Output:**
`6`

---

### Example 2

**Input:**
`arr = [-5, 8, -14, 2, 4, 12], k = -5`

**Output:**
`5`

---

### Example 3

**Input:**
`arr = [10, -10, 20, 30], k = 5`

**Output:**
`0`

---

## 💡 Idea (Prefix Sum + HashMap)

Since the array contains **negative numbers**, sliding window ❌ won’t work.

We use:

* **Prefix sum**
* **HashMap (dictionary)** to store first occurrence of each sum

---

## 🚀 Algorithm

1. Initialize:

   * `prefix_sum = 0`
   * `max_len = 0`
   * `hashmap = {}`

2. Traverse array:

   * Add current element to `prefix_sum`
   * If `prefix_sum == k` → update `max_len = i + 1`
   * If `(prefix_sum - k)` exists in hashmap:

     * subarray found → update length
   * Store prefix_sum in hashmap (only first occurrence)

---

## 🧑‍💻 Python Implementation

```python id="longest_subarray_k"
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
```

---

## ⏱️ Complexity

* **Time:** O(n)
* **Space:** O(n)

---

## ⚠️ Edge Cases

* No subarray found → return `0`
* Entire array sum equals `k`
* Negative numbers present
* Multiple valid subarrays → choose longest

---

## 🏁 Summary

This problem is best solved using **prefix sum + hashing**, which efficiently tracks subarrays and works even with negative numbers, unlike sliding window.
