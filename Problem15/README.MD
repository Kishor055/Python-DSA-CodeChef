Check Isomorphic Strings
You are given two strings, S and T. Determine whether these two strings are isomorphic.

Two strings are isomorphic if characters in S can be replaced to get T. All occurrences of a character must be replaced with another character while preserving the order. No two characters may map to the same character, but a character may map to itself.

Input Format
The first line contains an integer N, the number of test cases.
Each test case consists of two lines:
The first line contains the string S.
The second line contains the string T.

Output Format
For each test case, print "YES" if the strings are isomorphic, otherwise print "NO".

Constraints
1 ≤ |S| = |T| ≤ 10^5
S and T consist of ASCII characters.
1 ≤ N ≤ 100

Sample 1:
Input
2
mno
pqr
hello
world

Output
YES
NO

Explanation:
"mno" -> "pqr": mapping m->p, n->q, o->r YES
"hello" -> "world": 'l' maps to two different letters 'r' and 'l' NO

Sample 2:
Input
3
abcabc
xyzxyz
pqrpqr
mnopmn
abcd
abcc

Output
YES
NO
NO

Explanation:
"abcabc" -> "xyzxyz" YES
"pqrpqr" -> "mnopmn" NO
"abcd" -> "abcc" last character maps to two letters.
