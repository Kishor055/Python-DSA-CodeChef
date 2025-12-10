Check if the array is sorted
Given an array nums which is rotated k positions (k can be zero), return true if the original array was sorted before rotations else return false.

Rotation means that some suffix of the array is moved to the front. The suffix and the remaining elements of the array will remain in same order as before rotation. Duplicates are allowed in the array.

Note:
If A is the original sorted array and it is rotated right by k positions, the resulting array B satisfies:

B[(i+k)modA.length] = A[i]
for every valid index i.
1 2 3 4 5 is a sorted array and 2 3 4 5 1 is also a sorted array but after 4 rotations.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.

Each test case consists of multiple lines of input.

The first line of each test case contains a single integer N — the size of the array.
The second line of each test case contains N space-separated integers — the elements of the array nums.

Output Format
For each test case, output on a new line:

"true" if the array is sorted in non-decreasing order and then rotated any number of times (including zero).
"false" otherwise.

Constraints
1 ≤ nums.length ≤ 100
1 ≤ nums[i] ≤ 100

Sample 1:
Input
7
6 7 1 2 3 4 5

Output
true

Explanation:
The original sorted array was [1,2,3,4,5,6,7].
Rotating by k = 2 positions gives [6,7,1,2,3,4,5].

Sample 2:
Input
5
68 97 10 21 45

Output
true

Explanation:
The original sorted array [10,21,45,68,97] rotated by k = 2 results in [68,97,10,21,45].

Sample 3:
Input
5
4 5 2 3 1

Output
false

Explanation:
No rotation of a sorted array can produce this order.