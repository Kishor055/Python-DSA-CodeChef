# **Running Comparison — README**

## **Problem Overview**

Alice and Bob recently started running and want to compare their performance over several days.

They each run for **N days**:

* On day *i*, Alice runs **A[i]** meters.
* Bob runs **B[i]** meters.

Their happiness rule for each day:

* **Alice is unhappy** if **Bob ran strictly more than twice** her distance → `B[i] > 2 * A[i]`
* **Bob is unhappy** if **Alice ran strictly more than twice** his distance → `A[i] > 2 * B[i]`
* Otherwise they are **happy**.

Your task is to determine **on how many days both Alice and Bob are happy**.

---

## **Input Format**

* First line: integer **T** — number of test cases
* For each test case:

  * A line with integer **N** — number of days
  * A line with **N** integers: distances run by Alice
  * A line with **N** integers: distances run by Bob

---

## **Output Format**

For each test case, output a single integer — the count of days on which **both Alice and Bob are happy**.

---

## **Constraints**

* `1 ≤ T ≤ 1000`
* `1 ≤ N ≤ 100`
* `1 ≤ A[i], B[i] ≤ 100000`

---

## **Happiness Conditions**

For each day `i`:

### Alice is Happy if:

```
B[i] ≤ 2 * A[i]
```

### Bob is Happy if:

```
A[i] ≤ 2 * B[i]
```

### Both Happy if **both** conditions hold:

```
B[i] ≤ 2 * A[i]  AND  A[i] ≤ 2 * B[i]
```

---

## **Sample Input**

```
4
3
100 200 300
300 200 100
4
1000 1000 1000 1000
400 500 600 1200
4
800 399 1400 532
2053 2300 3400 23
5
800 850 900 950 1000
600 800 1000 1200 1400
```

## **Sample Output**

```
1
3
0
5
```

---

## **Explanation (Test Case 1)**

* Day 1: Alice unhappy (`300 > 2×100`)
* Day 2: Both happy
* Day 3: Bob unhappy (`300 > 2×100`)

**Answer = 1 day**

