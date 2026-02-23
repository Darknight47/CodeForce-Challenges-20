"""

----------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1999/B ------------------------------------------

Suneet and Slavic play a card game. The rules of the game are as follows:

Each card has an integer value between 1 and 10.
Each player receives 2 cards which are face-down (so a player doesn't know their cards).
The game is turn-based and consists exactly of two turns. In a round, both players pick a random unflipped card and flip it. 
The player who flipped a card with a strictly greater number wins the round. In case of equality, no one wins the round.
A player wins a game if he wins the most number of rounds (i.e. strictly greater than the other player). In case of equality, no one wins the game.
Since Suneet and Slavic aren't best friends, you need to calculate the number of ways the game could happen that Suneet would end up as the winner.

For a better understanding, please check the notes section.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first and only line of each test case contains 4 integers a1, a2, b1, b2 (1 ≤ a1, a2, b1, b2 ≤ 10) where a1 and a2 represent the cards Suneet has, and b1 and b2 represent the cards Slavic has, respectively.

Output
For each test case, output a single integer — the number of games Suneet would win considering all possible games.

Input:
5
3 8 2 6
1 1 1 1
10 10 2 2
1 1 10 10
3 8 7 2

Output:
2
0
4
0
2
"""
cases = int(input())
for _ in range(cases):
    a1, a2, b1, b2 = map(int, input().split())
    
    suneet_orders = [(a1, a2), (a2, a1)]
    slavic_orders = [(b1, b2), (b2, b1)]
    
    ways = 0
    for temp_sunset in suneet_orders:
        for temp_slavic in slavic_orders:
            sunseet_wins = 0
            slavic_wins = 0
            
            # round 1
            if temp_sunset[0] > temp_slavic[0]:
                sunseet_wins += 1
            elif temp_sunset[0] < temp_slavic[0]:
                slavic_wins += 1
            
            # round 2
            if temp_sunset[1] > temp_slavic[1]:
                sunseet_wins += 1
            elif temp_sunset[1] < temp_slavic[1]:
                slavic_wins += 1
            
            if sunseet_wins > slavic_wins:
                ways += 1
    print(ways)