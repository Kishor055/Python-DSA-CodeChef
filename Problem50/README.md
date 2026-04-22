# 📘 Equilibrium Point in Array

This module is part of the **Data Structures & Algorithms (DSA)** repository and focuses on finding the **first equilibrium point** in an array using an optimized approach.

---

## 📌 Problem Statement

Given an array `arr[]`, find the **first equilibrium index**.

An index is called an **equilibrium point** if:

> Sum of elements on the **left side** == Sum of elements on the **right side**

* Indexing is **0-based**
* If no equilibrium point exists, return `-1`

---

## 🧾 Examples

### Example 1

```id="ex1"
Input:
arr[] = [1, 2, 0, 3]

Output:
2

Explanation:
Left sum = 1 + 2 = 3  
Right sum = 3  
```

---

### Example 2

```id="ex2"
Input:
arr[] = [1, 1, 1, 1]

Output:
-1

Explanation:
No index satisfies left sum = right sum
```

---

### Example 3

```id="ex3"
Input:
arr[] = [-7, 1, 5, 2, -4, 3, 0]

Output:
3

Explanation:
Left sum = -7 + 1 + 5 = -1  
Right sum = -4 + 3 + 0 = -1
```

---

## ⚙️ Constraints

* `3 ≤ arr.size() ≤ 10^5`
* `-10^4 ≤ arr[i] ≤ 10^4`

---

## 🚀 Approach: Prefix Sum Optimization

### 💡 Idea

Instead of recalculating left and right sums every time:

1. Compute total sum of array
2. Maintain a running **left sum**
3. At each index:

   * Right sum = total sum − left sum − current element
4. Check condition:

   * If `left_sum == right_sum` → return index

---

## 💻 Implementation (Python)

```python id="code1"
class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            total_sum -= arr[i]  # right sum
        
            if left_sum == total_sum:
                return i
        
            left_sum += arr[i]
        
        return -1
```

---

## ⚡ Complexity Analysis

| Metric           | Value |
| ---------------- | ----- |
| Time Complexity  | O(n)  |
| Space Complexity | O(1)  |

---

## 🧠 Key Concepts Covered

* Prefix Sum Technique
* Array Traversal Optimization
* Running Sum Logic
* Time Complexity Reduction

---

## 📂 Repository Structure

```id="structure"
Data-Structure-Algorithms/
│
├── Arrays/
│   └── equilibrium_point.py
│
├── README.md
```

---

## 🧪 Edge Cases

* No equilibrium point exists
* Equilibrium at first or last index
* Negative numbers in array
* Single valid equilibrium point
* Large input size (10^5 elements)

---

## 🛠️ How to Run

1. Clone repository:

```bash id="clone"
git clone https://github.com/Kishor055/Data-Structure-Algorithms.git
```

2. Navigate to folder:

```bash id="cd"
cd Data-Structure-Algorithms/Arrays
```

3. Run file:

```bash id="run"
python equilibrium_point.py
```

---

## 🤝 Contributing

Contributions are welcome:

* Add alternative approaches (brute force, prefix array)
* Improve optimization techniques
* Add test cases

---

## ⭐ Support

If this project helped you, please ⭐ the repository.

---

## 📬 Contact

For queries or suggestions, feel free to open an issue on GitHub.

---

**Happy Coding! 🚀**
