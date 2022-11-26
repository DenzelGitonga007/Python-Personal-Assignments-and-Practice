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

import random # For random selection

# Function to play
def card_game(Ed, Grace, Linus):
    """...Playing now..."""
    print()
    print("...Let the game begin...")
    print("...Round One...")
    # To set who begins, then remove the 0
    if 0 in Ed:
        print("Ed begins because he has the 0: ", Ed)
        Ed.remove(0)
        # Add the score onto the dictionary
        round_one_scores = {
            "Ed" : 0
        }
        print("He remains with: ",Ed)
        print()
    elif 0 in Grace:
        print("Grace begins because she has the 0: ", Grace)
        # Add the score onto the dictionary
        round_one_scores = {
            "Grace" : 0
        }
        Grace.remove(0)
        print("She remains with: ", Grace)
        print()
    else:
        print("Linus begins because he has the 0: ", Linus)
        # Add the score onto the dictionary
        round_one_scores = {
            "Linus" : 0
        }
        Linus.remove(0)
        print("He remains with: ", Linus)
        print()
    # The other players to play, but not the one who started with the 0
    if 0 not in Ed and len(Ed) != 3:
        print("Ed playing... ... ...")
        # Randomly select a card
        Ed_round_one = random.sample(Ed, 1)
        # Remove the card from the Ed's list, as this is how the game is played
        Ed.remove(Ed_round_one[0]) # because Ed_round_one is a list
        print("He plays with card {} and remains with {}".format(Ed_round_one, Ed))
        # Update the score onto the dictionary
        round_one_scores["Ed"] = Ed_round_one[0]
        print()
    else:
        print("Grace or Linus to play next...")
        print()
    if 0 not in Grace and len(Grace) != 3:
        print("Grace playing... ... ...")
        # Randomly select a card
        Grace_round_one = random.sample(Grace, 1)
        # Remove the card from Grace's list, as this is how the game is played
        Grace.remove(Grace_round_one[0]) # because Grace_round_one is a list
        print("She plays with card {} and remains with {}".format(Grace_round_one, Grace))
        # Update the score onto the dictionary
        round_one_scores["Grace"] = Grace_round_one[0]
        print()
    else:
        print("Linus go next")

    if 0 not in Linus and len(Linus) != 3:
        print("Linus playing... ... ...")
        # Randomly select a card
        Linus_round_one = random.sample(Linus, 1)
        # Remove the card from Linus' list, as this is how the game is played
        Linus.remove(Linus_round_one[0]) # because Linus_round_one is a list
        print("He plays with card {} and remains with {}".format(Linus_round_one, Linus))
        # Update the score onto the dictionary
        round_one_scores["Linus"] = Linus_round_one[0]
        print()
        print("...Round One Closed...")
    else:
        print("...Round One Closed...")
    # View the scoreboard as the round_one_scores
    print()
    print("...Check out the scores now...")
    print("The scoreboard: ", round_one_scores)
    # Getting the winner of the first round
    round_one_winner = max(round_one_scores, key=round_one_scores.get)
    print("And round one winner is {} with {} points".format(round_one_winner, round_one_scores.get(round_one_winner)))
    print()
    print("...Round Two...")
    print("Cards remaining...")
    print("Ed: ", Ed)
    print("Grace: ",Grace)
    print("Linus: ", Linus)
    print()
    # The winner of the first round plays next
    


print("...Card Game...")
print()
print("Players are: Ed, Grace, Linus")
print()
# Declare the list of card numbers and select 4 cards to assign to Ed, Grace, and Linus
cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("The cards available are: ", cards)
print()
# Randomly select the cards and assign them to the players
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
print("Grace takes {} cards, and the cards that remain are: {}".format(Grace, cards))
print()
# Give to Linus
Linus = sorted(random.sample(cards, 4))
# To ensure that cards assigned to Linus are not in the list anymore
for Linus_cards in Linus:
    cards.remove(Linus_cards)
print("Linus takes the remaining cards: {}".format(Linus))
print()
print("The players are now ready to play: ")
print()
print("Ed: ",Ed)
print()
print("Grace: ",Grace)
print()
print("Linus: ",Linus)
# Declare the dictionaries for scores; player, score pairs
round_one_scores = {}
round_two_scores = {}
round_three_scores = {}
round_four_scores = {}
card_game(Ed, Grace, Linus)


