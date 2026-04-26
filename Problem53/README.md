# 📌 Check if Pair with Given Sum Exists in Array

## 🧩 Problem Statement

Given an array of integers `arr[]` and a target value `K`, the task is to determine whether there exists a pair of elements in the array whose sum is exactly equal to `K`.

Return `True` if such a pair exists, otherwise return `False`.

---

## 📥 Input

* An integer array `arr[]`
* An integer `K` (target sum)

---

## 📤 Output

* `True` if a valid pair exists
* `False` otherwise

---

## 📌 Examples

### Example 1

```
Input: arr = [0, -1, 2, -3, 1], K = -2
Output: True
Explanation: Pair (-3, 1) gives sum -2
```

### Example 2

```
Input: arr = [1, 2, 3, 4, 5], K = 10
Output: False
```

---

## 🚀 Approaches

---

## 1️⃣ Brute Force Approach

### 💡 Idea

Check all possible pairs using two nested loops.

### ⏱ Complexity

* Time: **O(n²)**
* Space: **O(1)**

### 🧾 Algorithm

1. Iterate through each element.
2. For each element, check all other elements.
3. If any pair sums to `K`, return `True`.

### 💻 Code (Python)

```python
def has_pair_with_sum(arr, K):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == K:
                return True
    return False
```

---

## 2️⃣ Hashing Approach (Optimal)

### 💡 Idea

Use a set to store visited elements and check complement `K - arr[i]`.

### ⏱ Complexity

* Time: **O(n)**
* Space: **O(n)**

### 🧾 Algorithm

1. Initialize an empty set.
2. For each element:

   * Compute complement = `K - arr[i]`
   * If complement exists in set → return True
   * Else insert current element into set

### 💻 Code (Python)

```python
def has_pair_with_sum(arr, K):
    seen = set()

    for num in arr:
        if (K - num) in seen:
            return True
        seen.add(num)

    return False
```

---

## 3️⃣ Two Pointer Approach (Sorted Array)

### 💡 Idea

Sort the array and use two pointers from both ends.

### ⏱ Complexity

* Time: **O(n log n)** (sorting)
* Space: **O(1)** (if in-place sort)

### 💻 Code (Python)

```python
def has_pair_with_sum(arr, K):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == K:
            return True
        elif current_sum < K:
            left += 1
        else:
            right -= 1

    return False
```

---

## 📊 Complexity Comparison

| Approach     | Time Complexity | Space Complexity | Best Use Case  |
| ------------ | --------------- | ---------------- | -------------- |
| Brute Force  | O(n²)           | O(1)             | Small arrays   |
| Hashing      | O(n)            | O(n)             | Most efficient |
| Two Pointers | O(n log n)      | O(1)             | Sorted arrays  |

---

## 🧠 Key Insights

* Hashing is the most efficient general solution.
* Two-pointer works only after sorting.
* Brute force is simple but inefficient for large inputs.

---

## 🏁 Conclusion

This problem is a classic variation of the **Two Sum problem**, commonly asked in coding interviews.
Choosing the right approach depends on whether sorting is allowed and memory constraints.

---
