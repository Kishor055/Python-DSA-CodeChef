# 📘 Missing and Repeating Number

This module is part of the **Data Structures & Algorithms** repository and focuses on solving the classic problem of identifying the **missing** and **repeating** numbers in an array.

---

## 📌 Problem Statement

Given an **unsorted array** `arr[]` of size `n`, containing numbers from `1` to `n`:

* One number is **missing**
* One number is **repeated (occurs twice)**

Your task is to find both numbers.

### 🔁 Return Format

Return a list:

```
[repeating, missing]
```

---

## 🧾 Examples

### Example 1

```id="ex1"
Input:
arr[] = [2, 2]

Output:
[2, 1]

Explanation:
Repeating number = 2  
Missing number = 1
```

---

### Example 2

```id="ex2"
Input:
arr[] = [1, 3, 3]

Output:
[3, 2]

Explanation:
Repeating number = 3  
Missing number = 2
```

---

### Example 3

```id="ex3"
Input:
arr[] = [4, 3, 6, 2, 1, 1]

Output:
[1, 5]

Explanation:
Repeating number = 1  
Missing number = 5
```

---

## ⚙️ Constraints

* `2 ≤ n ≤ 10^6`
* `1 ≤ arr[i] ≤ n`

---

## 🚀 Approaches

### 1. Mathematical Approach (Optimal)

#### 💡 Idea

Use formulas for:

* Sum of first `n` natural numbers
* Sum of squares of first `n` natural numbers

#### Key Equations

* `S - Sn = repeating - missing`
* `S2 - S2n = repeating² - missing²`

Solve these equations to get both values.

---

### 💻 Implementation (Python)

```python id="math-solution"
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        Sn = n * (n + 1) // 2
        S2n = n * (n + 1) * (2 * n + 1) // 6
        
        S = sum(arr)
        S2 = sum(x * x for x in arr)
        
        diff = S - Sn
        diff_sq = S2 - S2n
        
        sum_xy = diff_sq // diff
        
        repeating = (diff + sum_xy) // 2
        missing = repeating - diff
        
        return [repeating, missing]
```

---

### ⚡ Complexity

| Metric           | Value  |
| ---------------- | ------ |
| Time Complexity  | `O(n)` |
| Space Complexity | `O(1)` |

---

## 🧠 Alternative Approach (Hashing)

### 💡 Idea

* Use a frequency array to count occurrences
* Identify:

  * Element with frequency `2` → repeating
  * Element with frequency `0` → missing

```python id="hash-solution"
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        freq = [0] * (n + 1)
        
        repeating = missing = -1
        
        for num in arr:
            freq[num] += 1
        
        for i in range(1, n + 1):
            if freq[i] == 2:
                repeating = i
            elif freq[i] == 0:
                missing = i
        
        return [repeating, missing]
```

---

## 🧠 Key Concepts Covered

* Mathematical Derivation
* Array Traversal
* Hashing Technique
* Optimization (Time & Space)

---

## 📂 Repository Structure

```id="structure"
Data-Structure-Algorithms/
│
├── Arrays/
│   └── missing_and_repeating.py
│
├── README.md
```

---

## 🧪 Edge Cases Considered

* Smallest input size (`n = 2`)
* Repeating number at start/end
* Missing number at boundaries (1 or n)
* Large input size (up to 10^6)

---

## 🛠️ How to Run

1. Clone the repository:

```bash id="clone"
git clone https://github.com/Kishor055/Data-Structure-Algorithms.git
```

2. Navigate to the directory:

```bash id="cd"
cd Data-Structure-Algorithms/Arrays
```

3. Run the script:

```bash id="run"
python missing_and_repeating.py
```

---

## 🤝 Contributing

Contributions are welcome! You can:

* Add optimized approaches (e.g., XOR method)
* Improve code readability
* Add test cases

---

## ⭐ Support

If you found this helpful, consider giving a ⭐ to the repository!

---

## 📬 Contact

For queries or suggestions, feel free to open an issue on GitHub.

---

**Happy Coding! 🚀**