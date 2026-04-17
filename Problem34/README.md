## 📌 Leaders in an Array

## 🧩 Problem Statement

An element in an array `arr[]` is called a **leader** if it is **greater than or equal to all elements to its right**.

The **rightmost element is always a leader**.

Return all leaders in the order they appear in the array.

---

## 📥 Input

* Integer array `arr[]`

---

## 📤 Output

* List of all **leader elements** in left-to-right order

---

## 📘 Examples

### Example 1

**Input:**
`arr = [16, 17, 4, 3, 5, 2]`

**Output:**
`[17, 5, 2]`

---

### Example 2

**Input:**
`arr = [10, 4, 2, 4, 1]`

**Output:**
`[10, 4, 4, 1]`

---

### Example 3

**Input:**
`arr = [5, 10, 20, 40]`

**Output:**
`[40]`

---

## 💡 Idea

We traverse the array from **right to left**, keeping track of the **maximum element seen so far**.

* If current element ≥ max_so_far → it is a leader
* Update max_so_far

Finally, reverse the result (because we traversed from right).

---

## 🚀 Algorithm

1. Initialize:

   * `max_right = -∞`
   * `leaders = []`

2. Traverse array from right to left:

   * If `arr[i] >= max_right`:

     * Add `arr[i]` to `leaders`
     * Update `max_right`

3. Reverse `leaders`

4. Return result

---

## 🧑‍💻 Python Implementation

```python id="leaders_array"
class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders = []
        max_right = -1
        
        for i in range(n - 1, -1, -1):
            if arr[i] >= max_right:
                leaders.append(arr[i])
                max_right = arr[i]
        
        return leaders[::-1]
```

---

## ⏱️ Complexity

* **Time:** O(n)
* **Space:** O(1) extra (excluding output list)

---

## ⚠️ Edge Cases

* Strictly increasing array → only last element
* Strictly decreasing array → all elements
* All equal elements → all are leaders
* Single element → itself is leader

---

## 🏁 Summary

This is a classic **right-to-left scanning problem** where we maintain a running maximum to efficiently identify all leader elements in linear time.
