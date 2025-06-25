"""
---------------------- Link for the challenge: https://codeforces.com/problemset/problem/1834/A ----------------------------

Given an array a of length n, which elements are equal to −1 and 1. 
Let's call the array a good if the following conditions are held at the same time:

a1+a2+…+an≥0;
a1⋅a2⋅…⋅an=1.

In one operation, you can select an arbitrary element of the array ai and change its value to the opposite. In other words, if ai=−1, you can assign the value to ai:=1, and if ai=1, then assign the value to ai:=−1.

Determine the minimum number of operations you need to perform to make the array a good. It can be shown that this is always possible.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (ai=±1) — the elements of the array a.

Output
For each test case, output a single integer — the minimum number of operations that need to be done to make the a array good.

Input:
7
4
-1 -1 1 -1
5
-1 -1 -1 1 1
4
-1 1 -1 1
3
-1 -1 -1
5
1 1 1 1 1
1
-1
2
-1 -1

Output:
1
1
0
3
0
1
2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    minus = arr.count(-1)
    ans = 0

    # Step 1: Make the sum ≥ 0
    while (sze - 2 * minus) < 0:
        minus -= 1
        ans += 1
    # Step 2: Make the product = 1 (even number of -1s)
    if minus % 2 == 1:
        ans += 1
    print(ans)