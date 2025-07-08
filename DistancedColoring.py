"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2002/A -------------------------------

You received an n×m grid from a mysterious source. The source also gave you a magic positive integer constant k.

The source told you to color the grid with some colors, satisfying the following condition:

If (x1,y1), (x2,y2) are two distinct cells with the same color, then max(|x1−x2|,|y1−y2|)≥k.
You don't like using too many colors. Please find the minimum number of colors needed to color the grid.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The only line of each test case consists of three positive integers n, m, k (1 ≤ n, m, k ≤ 10^4) — the dimensions of the grid and the magic constant.

Output
For each test case, print a single integer — the minimum number of colors needed to color the grid.

Input:
6
3 3 2
5 1 10000
7 3 4
3 2 7
8 9 6
2 5 4

Output:
4
5
12
6
36
8
"""
cases = int(input())
for _ in range(cases):
    n, m, k = map(int, input().split())
    temp1 = min(n, k)
    temp2 = min(m, k)
    print(temp1 * temp2)