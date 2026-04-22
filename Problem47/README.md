# 📘 First Occurrence in Sorted Array (Binary Search)

This module is part of the **Data Structures & Algorithms** repository and demonstrates an efficient way to find the **first occurrence of a given element** in a sorted array using **Binary Search**.

---

## 📌 Problem Statement

Given a **sorted array** `arr[]` and an integer `k`, determine the **first (smallest index) occurrence** of `k` in the array.

* Return the index using **0-based indexing**
* If the element is not found, return `-1`

> ⚠️ If multiple occurrences exist, return the **leftmost (first) index**

---

## 🧾 Examples

### Example 1

```
Input:
arr[] = [1, 2, 3, 4, 5]
k = 4

Output:
3

Explanation:
Element 4 is present at index 3
```

---

### Example 2

```
Input:
arr[] = [11, 22, 33, 44, 55]
k = 445

Output:
-1

Explanation:
Element not found in the array
```

---

### Example 3

```
Input:
arr[] = [1, 1, 1, 1, 2]
k = 1

Output:
0

Explanation:
First occurrence of 1 is at index 0
```

---

## ⚙️ Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^6`
* `1 ≤ k ≤ 10^6`

---

## 🚀 Approach: Modified Binary Search

Since the array is **sorted**, Binary Search is the most efficient approach.

### 🔑 Key Idea

* When `arr[mid] == k`, **do not stop**
* Store the index and **continue searching on the left side**
* This ensures we find the **first occurrence**

---

## 💻 Implementation (Python)

```python
class Solution:
    def firstOccurrence(self, arr, k):
        low, high = 0, len(arr) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                ans = mid
                high = mid - 1   # search left half
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
```

---

## ⚡ Complexity Analysis

| Metric           | Value      |
| ---------------- | ---------- |
| Time Complexity  | `O(log n)` |
| Space Complexity | `O(1)`     |

---

## 🧠 Key Concepts Covered

* Binary Search
* Searching in Sorted Arrays
* Edge Case Handling
* Time Complexity Optimization

---

## 📂 Repository Structure

```
Data-Structure-Algorithms/
│
├── Searching/
│   └── first_occurrence.py
│
├── README.md
```

---

## 🧪 Edge Cases Considered

* Element not present in array
* Array with all identical elements
* Single element array
* Large input size (up to 10^5)

---

## 🛠️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Kishor055/Data-Structure-Algorithms.git
```

2. Navigate to the folder:

```bash
cd Data-Structure-Algorithms/Searching
```

3. Run the script:

```bash
python first_occurrence.py
```

---

## 🤝 Contributing

Contributions are welcome! You can:

* Add alternative approaches
* Optimize the solution further
* Improve documentation

---

## ⭐ Support

If this project helped you, consider giving it a ⭐ on GitHub!

---

## 📬 Contact

For queries or suggestions, feel free to open an issue or connect via GitHub.

---

**Happy Coding! 🚀**
