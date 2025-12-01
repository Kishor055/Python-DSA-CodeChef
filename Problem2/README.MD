# Find Maximum in an Array

## Problem Statement

Given a list of `N` integers representing the height of mountains, your task is to find the height of the tallest mountain in the list.

## Input Format

* The first line contains an integer `T`, the number of test cases.
* For each test case:

  * The first line contains an integer `N`, the number of mountains.
  * The second line contains `N` space-separated integers, representing the height of each mountain.

## Output Format

For each test case, output a single line containing one integer — the height of the tallest mountain.

## Constraints

* ( 1 \le T \le 10 )
* ( 1 \le N \le 100,000 )
* ( 0 \le \text{height of each mountain} \le 10^9 )

## Sample Input

```
1
5
4 7 6 3 1
```

## Sample Output

```
7
```

## Explanation

* There is only one test case.
* Heights of mountains: `[4, 7, 6, 3, 1]`
* The tallest mountain has a height of `7`.

## Approach

1. For each test case, read the number of mountains `N`.
2. Read the heights of the mountains into a list.
3. Use a simple linear scan to find the maximum height.
4. Print the maximum height for each test case.

## Python Example

```python
T = int(input())
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    print(max(heights))
```

---

I can also create a **more detailed README** with **time complexity and explanation of the algorithm** if you want.

Do you want me to do that?
