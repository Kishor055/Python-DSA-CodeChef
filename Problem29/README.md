# 📌 Indexes of Subarray Sum

## 🧩 Problem Statement

Given an array `arr[]` containing only **non-negative integers**, and a target value `target`, the task is to find a **continuous subarray** whose sum equals the given target.

Return the **1-based indices** of the leftmost and rightmost elements of the first such subarray found.

If no such subarray exists, return `[-1]`.

---

## 📥 Input

* An integer array `arr[]` of size `n`
* An integer `target`

---

## 📤 Output

* A list containing two integers: `[start_index, end_index]` (1-based indexing)
* Or `[-1]` if no valid subarray exists

---

## 📘 Examples

### Example 1

**Input:**
`arr = [1, 2, 3, 7, 5], target = 12`

**Output:**
`[2, 4]`

**Explanation:**
Subarray from index 2 to 4 → `2 + 3 + 7 = 12`

---

### Example 2

**Input:**
`arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15`

**Output:**
`[1, 5]`

**Explanation:**
Subarray from index 1 to 5 → `1 + 2 + 3 + 4 + 5 = 15`

---

### Example 3

**Input:**
`arr = [5, 3, 4], target = 2`

**Output:**
`[-1]`

**Explanation:**
No continuous subarray sums to 2.

---

## ⚙️ Constraints

* `1 ≤ arr.size() ≤ 10^6`
* `0 ≤ arr[i] ≤ 10^3`
* `0 ≤ target ≤ 10^9`

---

## 💡 Approach

Since all array elements are **non-negative**, we can efficiently solve this problem using the **sliding window technique**.

### Key Idea:

* Maintain a window `[start, end]`
* Expand `end` to increase sum
* Shrink `start` if sum exceeds target
* Stop when sum matches target

---

## 🚀 Algorithm

1. Initialize:

   * `start = 0`
   * `current_sum = 0`

2. Iterate `end` from `0` to `n-1`:

   * Add `arr[end]` to `current_sum`

3. While `current_sum > target`:

   * Subtract `arr[start]`
   * Move `start++`

4. If `current_sum == target`:

   * Return `[start + 1, end + 1]`

5. If no match found:

   * Return `[-1]`

---

## ⏱️ Time Complexity

* **O(n)**
  Each element is processed at most twice.

---

## 🧠 Space Complexity

* **O(1)**
  Only constant extra space is used.

---

## 🛠️ Edge Cases

* Target = 0 (may require careful handling of zeros)
* All elements greater than target
* Single element equal to target
* Multiple valid subarrays → return the **first occurrence**

---

## 🏁 Summary

This problem is a classic application of the **sliding window technique** optimized for arrays with **non-negative integers**, ensuring an efficient linear-time solution.
