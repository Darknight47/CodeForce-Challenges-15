"""
-------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1913/A ----------------------------

Monocarp is a great solver of adhoc problems. Recently, he participated in an Educational Codeforces Round, and gained rating!

Monocarp knew that, before the round, his rating was a. 
After the round, it increased to b (b > a). He wrote both values one after another to not forget them.

However, he wrote them so close to each other, that he can't tell now where the first value ends and the second value starts.

Please, help him find some values a and b such that:

neither of them has a leading zero;
both of them are strictly greater than 0;
b>a;
they produce the given value ab when written one after another.
If there are multiple answers, you can print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The only line of each testcase consists of a single string ab of length from 2 to 8 that:

consists only of digits;
doesn't start with a zero.

Output
For each testcase, determine if such values a and b exist. If they don't, print -1. Otherwise, print two integers a and b.

If there are multiple answers, you can print any of them.

Input:
5
20002001
391125
200200
2001000
12

Output:
2000 2001
39 1125
-1
200 1000
1 2
"""
cases = int(input())
for _ in range(cases):
    s = input()
    n = len(s)
    ok = False
    for i in range(1, n):
        first = s[:i]
        second = s[i:]
        if(second[0] == '0'):
            continue
        if(int(second) > int(first)):
            ok = True
            break
    if(ok):
        print(first, second)
    else:
        print(-1)