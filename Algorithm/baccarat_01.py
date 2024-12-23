# This is a python file to show how the game works
import random

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
OUTCOME = ['Player wins', 'Banker wins', 'Tie']

# Inclusive range function
irange = lambda start, end: range(start, end + 1)

def compute_score(hand):
    """Compute the score of a hand"""
    total_value = 0
    for card in hand:
        total_value += VALUE[CARDS.index(card)]
    return total_value % 10

def play():
    """Returns the winner"""
    player_hand = [
        random.choice(CARDS),
        random.choice(CARDS)
    ]
    banker_hand = [
        random.choice(CARDS),
        random.choice(CARDS)
    ]

    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    print('Player has cards:\t' + player_hand[0] + '\t' + player_hand[1])
    print('Player has score of\t' + str(player_score))
    print('Banker has cards:\t' + banker_hand[0] + '\t' + banker_hand[1])
    print('Banker has score of\t' + str(banker_score))

    # Natural
    if player_score in [8, 9] or banker_score in [8, 9]:
        if player_score != banker_score:
            return OUTCOME[banker_score > player_score]
        else:
            return OUTCOME[2]

    # Player has low score
    if player_score in irange(0, 5):
        # Player get's a third card
        player_hand.append(random.choice(CARDS))
        player_third = compute_score([player_hand[2]])
        print('Player gets a third card:\t' + player_hand[2])

        # Determine if banker needs a third card
        if (banker_score == 6 and player_third in [6, 7]) or \
           (banker_score == 5 and player_third in irange(4, 7)) or \
           (banker_score == 4 and player_third in irange(2, 7)) or \
           (banker_score == 3 and player_third != 8) or \
           (banker_score in [0, 1, 2]):
            banker_hand.append(random.choice(CARDS))
            print('Banker gets a third card:\t' + banker_hand[2])

    elif player_score in [6, 7]:
        if banker_score in irange(0, 5):
            banker_hand.append(random.choice(CARDS))
            print('Banker gets a third card:\t' + banker_hand[2])

    # Compute the scores again and return the outcome
    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    print('Player has final score of\t' + str(player_score))
    print('Banker has final score of\t' + str(banker_score))

    if player_score != banker_score:
        return OUTCOME[banker_score > player_score]
    else:
        return OUTCOME[2]

print(play())