## ✅ Missing in Array — Python Solution

### 🧠 Idea

The array contains numbers from **1 to n**, but one number is missing.
We can use the **mathematical sum formula**:

![alt text](image.png)

Then subtract the sum of the given array.

---

## ⚙️ Efficient Approach (O(n))

```python
# User function Template for python3
class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1  # because one number is missing
        
        total_sum = n * (n + 1) // 2
        arr_sum = sum(arr)
        
        return total_sum - arr_sum
```

---

## 🚀 Alternative Approach (XOR Method)

### 🧠 Idea

XOR cancels identical numbers:

* `a ^ a = 0`
* `a ^ 0 = a`

So XOR all numbers from `1 to n` and XOR all elements of the array.

```python
class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1
        
        xor_all = 0
        xor_arr = 0
        
        for i in range(1, n + 1):
            xor_all ^= i
        
        for num in arr:
            xor_arr ^= num
        
        return xor_all ^ xor_arr
```

---

## ⏱ Complexity

| Method      | Time | Space |
| ----------- | ---- | ----- |
| Sum Formula | O(n) | O(1)  |
| XOR Method  | O(n) | O(1)  |

---

## 🏁 Summary

* Best simple solution → **Sum formula**
* Best bit manipulation solution → **XOR method**
* Both are optimal for constraints up to (10^6)

---