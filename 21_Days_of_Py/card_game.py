# Twelve cards with grades from 0 to 11 randomly divided among 3 players: Ed, Grace, and Linus , 4 cards each.
# - The game consists of 4 rounds. The goal of the round is to move by the card with the most points.
# - In round 1, the first player who has a card with 0 points, takes the first turn, 
# and he starts with that card. Then the second player (queue - Ed -> Grace -> Linus -> Ed, etc.) 
# can move with any of his cards (each card is used only once per game, 
# and there are no rules that require players to make only the best moves).
# - The third player makes his move after the second player, and he sees the previous moves.
# - The winner of the previous round then makes the first move in the next round with any remaining card.
# - The player who wins 2 rounds first, wins the game.
# Task
# Return true if Ed has a chance of winning the game.
# Return false if Ed has no chance.
# Input
# 3 arrays of 4 unique numbers in each (numbers in array are sorted in ascending order). 
# Input is always valid, no need to check.
# Example
# Round 1: Ed 2 5 8 11, Grace 1 4 7 10, Linus 0 3 6 9. Linus has to start from 0. 
# Ed is risking nothing and goes 2. Grace gets lucky and wins round by throwing 4.
# Round 2: Ed 5 8 11, Grace 1 7 10, Linus 3 6 9. Grace starts from 1. Linus goes 3, Ed wins with 5.
# Round 3: Ed 8 11, Grace 7 10, Linus 6 9. Ed starts from 11 and wins the round either way.
# Ed is the first to win 2 rounds and therefore wins the game, the answer is true.
# One more example
# Ed 0 1 2 3, Grace 6 7 8 11, Linus 4 5 9 10.
# With these cards Ed has no chance, the answer is false.
# Tip
# Players can actually play DUMB moves, especially Grace and Linus.

# Function to play
def card_game(Ed, Grace, Linus):
    """...Playing now..."""
    print("")
    print("...Let the game begin...")
    
print("...Card Game...")
print()
print("Players are: Ed, Grace, Linus")
print()
# Declare the list of card numbers and select 4 cards to assign to Ed, Grace, and Linus
cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("The cards available are: ", cards)
print()
# Randomly select the cards and assign them to the players
import random
Ed = sorted(random.sample(cards, 4))
# To ensure that cards assigned to Ed are not in the list anymore
for Ed_cards in Ed:
    cards.remove(Ed_cards)
print("After giving Ed {} cards, the cards that remain are: {}".format(Ed, cards))
print()
# Give to Grace also
Grace = sorted(random.sample(cards, 4))
# To ensure that cards assigned to Grace are not in the list anymore
for Grace_cards in Grace:
    cards.remove(Grace_cards)
print("After giving Grace {} cards, the cards that remain are: {}".format(Grace, cards))
print()
# Give to Linus
Linus = sorted(random.sample(cards, 4))
# To ensure that cards assigned to Linus are not in the list anymore
for Linus_cards in Linus:
    cards.remove(Linus_cards)
print("After giving Ed {} cards, the cards that remain are: {}".format(Linus, cards))
print()
print("The players are now ready to play: ")
print()
print("Ed: ",Ed)
print()
print("Grace: ",Grace)
print()
print("Linus: ",Linus)
card_game(Ed, Grace, Linus)


