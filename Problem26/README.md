# 📘 Difficulty Rating Order

This problem checks whether students solved coding problems in **non-decreasing order of difficulty**.

A sequence is **non-decreasing** if each element is **greater than or equal to** the previous one.
If at any point a later problem has a **lower** difficulty than a previous one, the order is incorrect.

---

## ✅ Problem Description

Our Chef wants to ensure students are practicing problems properly.
Given the list of problem difficulties solved **in order**, determine whether they are solved in **non-decreasing order**.

A student should **not** solve a problem with difficulty `d1` and then later solve a problem with difficulty `d2` such that:

```
d2 < d1
```

---

## 📝 Input Format

* The first line contains an integer **T** — number of test cases.
* Each test case contains:

  * An integer **N** — number of problems solved.
  * A line of **N space-separated integers** representing the difficulty levels.

---

## 🖨 Output Format

For each test case, print:

* `"Yes"` — if the sequence is non-decreasing
* `"No"` — if the sequence ever decreases

Output is case-insensitive (`YES`, `yes`, `YeS` are all valid).

---

## 🔒 Constraints

* (1 \leq T \leq 100)
* (2 \leq N \leq 100)
* (1 \leq \text{difficulty} \leq 5000)

---

## 📌 Example

### **Input**

```
4
3
1 2 3
3
1 1 2
5
100 200 300 400 350
5
1000 2000 5000 3000 1000
```

### **Output**

```
Yes
Yes
No
No
```

---

## 🧠 Explanation

### Test case 1

`1 ≤ 2 ≤ 3` → Non-decreasing → **Yes**

### Test case 2

`1 ≤ 1 ≤ 2` → Non-decreasing (equal allowed) → **Yes**

### Test case 3

`400 > 350` → Decrease detected → **No**

### Test case 4

`5000 > 3000` → Decrease detected → **No**

---

## 🚀 Approach

* Traverse the list of difficulties.
* Compare each element to the previous one.
* If any element is smaller than the previous one → print `"No"`.
* Else, after checking all → print `"Yes"`.

