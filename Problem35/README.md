## 📌 Array Duplicates

## 🧩 Problem Statement

You are given an array `arr[]` of size `n`, where:

* Elements are in the range **1 to n**
* Each element appears **at most twice**

Your task is to return all elements that appear **exactly twice**.

Return an empty list if no duplicates exist.

---

## 📥 Input

* Integer array `arr[]` of size `n`

---

## 📤 Output

* List of integers that appear **twice**
* Order does not matter (will be sorted by driver code)

---

## 📘 Examples

### Example 1

**Input:**
`arr = [2, 3, 1, 2, 3]`

**Output:**
`[2, 3]`

---

### Example 2

**Input:**
`arr = [3, 1, 2]`

**Output:**
`[]`

---

## 💡 Idea

We use the fact that:

* Elements are in range **1 to n**

So we can use an **in-place marking technique**:

* Treat array indices as hash markers
* Flip sign of visited index
* If already negative → duplicate found

---

## 🚀 Algorithm (In-place marking)

1. Traverse each element `x` in array:

   * Convert to index: `idx = abs(x) - 1`
2. If `arr[idx]` is already negative:

   * `x` is a duplicate → add to result
3. Else:

   * Mark it visited by making it negative

---

## 🧑‍💻 Python Implementation

```python id="array_duplicates"
class Solution:
    def findDuplicates(self, arr):
        result = []
        
        for i in range(len(arr)):
            idx = abs(arr[i]) - 1
            
            if arr[idx] < 0:
                result.append(idx + 1)
            else:
                arr[idx] = -arr[idx]
        
        return result
```

---

## ⏱️ Complexity

* **Time:** O(n)
* **Space:** O(1) extra (excluding output)

---

## ⚠️ Edge Cases

* No duplicates → return `[]`
* All elements repeated twice
* Single element array
* Already negative values after marking

---

## 🏁 Summary

This problem is efficiently solved using an **in-place index marking technique**, leveraging the constrained range (1 to n) to avoid extra space.
