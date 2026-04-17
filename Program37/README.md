## 📌 Majority Element (Boyer-Moore Voting Algorithm)

## 🧩 Problem Statement

Given an array `arr[]`, find the **majority element**.

A majority element is an element that appears **strictly more than ⌊n/2⌋ times**.

* If such an element exists, return it
* Otherwise, return `-1`

---

## 📥 Input

* Integer array `arr[]`

---

## 📤 Output

* Majority element, or `-1` if none exists

---

## 📘 Examples

### Example 1

**Input:**
`arr = [1, 1, 2, 1, 3, 5, 1]`

**Output:**
`1`

---

### Example 2

**Input:**
`arr = [7]`

**Output:**
`7`

---

### Example 3

**Input:**
`arr = [2, 13]`

**Output:**
`-1`

---

## 💡 Idea (Boyer-Moore Voting Algorithm)

We use a **greedy voting approach**:

* Choose a candidate
* Increase count if same element appears
* Decrease count if different element appears
* If count becomes 0 → choose new candidate

⚠️ Important: This only gives a **potential candidate**, so we must **verify it**.

---

## 🚀 Algorithm

### Step 1: Find Candidate

* Initialize:

  * `candidate = None`
  * `count = 0`
* Traverse array:

  * If `count == 0` → set candidate
  * If element == candidate → `count++`
  * Else → `count--`

### Step 2: Verify Candidate

* Count occurrences of candidate
* If > n//2 → return candidate
* Else → return `-1`

---

## 🧑‍💻 Python Implementation

```python id="majority_element"
class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0
        
        # Step 1: Find candidate
        for num in arr:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Verify candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        
        return -1
```

---

## ⏱️ Complexity

* **Time:** O(n)
* **Space:** O(1)

---

## ⚠️ Edge Cases

* Single element → always majority
* No majority element → return `-1`
* All elements same → return that element

---

## 🏁 Summary

The **Boyer-Moore Voting Algorithm** efficiently finds the majority element in **linear time and constant space**, making it optimal for large arrays.
