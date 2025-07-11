"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1838/A ----------------------------------

Two integers were written on a blackboard. After that, the following step was carried out n−2 times:

Select any two integers on the board, and write the absolute value of their difference on the board.
After this process was complete, the list of n integers was shuffled. You are given the final list. 
Recover one of the initial two numbers. You do not need to recover the other one.

You are guaranteed that the input can be generated using the above process.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 10^0) — the size of the final list.

The next line of each test case contains n integers a1,a2,…an (−10^9 ≤ a(i) ≤ 10^9) — the shuffled list of numbers written on the blackboard.

It is guaranteed that the input was generated using the process described above.

Output
For each test case, output a single integer x — one of the two initial numbers on the blackboard.

If there are multiple solutions, print any of them.

Input:
9
3
9 2 7
3
15 -4 11
4
-9 1 11 -10
5
3 0 0 0 3
7
8 16 8 0 8 16 8
4
0 0 0 0
10
27 1 24 28 2 -1 26 25 28 27
6
600000000 800000000 0 -200000000 1000000000 800000000
3
0 -1000000000 1000000000

Output:
9
11
-9
3
8
0
-1
600000000
0
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    if(arr[0] < 0):
        print(arr[0])
    else:
        temp = max(arr)
        print(temp)