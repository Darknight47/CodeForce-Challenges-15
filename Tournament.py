"""
------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2123/B -----------------------------

You are given an array of integers a1,a2,…,an. A tournament is held with n players. Player i has strength ai.

While more than k players remain,

Two remaining players are chosen at random;
Then the chosen player with the lower strength is eliminated. If the chosen players have the same strength, one is eliminated at random.
Given integers j and k (1 ≤ j , k ≤ n), 
determine if there is any way for player j to be one of the last k remaining players.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4)  — the number of test cases.

The first line of each test case contains three integers n, j, and k (2 ≤ n ≤ 2⋅10^5, 1≤j,k≤n).

The second line of each test case contains n integers, a1,a2,…,an (1 ≤ ai ≤ n).

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output on a single line "YES" if player j can be one of the last k remaining players, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
3
5 2 3
3 2 4 4 1
5 4 1
5 3 4 5 2
6 1 1
1 2 3 4 5 6

Output:
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n, j, k = map(int, input().split())
    arr = list(map(int, input().split()))
    tempPlayer = arr[j - 1]
    tempMax = max(arr)
    if(k > 1 or tempPlayer == tempMax):
        print("YES")
    else:
        print("NO")