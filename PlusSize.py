"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2019/A -----------------------------------

You are given an array a1,a2,…,an of positive integers.

You can color some elements of the array red, but there cannot be two adjacent red elements (i.e., for 1≤i≤n−1, at least one of ai and ai+1 must not be red).

Your score is the maximum value of a red element plus the number of red elements. Find the maximum score you can get.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the length of the array.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 1000) — the given array.

Output
For each test case, output a single integer: the maximum possible score you can get after coloring some elements red according to the statement.

Input:
4
3
5 4 5
3
4 5 4
10
3 3 3 3 4 1 2 3 4 5
9
17 89 92 42 29 92 14 70 45

Output:
7
6
10
97
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempEvens = []
    evens = 0
    tempOdds = []
    odds = 0
    for i in range(sze):
        if(i % 2 == 0):
            tempEvens.append(arr[i])
            evens += 1
        else:
            tempOdds.append(arr[i])
            odds += 1
    
    tempSumEvens = (max(tempEvens) if tempEvens else 0) + evens
    tempSumOdds = (max(tempOdds) if tempOdds else 0) + odds
    print(max(tempSumEvens, tempSumOdds))