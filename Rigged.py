"""
------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1879/A --------------------------------------

Monocarp organizes a weightlifting competition. There are n athletes participating in the competition, the i-th athlete has strength si and endurance ei. 
The 1-st athlete is Monocarp's friend Polycarp, and Monocarp really wants Polycarp to win.

The competition will be conducted as follows. The jury will choose a positive (greater than zero) integer w, which denotes the weight of the barbell that will be used in the competition. 
The goal for each athlete is to lift the barbell as many times as possible. 
The athlete who lifts the barbell the most amount of times will be declared the winner (if there are multiple such athletes — there's no winner).

If the barbell's weight w is strictly greater than the strength of the i-th athlete si, then the i-th athlete will be unable to lift the barbell even one single time. 
Otherwise, the i-th athlete will be able to lift the barbell, and the number of times he does it will be equal to his endurance ei.

For example, suppose there are 4 athletes with parameters s1=7,e1=4; s2=9,e2=3; s3=4,e3=6; s4=2,e4=2. 
If the weight of the barbell is 5, then:

the first athlete will be able to lift the barbell 4 times;
the second athlete will be able to lift the barbell 3 times;
the third athlete will be unable to lift the barbell;
the fourth athlete will be unable to lift the barbell.

Monocarp wants to choose win such a way that Polycarp (the 1-st athlete) wins the competition. Help him to choose the value of w, or report that it is impossible.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains one integer n (2 ≤ n ≤ 100) — the number of athletes. 
Then n lines follow, the i-th of them contains two integers si and ei (1 ≤ si ≤ 10^9; 1 ≤ ei ≤ 100) — the strength and the endurance of the i-th athlete.

Output
For each test case, print the answer as follows:

if the answer exists, print one integer — the value of w meeting the constraints. 
The integer you print should satisfy 1 ≤ w ≤ 10^9. It can be shown that if the answer exists, at least one such value of w exists as well. If there are multiple answers, you can print any of them;
otherwise, print one integer −1.

Input:
3
4
7 4
9 3
4 6
2 2
2
4 6
100 100
2
1337 3
1337 3

Output:
5
-1
-1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s1, x1 = map(int, input().split())
    ok = True
    for _ in range(sze - 1):
        sTemp, xTemp = map(int, input().split())
        if(sTemp >= s1 and xTemp >= x1):
            ok = False
    print(s1 if ok else -1)