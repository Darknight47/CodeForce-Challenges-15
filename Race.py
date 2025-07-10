"""
------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2112/A ------------------------------------------

Alice and Bob participate in a game TV show. When the game starts, the prize will be dropped to a certain point, and whoever gets to it first will get the prize.

Alice decided that she would start running from point a. Bob, however, has not yet chosen his starting position.

Bob knows that the prize could drop either at point x or at point y. 
He also knows that he can reach the prize faster than Alice if the distance from his starting position to the prize is strictly less than the distance from Alice's starting position to the prize. 
The distance between any two points c and d is calculated as |c−d|.

Your task is to determine whether Bob can choose an integer point that is guarantee to get to the prize faster, regardless of where it appears (at point x or y). 
Bob can choose any integer point, except for a (in particular, he can choose to start in point x, point y, or any other point, but not a).

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The only line of each test case contains three integers a, x, y (1 ≤ a, x, y ≤ 100). Points a, x, and y are pairwise distinct.

Output
For each test case, print "YES" (case insensitive) if Bob can choose an integer point that is guarantee to get to the prize faster, regardless of where it appears. Otherwise, print "NO" (case insensitive).

Input:
3
1 3 4
5 3 1
3 1 5

Output:
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    a, x, y = map(int, input().split())
    ok = False
    for b in range(min(a, x, y), max(a, x, y) + 1):
        if b == a:
            continue
        if abs(b - x) < abs(a - x) and abs(b - y) < abs(a - y):
            ok = True
            break
    print("YES" if ok else "NO")