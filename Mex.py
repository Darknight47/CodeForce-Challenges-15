"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2057/A ---------------------------------

One day, the schoolboy Mark misbehaved, so the teacher Sasha called him to the whiteboard.

Sasha gave Mark a table with n rows and m columns. His task is to arrange the numbers 0,1,…,n⋅m−1 in the table 
(each number must be used exactly once) in such a way as to maximize the sum of MEX∗ across all rows and columns. More formally, he needs to maximize.

Sasha is not interested in how Mark arranges the numbers, so he only asks him to state one number — the maximum sum of MEX across all rows and columns that can be achieved.

Input
Each test contains multiple test cases. The first line contains a single integer t
(1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n and m (1 ≤ n, m ≤ 10^9) — the number of rows and columns in the table, respectively.

Output
For each test case, output the maximum possible sum of mex across all rows and columns.

Input:
3
1 1
2 2
3 5

Output:
2
3
6
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    print(max(a, b) + 1)