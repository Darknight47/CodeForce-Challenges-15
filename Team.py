"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2091/B --------------------------------

At the IT Campus "NEIMARK", there are training sessions in competitive programming — both individual and team-based!

For the next team training session, n students will attend, and the skill of the i-th student is given by a positive integer a(i).

The coach considers a team strong if its strength is at least x. 
The strength of a team is calculated as the number of team members multiplied by the minimum skill among the team members.

For example, if a team consists of 4 members with skills [5,3,6,8], then the team's strength is 4⋅min([5,3,6,8])=12.

Output the maximum possible number of strong teams, given that each team must have at least one participant and every participant must belong to exactly one team.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains two integers n and x (1 ≤ n ≤ 2⋅10^5, 1 ≤ x ≤ 10^9) — the number of students in training and the minimum strength of a team to be considered strong.

The second line of each test case contains n integers a(i) (1 ≤ a(i) ≤ 10^9) — the skill of each student.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output the maximum possible number of teams with strength at least x.

Input:
5
6 4
4 5 3 3 2 6
4 10
4 2 1 3
5 3
5 3 2 3 2
3 6
9 1 7
6 10
6 1 3 6 3 2

Output:
4
0
4
2
1
"""
cases = int(input())
for _ in range(cases):
    sze, x = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    tempArr = []
    ans = 0
    for i in range(sze - 1, -1, -1):
        num = arr[i]
        tempArr.append(num)
        tempMin = min(tempArr)
        tempStrength = len(tempArr) * tempMin
        if(tempStrength >= x):
            ans += 1
            tempArr = []
    print(ans)