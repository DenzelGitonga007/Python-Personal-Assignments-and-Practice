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
    # Getting the winner of the first round
    round_one_winner = max(round_one_scores, key=round_one_scores.get)
    # Checking whether Ed has a chance of winning
    if round_one_winner == "Ed":
        print("Ed has a chance of winning")
    else:
        print("Not yet there, Ed")
    print()
    print("And round one winner is {} with {} points".format(round_one_winner, round_one_scores.get(round_one_winner)))
    # View the scoreboard as the round_one_scores
    print()
    print("...Check out the scores...")
    print("The scoreboard: ", round_one_scores)
    # Adding the winner to the general score
    # winners = {
    #     round_one_winner : round_one_scores.get(round_one_winner)
    # }
    print()
    # Round Two
    print("...Round Two...")
    print("Cards remaining...")
    print("Ed: ", Ed)
    print("Grace: ",Grace)
    print("Linus: ", Linus)
    print()
    # The winner of the first round plays next
    if round_one_winner == "Ed":
        print("Ed plays first because he won the first round")
        Ed_round_two = random.sample(Ed, 1)
        # Remove the card
        Ed.remove(Ed_round_two[0]) # Because Ed_round_two is a list
        print("He plays with card {} and remains with {} cards".format(Ed_round_two, Ed))
        # Add the score to the round_two_scores
        round_two_scores = {
            "Ed" : Ed_round_two[0]
        }
    elif round_one_winner == "Grace":
        print("Grace plays first because she won the first round")
        Grace_round_two = random.sample(Grace, 1)
        # Remove the card
        Grace.remove(Grace_round_two[0]) # Because Grace_round_two is a list
        print("She plays with card {} and remains with {} cards".format(Grace_round_two, Grace))
        # Add the score to the round_two_scores
        round_two_scores = {
            "Grace" : Grace_round_two[0]
        }
    else:
        print("Linus plays first because he won the first round")
        Linus_round_two = random.sample(Linus, 1)
        # Remove the card
        Linus.remove(Linus_round_two[0]) # Because Linus_round_two is a list
        print("He plays with card {} and remains with {} cards".format(Linus_round_two, Linus))
        # Add the score to the round_two_scores
        round_two_scores = {
            "Linus" : Linus_round_two[0]
        }
    # The other players to play as well
    print()
    if len(Ed) != 2: #If Ed hasn't already played, or given out one more card
        print("Ed plays next... ... ...")
        Ed_round_two = random.sample(Ed, 1)
        # Remove the card
        Ed.remove(Ed_round_two[0])
        print("He plays with card {} and remains with {}".format(Ed_round_two, Ed))
        # Update the score to the round_two_scores
        round_two_scores["Ed"] = Ed_round_two[0]
        print()
    else:
        print("Grace or Linux play next...")
    if len(Grace) != 2: #If Grace hasn't already played, or given out one more card
        print("Grace playing... ... ...")
        Grace_round_two = random.sample(Grace, 1)
        # Remove the card
        Grace.remove(Grace_round_two[0])
        print("She plays with card {} and remains with {}".format(Grace_round_two, Grace))
        # Update the score to the round_two_scores
        round_two_scores["Grace"] = Grace_round_two[0]
        print()
    else:
        print("Linux next...")
    if len(Linus) != 2: #If Grace hasn't already played, or given out one more card
        print("Linus playing... ... ...")
        Linus_round_two = random.sample(Linus, 1)
        # Remove the card
        Linus.remove(Linus_round_two[0])
        print("He plays with card {} and remains with {}".format(Linus_round_two, Linus))
        # Update the score to the round_two_scores
        round_two_scores["Linus"] = Linus_round_two[0]
        print()
        print("...Round Two Closed...")
    else:
        print("...Round Two Closed...")

    # Getting the winner of the second round
    round_two_winner = max(round_two_scores, key=round_two_scores.get)
    # Checking whether Ed has a chance of winning
    if round_two_winner != "Ed":
        print("Oops! You missed it again, but keep trying, Ed")
    else:
        print("Yes, you're probably almost there, Ed")
    print()
    print("And round two winner is {} with {} points".format(round_two_winner, round_two_scores.get(round_two_winner)))
    # View the scoreboard as the round_one_scores
    print()
    print("...Check out the scores...")
    print("The scoreboard: ", round_two_scores)
    # Check whether there's any player who has won two times now
    if round_one_winner == "Ed" and round_two_winner == "Ed":
        print("Therefore, Ed wins the game")
        return
    elif round_one_winner == "Grace" and round_two_winner == "Grace":
        print("Therefore, Grace wins the game")
        return
    elif round_one_winner == "Linus" and round_two_winner == "Linus":
        print("Therefore, Linus wins the game")
        return
    else:
        print()
    
    # Round three
    print("...Round Three...")
    print("Cards remaining...")
    print("Ed: ", Ed)
    print("Grace: ",Grace)
    print("Linus: ", Linus)
    print()
    # The winner of the second round plays next
    if round_two_winner == "Ed":
        print("Ed plays first because he won in the second round")
        Ed_round_three = random.sample(Ed, 1)
        # Remove the card
        Ed.remove(Ed_round_three[0]) # Because Ed_round_three is a list
        print("He plays with card {} and remains with {} card".format(Ed_round_three, Ed))
        # Add the score to the round_three_scores
        round_three_scores = {
            "Ed" : Ed_round_three[0]
        }
    elif round_two_winner == "Grace":
        print("Grace plays first because she won in the second round")
        Grace_round_three = random.sample(Grace, 1)
        # Remove the card
        Grace.remove(Grace_round_three[0]) # Because Grace_round_three is a list
        print("She plays with card {} and remains with {} card".format(Grace_round_three, Grace))
        # Add the score to the round_three_scores
        round_three_scores = {
            "Grace" : Grace_round_three[0]
        }
    else:
        print("Linus plays first because he won the second round")
        Linus_round_three = random.sample(Linus, 1)
        # Remove the card
        Linus.remove(Linus_round_three[0]) # Because Linus_round_three is a list
        print("He plays with card {} and remains with {} card".format(Linus_round_three, Linus))
        # Add the score to the round_three_scores
        round_three_scores = {
            "Linus" : Linus_round_three[0]
        }
    # The other players to play as well
    print()
    if len(Ed) != 1: #If Ed hasn't already played, or given out one more card
        print("Ed plays next... ... ...")
        Ed_round_three = random.sample(Ed, 1)
        # Remove the card
        Ed.remove(Ed_round_three[0])
        print("He plays with card {} and remains with {}".format(Ed_round_three, Ed))
        # Update the score to the round_three_scores
        round_three_scores["Ed"] = Ed_round_three[0]
        print()
    else:
        print("Grace or Linux play next...")
    if len(Grace) != 1: #If Grace hasn't already played, or given out one more card
        print("Grace playing... ... ...")
        Grace_round_three = random.sample(Grace, 1)
        # Remove the card
        Grace.remove(Grace_round_three[0])
        print("She plays with card {} and remains with {}".format(Grace_round_three, Grace))
        # Update the score to the round_three_scores
        round_three_scores["Grace"] = Grace_round_three[0]
        print()
    else:
        print("Linux next...")
    if len(Linus) != 1: #If Grace hasn't already played, or given out one more card
        print("Linus playing... ... ...")
        Linus_round_three = random.sample(Linus, 1)
        # Remove the card
        Linus.remove(Linus_round_three[0])
        print("He plays with card {} and remains with {}".format(Linus_round_three, Linus))
        # Update the score to the round_three_scores
        round_three_scores["Linus"] = Linus_round_three[0]
        print()
        print("...Round Three Closed...")
    else:
        print("...Round Three Closed...")

    # Getting the winner of the third round
    round_three_winner = max(round_three_scores, key=round_three_scores.get)
    # Checking whether Ed has a chance of winning
    if round_three_winner != "Ed":
        print("Oops! You missed it again, you've got one more shot, Ed")
    else:
        print("Yes, you're probably almost there, Ed")
    print()
    print("And round three winner is {} with {} points".format(round_three_winner, round_three_scores.get(round_two_winner)))
    # View the scoreboard as the round_three_scores
    print()
    print("...Check out the scores...")
    print("The scoreboard: ", round_three_scores)
    # Check whether there's any player who has won two times now
    if (round_one_winner == "Ed" or round_two_winner == "Ed") and round_three_winner == "Ed":
        print("Therefore, Ed wins the game")
        return
    elif (round_one_winner == "Grace" or round_two_winner == "Grace") and round_three_winner == "Grace":
        print("Therefore, Grace wins the game")
        return
    elif (round_one_winner == "Linus" or round_two_winner == "Linus") and round_three_winner == "Linus":
        print("Therefore, Linus wins the game")
        return
    else:
        print()
    print()
    # Round four
    print("...Round Four...")
    print("Cards remaining...")
    print("Ed: ", Ed)
    print("Grace: ",Grace)
    print("Linus: ", Linus)
    print()
    # The winner of the four round plays next
    if round_three_winner == "Ed":
        print("Ed plays first because he won in the third round")
        Ed_round_four = random.sample(Ed, 1)
        # Remove the card
        Ed.remove(Ed_round_four[0]) # Because Ed_round_four is a list
        print("He plays with card {} and remains with {} card".format(Ed_round_four, Ed))
        # Add the score to the round_four_scores
        round_four_scores = {
            "Ed" : Ed_round_four[0]
        }
    elif round_three_winner == "Grace":
        print("Grace plays first because she won in the third round")
        Grace_round_four = random.sample(Grace, 1)
        # Remove the card
        Grace.remove(Grace_round_four[0]) # Because Grace_round_three is a list
        print("She plays with card {} and remains with {} card".format(Grace_round_four, Grace))
        # Add the score to the round_four_scores
        round_four_scores = {
            "Grace" : Grace_round_four[0]
        }
    else:
        print("Linus plays first because he won the third round")
        Linus_round_four = random.sample(Linus, 1)
        # Remove the card
        Linus.remove(Linus_round_four[0]) # Because Linus_round_four is a list
        print("He plays with card {} and remains with {} card".format(Linus_round_four, Linus))
        # Add the score to the round_four_scores
        round_four_scores = {
            "Linus" : Linus_round_four[0]
        }
    # The other players to play as well
    print()
    if len(Ed) != 0: #If Ed hasn't already played, or given out one more card
        print("Ed plays next... ... ...")
        Ed_round_four = random.sample(Ed, 1)
        # Remove the card
        Ed.remove(Ed_round_four[0])
        print("He plays with card {} and remains with {}".format(Ed_round_four, Ed))
        # Update the score to the round_four_scores
        round_four_scores["Ed"] = Ed_round_four[0]
        print()
    else:
        print("Grace or Linux play next...")
    if len(Grace) != 0: #If Grace hasn't already played, or given out one more card
        print("Grace playing... ... ...")
        Grace_round_four = random.sample(Grace, 1)
        # Remove the card
        Grace.remove(Grace_round_four[0])
        print("She plays with card {} and remains with {}".format(Grace_round_four, Grace))
        # Update the score to the round_four_scores
        round_four_scores["Grace"] = Grace_round_four[0]
        print()
    else:
        print("Linux next...")
    if len(Linus) != 0: #If Grace hasn't already played, or given out one more card
        print("Linus playing... ... ...")
        Linus_round_four = random.sample(Linus, 1)
        # Remove the card
        Linus.remove(Linus_round_four[0])
        print("He plays with card {} and remains with {}".format(Linus_round_four, Linus))
        # Update the score to the round_four_scores
        round_four_scores["Linus"] = Linus_round_four[0]
        print()
        print("...Round Four Closed...")
    else:
        print("...Round Four Closed...")

    # Getting the winner of the fourth round
    round_four_winner = max(round_four_scores, key=round_four_scores.get)
    # Checking whether Ed has a chance of winning
    if round_four_winner != "Ed":
        print("Oops! You missed it again, but keep trying, Ed")
    else:
        print("Yes, you're probably almost there, Ed")
    print()
    print("And round four winner is {} with {} points".format(round_four_winner, round_four_scores.get(round_four_winner)))
    # View the scoreboard as the round_four_scores
    print()
    print("...Check out the scores...")
    print("The scoreboard: ", round_four_scores)
    if (round_one_winner == "Ed" or round_two_winner == "Ed") and (round_three_winner == "Ed" or round_four_winner == "Ed"):
        print("Therefore, Ed wins the game")
        return
    elif (round_one_winner == "Grace" or round_two_winner == "Grace") and (round_three_winner == "Grace" or round_four_winner == "Grace"):
        print("Therefore, Grace wins the game")
        return
    elif (round_one_winner == "Linus" or round_two_winner == "Linus") and (round_three_winner == "Linus" or round_four_winner == "Ed"):
        print("Therefore, Linus wins the game")
        return
    else:
        print()
    print()
    #End of function
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
winners = {}
card_game(Ed, Grace, Linus)


