"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1989/A ---------------------------

Monocarp visited a retro arcade club with arcade cabinets. There got curious about the "Catch the Coin" cabinet.

The game is pretty simple. The screen represents a coordinate grid such that:

the X-axis is directed from left to right;
the Y-axis is directed from bottom to top;
the center of the screen has coordinates (0,0).

At the beginning of the game, the character is located in the center, and n coins appear on the screen — the i-th coin is at coordinates (xi,yi). 
The coordinates of all coins are different and not equal to (0,0).

In one second, Monocarp can move the character in one of eight directions. If the character is at coordinates (x,y)
, then it can end up at any of the coordinates (x,y+1), (x+1,y+1), (x+1,y), (x+1,y−1), (x,y−1), (x−1,y−1), (x−1,y), (x−1,y+1).

If the character ends up at the coordinates with a coin, then Monocarp collects that coin.

After Monocarp makes a move, all coins fall down by 1, that is, they move from (x,y) to (x,y−1). 
You can assume that the game field is infinite in all directions.

Monocarp wants to collect at least one coin, but cannot decide which coin to go for. Help him determine, for each coin, whether he can collect it.

Input
The first line contains a single integer n (1 ≤ n ≤ 500) — the number of coins.

In the i-th of the next n lines, two integers xi and yi (−50 ≤ x(i), y(i) ≤ 50) are written — 
the coordinates of the i-th coin. The coordinates of all coins are different. No coin is located at (0,0).

Output
For each coin, print "YES" if Monocarp can collect it. Otherwise, print "NO".

Input:
5
24 42
-2 -1
-1 -2
0 -50
15 0

Output:
YES
YES
NO
NO
YES
"""
cases = int(input())
for _ in range(cases):
    x, y = map(int, input().split())
    if(y >= -1):
        print("YES")
    else:
        print("NO")