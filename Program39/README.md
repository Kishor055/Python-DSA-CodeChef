## 📌 Minimize the Heights II

## 🧩 Problem Statement

Given an array `arr[]` representing heights of towers and an integer `k`, you must **modify each tower exactly once** by either:

* Increasing its height by `k`, or
* Decreasing its height by `k`

Your goal is to **minimize the difference between the tallest and shortest towers** after modification.

⚠️ Constraint: Heights must **not become negative**.

---

## 📥 Input

* Integer `k`
* Integer array `arr[]` of size `n`

---

## 📤 Output

* Minimum possible difference between **maximum and minimum heights**

---

## 📘 Examples

### Example 1

**Input:**
`k = 2, arr = [1, 5, 8, 10]`

**Output:**
`5`

---

### Example 2

**Input:**
`k = 3, arr = [3, 9, 12, 16, 20]`

**Output:**
`11`

---

## 💡 Idea

To minimize the height difference:

* Sort the array
* Try to **balance small and large elements**

  * Increase smaller values (`+k`)
  * Decrease larger values (`-k`)

We simulate splitting the array into two parts:

* Left part → increased
* Right part → decreased

---

## 🚀 Algorithm

1. Sort the array

2. Initialize:

   * `ans = arr[n-1] - arr[0]`

3. Set:

   * `small = arr[0] + k`
   * `big = arr[n-1] - k`

4. Traverse from `i = 1` to `n-1`:

   * If `arr[i] - k < 0` → skip
   * Compute:

     * `min_height = min(small, arr[i] - k)`
     * `max_height = max(big, arr[i-1] + k)`
   * Update `ans = min(ans, max_height - min_height)`

---

## 🧑‍💻 Python Implementation

```python id="minimize_heights"
class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[n - 1] - arr[0]
        
        small = arr[0] + k
        big = arr[n - 1] - k
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            
            min_height = min(small, arr[i] - k)
            max_height = max(big, arr[i - 1] + k)
            
            ans = min(ans, max_height - min_height)
        
        return ans
```

---

## ⏱️ Complexity

* **Time:** O(n log n) (due to sorting)
* **Space:** O(1)

---

## ⚠️ Edge Cases

* Single element → difference = 0
* All elements equal
* Large `k` causing negative values → skip those cases
* Already minimized difference

---

## 🏁 Summary

This problem is solved using a **greedy + sorting approach**, where we strategically decide which elements to increase or decrease to minimize the overall height difference.
