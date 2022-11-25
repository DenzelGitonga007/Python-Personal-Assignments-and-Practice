Twelve cards with grades from 0 to 11 randomly divided among 3 players: Ed, Grace, and Linus , 4 cards each.
- The game consists of 4 rounds. The goal of the round is to move by the card with the most points.
- In round 1, the first player who has a card with 0 points, takes the first turn, 
and he starts with that card. Then the second player (queue - Ed -> Grace -> Linus -> Ed, etc.) 
can move with any of his cards (each card is used only once per game, 
and there are no rules that require players to make only the best moves).
- The third player makes his move after the second player, and he sees the previous moves.
- The winner of the previous round then makes the first move in the next round with any remaining card.
- The player who wins 2 rounds first, wins the game.
Task
Return true if Ed has a chance of winning the game.
Return false if Ed has no chance.
Input
3 arrays of 4 unique numbers in each (numbers in array are sorted in ascending order). 
Input is always valid, no need to check.
Example
Round 1: Ed 2 5 8 11, Grace 1 4 7 10, Linus 0 3 6 9. Linus has to start from 0. 
Ed is risking nothing and goes 2. Grace gets lucky and wins round by throwing 4.
Round 2: Ed 5 8 11, Grace 1 7 10, Linus 3 6 9. Grace starts from 1. Linus goes 3, Ed wins with 5.
Round 3: Ed 8 11, Grace 7 10, Linus 6 9. Ed starts from 11 and wins the round either way.
Ed is the first to win 2 rounds and therefore wins the game, the answer is true.
One more example
Ed 0 1 2 3, Grace 6 7 8 11, Linus 4 5 9 10.
With these cards Ed has no chance, the answer is false.
Tip
Players can actually play DUMB moves, especially Grace and Linus.