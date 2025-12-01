
# Longest Common Prefix

## Problem Statement

You are given N strings. Your task is to find the longest common prefix among all these strings.

If there is no common prefix, print an empty string ("").

## Input Format

The first line contains an integer N, the number of strings.

The next N lines each contain one string S[i].

## Output Format

Print the longest common prefix among all strings.

If no common prefix exists, print an empty string ("").

## Constraints

* 1 ≤ N ≤ 200
* 0 ≤ |S[i]| ≤ 200
* Each string consists of lowercase English letters only.

## Sample 1

**Input:**

```
4
interview
internet
internal
interval
```

**Output:**

```
inter
```

**Explanation:**
All strings start with "inter", which is the longest common prefix.

## Sample 2

**Input:**

```
3
apple
ape
april
```

**Output:**

```
ap
```

**Explanation:**
All strings start with "ap" — that’s the longest common prefix.

