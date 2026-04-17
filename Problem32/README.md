## 📌 Kadane’s Algorithm — Maximum Subarray Sum

## 🧩 Problem Statement

Given an integer array `arr[]`, find the **maximum sum of a contiguous subarray** (at least one element must be included).

A subarray is a **continuous sequence of elements** in the array.

---

## 📥 Input

* Integer array `arr[]`

---

## 📤 Output

* A single integer representing the **maximum subarray sum**

---

## 📘 Examples

### Example 1

**Input:**
`arr = [2, 3, -8, 7, -1, 2, 3]`

**Output:**
`11`

**Explanation:**
Subarray `[7, -1, 2, 3]` gives maximum sum = 11

---

### Example 2

**Input:**
`arr = [-2, -4]`

**Output:**
`-2`

**Explanation:**
Best subarray is `[-2]`

---

### Example 3

**Input:**
`arr = [5, 4, 1, 7, 8]`

**Output:**
`25`

**Explanation:**
Whole array gives maximum sum

---

## 💡 Idea (Kadane’s Algorithm)

At each position, decide:

> Should we extend the previous subarray or start fresh from current element?

We maintain:

* `current_sum` → best sum ending at current index
* `max_sum` → global maximum found so far

---

## 🚀 Algorithm

1. Initialize:

   * `current_sum = arr[0]`
   * `max_sum = arr[0]`

2. Traverse array from index 1:

   * `current_sum = max(arr[i], current_sum + arr[i])`
   * `max_sum = max(max_sum, current_sum)`

3. Return `max_sum`

---

## 🧑‍💻 Python Implementation

```python id="kadanes_algo"
class Solution:
    def maxSubArraySum(self, arr):
        current_sum = arr[0]
        max_sum = arr[0]
        
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
```

---

## ⏱️ Time Complexity

* **O(n)** → single traversal

---

## 🧠 Space Complexity

* **O(1)** → constant space

---

## ⚠️ Edge Cases

* All negative numbers → return largest (least negative)
* Single element array
* Mix of positive and negative values
* All positive numbers → sum of entire array

---

## 🏁 Summary

Kadane’s Algorithm is a **greedy dynamic programming technique** that efficiently finds the maximum subarray sum in linear time using constant space.
