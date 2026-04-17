## 📌 Sort 0s, 1s and 2s (Dutch National Flag Problem)

## 🧩 Problem Statement

Given an array `arr[]` containing only **0s, 1s, and 2s**, sort it in ascending order **without using built-in sorting functions**.

You must aim for a **one-pass, constant space solution**.

---

## 📥 Input

* Integer array `arr[]` containing only values: `0, 1, 2`

---

## 📤 Output

* Sorted array in non-decreasing order

---

## 📘 Examples

### Example 1

**Input:**
`arr = [0, 1, 2, 0, 1, 2]`

**Output:**
`[0, 0, 1, 1, 2, 2]`

---

### Example 2

**Input:**
`arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]`

**Output:**
`[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]`

---

## 💡 Idea (Dutch National Flag Algorithm)

We use **three pointers**:

* `low` → boundary for 0s
* `mid` → current element
* `high` → boundary for 2s

### Rules:

* If `arr[mid] == 0` → swap with `low`, move both forward
* If `arr[mid] == 1` → move `mid`
* If `arr[mid] == 2` → swap with `high`, move `high` backward

---

## 🚀 Algorithm

1. Initialize:

   * `low = 0`
   * `mid = 0`
   * `high = len(arr) - 1`

2. While `mid <= high`:

   * If `arr[mid] == 0`:

     * swap `arr[low]` and `arr[mid]`
     * `low += 1`, `mid += 1`
   * Else if `arr[mid] == 1`:

     * `mid += 1`
   * Else (arr[mid] == 2):

     * swap `arr[mid]` and `arr[high]`
     * `high -= 1`

---

## 🧑‍💻 Python Implementation

```python id="dnf_sort"
class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            
            elif arr[mid] == 1:
                mid += 1
            
            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr
```

---

## ⏱️ Complexity

* **Time:** O(n) (single pass)
* **Space:** O(1)

---

## ⚠️ Edge Cases

* All 0s
* All 1s
* All 2s
* Already sorted array
* Reverse order array

---

## 🏁 Summary

This is a classic **three-way partitioning problem**, efficiently solved using the **Dutch National Flag Algorithm** in a single traversal with constant space.
