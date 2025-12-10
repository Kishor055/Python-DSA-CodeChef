
# **Largest and Second Largest**

## **📝 Problem Overview**

You are given an array **A** of **N integers**.
Your task is to determine the **maximum possible sum** of **two distinct integers** in the array.

It is guaranteed that the array contains **at least two distinct values**.

---

## **📥 Input Format**

* The first line contains an integer **T** — number of test cases.
* Each test case consists of:

  * An integer **N** — size of the array.
  * A line with **N space-separated integers** — the elements of the array **A**.

---

## **📤 Output Format**

For each test case, print the **maximum sum of two distinct integers** on a new line.

---

## **✅ Constraints**

* (1 \leq T \leq 1000)
* (2 \leq N \leq 10^5)
* (1 \leq A_i \leq 1000)
* The sum of all **N** across test cases ≤ (2 \times 10^5)

---

## **💡 Key Idea**

To get the maximum sum of two distinct values, simply find:

* The **largest** value in the array.
* The **second-largest distinct** value.

The answer is:
[
\text{max1} + \text{max2}
]

This can be computed efficiently in **O(N)** per test case.

---

## **🧪 Sample Input**

```
4
3
4 1 6
7
3 7 2 1 1 5 3
5
8 2 9 4 9
2
1 2
```

## **🧾 Sample Output**

```
10
12
17
3
```

---

## **📘 Explanation**

**Test Case 1:**
Distinct values → {1, 4, 6}
Largest two → 6 and 4 → **6 + 4 = 10**

**Test Case 2:**
Distinct values → {1, 2, 3, 5, 7}
Largest two → 7 and 5 → **7 + 5 = 12**

**Test Case 3:**
Distinct values → {2, 4, 8, 9}
Largest two → 9 and 8 → **9 + 8 = 17**

**Test Case 4:**
Distinct values → {1, 2}
Two largest → **2 + 1 = 3**

