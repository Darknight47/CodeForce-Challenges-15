"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2121/A -------------------------------

You are given an array of distinct integers x1,x2,…,xn and an integer s.

Initially, you are at position pos=s on the X axis. In one step, you can perform exactly one of the following two actions:

Move from position pos to position pos+1.
Move from position pos to position pos−1.
A sequence of steps will be considered successful if, during the entire journey, you visit each position xi on the X axis at least once. 
Note that the initial position pos=s is also considered visited.

Your task is to determine the minimum number of steps in any successful sequence of steps.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n and s (1 ≤ n ≤ 10, 1 ≤ s ≤ 100) — the number of positions to visit and the starting position.

The second line of each test case contains n integers x1,x2,…,xn (1≤xi≤100). 
It is guaranteed that for all 1≤i<n, it holds that xi<xi+1.

Output
For each test case, output the minimum number of steps in any successful sequence of steps.

Input:
12
1 1
1
1 2
1
1 1
2
2 1
2 3
2 2
1 3
2 3
1 2
3 1
1 2 3
3 2
1 3 4
3 3
1 2 3
4 3
1 2 3 10
5 5
1 2 3 6 7
6 6
1 2 3 9 10 11

Output:
0
1
1
2
3
2
2
4
2
11
8
15
"""
cases = int(input())
for _ in range(cases):
    toVisits, startPos = map(int, input().split())
    arr = list(map(int, input().split()))
    fromLeftSide = 0
    fromRightSide = 0
    if(startPos > arr[toVisits - 1]):
        fromRightSide = startPos - arr[0]
    elif(startPos < arr[0]):
        fromLeftSide = arr[toVisits - 1] - startPos
    else:
        fromLeftSide = abs(arr[0] - startPos)
        fromRightSide = abs(arr[len(arr) - 1] - startPos)
    tempMin = min(fromLeftSide, fromRightSide) * 2
    tempMax = max(fromLeftSide, fromRightSide)
    ans = tempMin + tempMax
    print(ans)