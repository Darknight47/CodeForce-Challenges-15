"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1739/A --------------------------------

There is a chess board of size n×m. The rows are numbered from 1 to n, the columns are numbered from 1 to m.

Let's call a cell isolated if a knight placed in that cell can't move to any other cell on the board. 
Recall that a chess knight moves two cells in one direction and one cell in a perpendicular direction:

Find any isolated cell on the board. If there are no such cells, print any cell on the board.

Input
The first line contains a single integer t (1 ≤ t ≤ 64) — the number of testcases.

The only line of each testcase contains two integers n and m (1 ≤ n , m ≤ 8) — the number of rows and columns of the board.

Output
For each testcase, print two integers — the row and the column of any isolated cell on the board. If there are no such cells, print any cell on the board.

Input:
3
1 7
8 8
3 3

Output:
1 7
7 2
2 2
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    temp1 = (n // 2) + 1
    temp2 = (m // 2) + 1
    print(temp1, temp2)