## 📌 Minimum Jumps — Greedy Solution

## 🧩 Problem Statement

You are given an array `arr[]` where each element represents the **maximum number of steps you can jump forward** from that position.

Your task is to find the **minimum number of jumps required** to reach the last index starting from index `0`.

* Return `-1` if the last index is not reachable.

---

## 📥 Input

* Integer array `arr[]`

---

## 📤 Output

* Minimum number of jumps to reach the last index
* `-1` if unreachable

---

## 📘 Examples

### Example 1

**Input:**
`arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]`

**Output:**
`3`

**Explanation:**
0 → 1 → 4 → 10

---

### Example 2

**Input:**
`arr = [1, 4, 3, 2, 6, 7]`

**Output:**
`2`

**Explanation:**
0 → 1 → 5

---

### Example 3

**Input:**
`arr = [0, 10, 20]`

**Output:**
`-1`

**Explanation:**
Cannot move from index 0

---

## 💡 Idea (Greedy Approach)

We track:

* `farthest` → farthest index we can reach
* `end` → end of current jump range
* `jumps` → number of jumps taken

We expand the range as far as possible and only increase jump count when needed.

---

## 🚀 Algorithm

1. If first element is `0`, return `-1`

2. Initialize:

   * `jumps = 0`
   * `farthest = 0`
   * `end = 0`

3. Traverse array (except last element):

   * Update `farthest = max(farthest, i + arr[i])`
   * If `i == end`:

     * Increase `jumps`
     * Update `end = farthest`
   * If `end >= last index`, break early

4. If `end` never reaches last index → return `-1`

---

## 🧑‍💻 Python Implementation

```python id="min_jumps"
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 0
        farthest = 0
        end = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + arr[i])
            
            if i == end:
                jumps += 1
                end = farthest
                
                if end >= n - 1:
                    return jumps
                
                if end == i:
                    return -1
        
        return -1
```

---

## ⏱️ Complexity

* **Time:** O(n)
* **Space:** O(1)

---

## ⚠️ Edge Cases

* First element is 0 → unreachable
* Already at last index
* Array with all zeros except first
* Large jumps skipping directly to end

---

## 🏁 Summary

This is a **greedy range-expansion problem** where we always track the farthest reachable index and count jumps only when the current range is exhausted.
