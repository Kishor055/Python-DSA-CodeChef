# 📘 Kth Smallest Element – Data Structures & Algorithms

This repository is part of the **Data Structures & Algorithms** collection and focuses on solving the classic **Kth Smallest Element** problem efficiently using different approaches.

---

## 📌 Problem Statement

Given an integer array `arr[]` and an integer `k`, your task is to find and return the **kth smallest element** in the array.

> ⚠️ The kth smallest element is determined based on the **sorted order** of the array (not distinct elements).

---

## 🧾 Examples

### Example 1

```
Input:
arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

Output:
5

Explanation:
Sorted array → [2, 3, 4, 5, 6, 10, 10, 33, 48, 53]
4th smallest element = 5
```

### Example 2

```
Input:
arr[] = [7, 10, 4, 3, 20, 15]
k = 3

Output:
7

Explanation:
Sorted array → [3, 4, 7, 10, 15, 20]
3rd smallest element = 7
```

---

## ⚙️ Constraints

* `1 ≤ arr.size() ≤ 10^5`
* `1 ≤ arr[i] ≤ 10^5`
* `1 ≤ k ≤ arr.size()`

---

## 🚀 Approaches

### 1. Sorting Approach (Simple)

* Sort the array
* Return element at index `k-1`

**Time Complexity:** `O(n log n)`
**Space Complexity:** `O(1)` (in-place sort)

---

### 2. Min Heap Approach

* Build a min heap
* Extract the smallest element `k` times

**Time Complexity:** `O(n + k log n)`
**Space Complexity:** `O(n)`

---

### 3. Max Heap (Optimized for Large n)

* Maintain a max heap of size `k`
* Keep only the smallest `k` elements

**Time Complexity:** `O(n log k)`
**Space Complexity:** `O(k)`

---

### 4. Quick Select Algorithm (Best Average Case)

* Partition-based selection (similar to QuickSort)
* Efficient for large datasets

**Time Complexity:**

* Average: `O(n)`
* Worst: `O(n²)`

**Space Complexity:** `O(1)`

---

## 💻 Python Implementation

```python
class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k - 1]
```

---

## 🧠 Key Concepts Covered

* Sorting Algorithms
* Heap Data Structure (Min Heap / Max Heap)
* Divide and Conquer (Quick Select)
* Time & Space Complexity Optimization

---

## 📂 Repository Structure

```
Data-Structure-Algorithms/
│
├── Arrays/
│   └── kth_smallest.py
│
├── README.md
```

---

## 📈 Use Cases

* Data Analysis (finding order statistics)
* Competitive Programming
* Interview Preparation
* Real-time ranking systems

---

## 🛠️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Kishor055/Data-Structure-Algorithms.git
```

2. Navigate to the directory:

```bash
cd Data-Structure-Algorithms
```

3. Run the Python file:

```bash
python kth_smallest.py
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Improve existing solutions
* Add new optimized approaches
* Fix bugs or enhance documentation

---

## ⭐ Support

If you find this repository helpful, consider giving it a ⭐ on GitHub!

---

## 📬 Contact

For any queries or suggestions, feel free to reach out via GitHub.

---

**Happy Coding! 🚀**
