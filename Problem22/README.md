# **MIN To MAX – Problem README**

## **Problem Statement**

You are given an array **A** of size **N**.

Let **M** be the **minimum value** present in the array initially.

In one operation, you can choose an element
**A[i]** (1 ≤ i ≤ N) and an integer **X** (1 ≤ X ≤ 100), and set:

```
A[i] = X
```

Your task is to determine the **minimum number of operations** required to make **M** the **maximum value** in the array.

---

## **Input Format**

* The first line contains a single integer **T** — the number of test cases.
* Each test case has two lines:

  * First line: integer **N** — size of the array.
  * Second line: **N** space-separated integers — the array elements.

---

## **Output Format**

For each test case, print on a new line:

```
Minimum number of operations required to make M the maximum value.
```

---

## **Constraints**

```
1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ A[i] ≤ 100
```

---

## **Explanation**

Let **M = min(A)** initially.

To make **M** the **maximum**, every element **greater than M** must be changed to **M**.

Thus, the answer is simply:

```
Count of elements in A such that A[i] > M
```

---

## **Sample Input**

```
3
2
1 2
4
2 2 3 4
1
1
```

## **Sample Output**

```
1
2
0
```

## **Sample Explanation**

### Test Case 1:

A = [1, 2], M = 1
Only one element (2) is greater than 1 → **1 operation needed**

### Test Case 2:

A = [2, 2, 3, 4], M = 2
Elements greater than 2: (3, 4) → **2 operations**

### Test Case 3:

A = [1], M = 1
Already minimum and maximum → **0 operations**

---

## **Python Function (for reference)**

You can use this logic inside your required class method:

```python
class Solution:
    def count_non_minimum(self, nums):
        M = min(nums)
        return sum(1 for x in nums if x > M)
```

