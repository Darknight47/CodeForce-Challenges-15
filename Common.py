"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2103/A -------------------------------------

You are given an array of integers a1,a2,…,an. 
An array x1,x2,…,xm is beautiful if there exists an array y1,y2,…,ym such that the elements of y are distinct (in other words, yi≠yj for all 1 ≤ i < j ≤ m), 
and the product of xi and y(i) is the same for all 1≤i≤m (in other words, xi⋅yi=xj⋅yj for all 1 ≤ i < j ≤ m).

Your task is to determine the maximum size of a subsequence∗ of array a that is beautiful.

∗ A sequence b is a subsequence of a sequence a if b can be obtained from a by the deletion of several (possibly, zero or all) element from arbitrary positions.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ n) — the elements of array a.

Note that there are no constraints on the sum of n over all test cases.

Output
For each test case, output the maximum size of a subsequence of array a that is beautiful.

Input:
3
3
1 2 3
5
3 1 4 1 5
1
1

Output:
3
4
1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    tempSet = set(map(int, input().split()))
    print(len(tempSet))