# 📘 Array Search (Linear Search)

This module is part of the **Data Structures & Algorithms** repository and focuses on solving the **Array Search** problem using a simple and effective approach.

---

## 📌 Problem Statement

Given an array `arr[]` of `n` integers and an integer `x`, determine whether `x` exists in the array.

* Return the **index of the first occurrence** of `x`
* If `x` is not present, return `-1`

---

## 🧾 Examples

### Example 1

```
Input:
arr[] = [1, 2, 3, 4]
x = 3

Output:
2

Explanation:
Element 3 is found at index 2
```

---

### Example 2

```
Input:
arr[] = [10, 8, 30, 4, 5]
x = 5

Output:
4

Explanation:
Element 5 is present at index 4
```

---

### Example 3

```
Input:
arr[] = [10, 8, 30]
x = 6

Output:
-1

Explanation:
Element 6 is not present in the array
```

---

## ⚙️ Constraints

* `1 ≤ arr.size ≤ 10^6`
* `0 ≤ arr[i] ≤ 10^6`
* `0 ≤ x ≤ 10^5`

---

## 🚀 Approach: Linear Search

Since the array is **not necessarily sorted**, the most straightforward approach is **Linear Search**.

### 🔑 Key Idea

* Traverse the array from left to right
* Compare each element with `x`
* Return index immediately when found
* If traversal completes without finding `x`, return `-1`

---

## 💻 Implementation (Python)

```python
class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
```

---

## ⚡ Complexity Analysis

| Metric           | Value  |
| ---------------- | ------ |
| Time Complexity  | `O(n)` |
| Space Complexity | `O(1)` |

---

## 🧠 Key Concepts Covered

* Linear Search Algorithm
* Array Traversal
* First Occurrence Handling
* Time Complexity Basics

---

## 📂 Repository Structure

```
Data-Structure-Algorithms/
│
├── Arrays/
│   └── array_search.py
│
├── README.md
```

---

## 🧪 Edge Cases Considered

* Element present at first index
* Element present at last index
* Element not present
* Single element array
* Large input size (up to 10^6)

---

## 🛠️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Kishor055/Data-Structure-Algorithms.git
```

2. Navigate to the directory:

```bash
cd Data-Structure-Algorithms/Arrays
```

3. Run the script:

```bash
python array_search.py
```

---

## 🤝 Contributing

Contributions are welcome! You can:

* Add optimized approaches
* Improve documentation
* Include test cases

---

## ⭐ Support

If this repository helped you, consider giving it a ⭐ on GitHub!

---

## 📬 Contact

For any queries or suggestions, feel free to open an issue.

---

**Happy Coding! 🚀**