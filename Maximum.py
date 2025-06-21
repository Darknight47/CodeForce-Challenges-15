"""
-------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1979/A ------------------------------

Alice and Bob came up with a rather strange game. They have an array of integers a1,a2,…,an.
Alice chooses a certain integer k and tells it to Bob, then the following happens:

Bob chooses two integers i and j (1 ≤ i < j ≤ n), and then finds the maximum among the integers ai,ai+1,…,aj;
If the obtained maximum is strictly greater than k, Alice wins, otherwise Bob wins.
Help Alice find the maximum k at which she is guaranteed to win.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 5⋅10^4) — the number of elements in the array.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of the array.

It is guaranteed that the sum of n over all test cases does not exceed 5⋅10^4.

Output
For each test case, output one integer — the maximum integer k at which Alice is guaranteed to win.

Input:
6
4
2 4 1 7
5
1 2 3 4 5
2
1 1
3
37 8 16
5
10 10 10 10 9
10
3 12 9 5 2 3 2 9 8 2

Output:
3
1
0
15
9
2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = max(arr[0], arr[1])
    for i in range(1, sze - 1):
        maxNum = max(arr[i], arr[i + 1])
        ans = min(ans, maxNum)
    print(ans - 1)