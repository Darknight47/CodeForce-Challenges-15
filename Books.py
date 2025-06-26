"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1978/A -----------------------------

Alice has n books. The 1-st book contains a1 pages, the 2-nd book contains a2 pages, …, the n-th book contains an pages. Alice does the following:

She divides all the books into two non-empty piles. Thus, each book ends up in exactly one of the two piles.
Alice reads one book with the highest number in each pile.
Alice loves reading very much. Help her find the maximum total number of pages she can read by dividing the books into two piles.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the number of books Alice has.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the number of pages in each book.

Output
For each test case, output a single integer — the maximum number of pages Alice can read.

Input:
5
2
1 1
4
2 3 3 1
5
2 2 3 2 2
2
10 3
3
1 2 3

Output:
2
4
5
13
5
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    last = arr.pop()
    maxNum = max(arr)
    print(last + maxNum)