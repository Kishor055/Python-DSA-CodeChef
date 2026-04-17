## 📌 Count Inversions in an Array

## 🧩 Problem Statement

Given an array `arr[]`, count the number of **inversions**.

An inversion is a pair `(i, j)` such that:

* `i < j`
* `arr[i] > arr[j]`

---

## 📥 Input

* Integer array `arr[]`

---

## 📤 Output

* Integer representing the **total inversion count**

---

## 📘 Examples

### Example 1

**Input:**
`arr = [2, 4, 1, 3, 5]`

**Output:**
`3`

**Explanation:**
Inversions → `(2,1), (4,1), (4,3)`

---

### Example 2

**Input:**
`arr = [2, 3, 4, 5, 6]`

**Output:**
`0`

---

### Example 3

**Input:**
`arr = [10, 10, 10]`

**Output:**
`0`

---

## 💡 Idea

A brute-force approach checks all pairs → **O(n²)** ❌ (too slow)

Instead, use **Merge Sort**:

* While merging, count how many elements from the left array are greater than elements in the right array

---

## 🚀 Algorithm (Merge Sort Based)

1. Divide the array into two halves
2. Recursively count inversions in both halves
3. Count **cross inversions** during merge:

   * If `left[i] > right[j]`, then all remaining elements in left are also greater

---

## 🧑‍💻 Python Implementation

```python id="count_inversions"
class Solution:
    def inversionCount(self, arr):
        return self.merge_sort(arr, 0, len(arr) - 1)
    
    def merge_sort(self, arr, left, right):
        inv_count = 0
        
        if left < right:
            mid = (left + right) // 2
            
            inv_count += self.merge_sort(arr, left, mid)
            inv_count += self.merge_sort(arr, mid + 1, right)
            inv_count += self.merge(arr, left, mid, right)
        
        return inv_count
    
    def merge(self, arr, left, mid, right):
        temp = []
        i, j = left, mid + 1
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inv_count += (mid - i + 1)
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= right:
            temp.append(arr[j])
            j += 1
        
        # copy back to original array
        for idx in range(len(temp)):
            arr[left + idx] = temp[idx]
        
        return inv_count
```

---

## ⏱️ Complexity

* **Time:** O(n log n)
* **Space:** O(n)

---

## ⚠️ Edge Cases

* Already sorted → 0 inversions
* Reverse sorted → maximum inversions
* All elements same → 0 inversions

---

## 🏁 Summary

Counting inversions efficiently requires a **modified merge sort**, reducing complexity from **O(n²) to O(n log n)** by leveraging sorted subarrays during merging.
