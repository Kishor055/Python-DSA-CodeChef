# 📌 Second Largest Element in Array

## 🧩 Problem Statement

Given an array of positive integers `arr[]`, the task is to find the **second largest distinct element** in the array.

If the second largest element does not exist (i.e., all elements are equal), return `-1`.

---

## 📥 Input

* An integer array `arr[]` of size `n`

---

## 📤 Output

* A single integer representing the **second largest distinct element**
* Return `-1` if it does not exist

---

## 📘 Examples

### Example 1

**Input:**
`arr = [12, 35, 1, 10, 34, 1]`

**Output:**
`34`

**Explanation:**

* Largest element = 35
* Second largest element = 34

---

### Example 2

**Input:**
`arr = [10, 5, 10]`

**Output:**
`5`

**Explanation:**

* Largest element = 10
* Second largest distinct element = 5

---

### Example 3

**Input:**
`arr = [10, 10, 10]`

**Output:**
`-1`

**Explanation:**
All elements are equal, so no second largest exists.

---

## ⚙️ Constraints

* `2 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`

---

## 💡 Approach

We solve this problem using a **single traversal (Greedy approach)** by maintaining two variables:

* `largest` → stores the maximum element
* `second_largest` → stores the second maximum distinct element

---

## 🚀 Algorithm

1. Initialize:

   * `largest = -1`
   * `second_largest = -1`

2. Traverse the array:

   * If current element > `largest`:

     * Update `second_largest = largest`
     * Update `largest = current element`
   * Else if current element is:

     * not equal to `largest`
     * and greater than `second_largest`
     * update `second_largest`

3. Return `second_largest`

---

## ⏱️ Time Complexity

* **O(n)** → single traversal of array

---

## 🧠 Space Complexity

* **O(1)** → constant extra space

---

## ⚠️ Edge Cases

* All elements equal → return `-1`
* Only two elements → return the smaller one
* Already sorted array
* Reverse sorted array
* Duplicate largest values

---

## 🏁 Summary

This problem is efficiently solved using a **greedy single-pass approach**, avoiding sorting and ensuring optimal performance even for large inputs.

---
