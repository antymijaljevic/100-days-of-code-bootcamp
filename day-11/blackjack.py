# antymijaljevic@gmail.com
# Feb 11th 2023

from art import logo
from os import name, system
from random import shuffle, choice

""" poker cards and their values in Blackjack """
blackjack_cards = [('2♣️', 2), ('2♦️', 2), ('2♥️', 2), ('2♠️', 2),
                   ('3♣️', 3), ('3♦️', 3), ('3♥️', 3), ('3♠️', 3),
                   ('4♣️', 4), ('4♦️', 4), ('4♥️', 4), ('4♠️', 4),
                   ('5♣️', 5), ('5♦️', 5), ('5♥️', 5), ('5♠️', 5),
                   ('6♣️', 6), ('6♦️', 6), ('6♥️', 6), ('6♠️', 6),
                   ('7♣️', 7), ('7♦️', 7), ('7♥️', 7), ('7♠️', 7),
                   ('8♣️', 8), ('8♦️', 8), ('8♥️', 8), ('8♠️', 8),
                   ('9♣️', 9), ('9♦️', 9), ('9♥️', 9), ('9♠️', 9),
                   ('10♣️', 10), ('10♦️', 10), ('10♥️', 10), ('10♠️', 10),
                   ('J♣️', 10), ('J♦️', 10), ('J♥️', 10), ('J♠️', 10),
                   ('Q♣️', 10), ('Q♦️', 10), ('Q♥️', 10), ('Q♠️', 10),
                   ('K♣️', 10), ('K♦️', 10), ('K♥️', 10), ('K♠️', 10),
                   ('A♣️', 11), ('A♦️', 11), ('A♥️', 11), ('A♠️', 11)
                   ]

""" set bank balance """
player_bank = 1000
dealer_bank = 1000

""" set deck count """
deck_count = 2

""" possible chips """
chips = ['1', '5', '25', '50', '100', 'yolo']

def clear_terminal():
    """ 
        clears screen depends on a OS type
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
   
def shuffle_decks(deck, deck_count):
    """ 
        multiply original deck and shuffle it 
    """
    the_deck = deck * deck_count
    shuffle(the_deck)
    
    return the_deck

def set_bet(chip):
    """ 
        deduct values based on the choice
    """
    
    """ using global variables to keep track of the balance """
    global player_bank
    global dealer_bank
    bets = 0
    
    if chip.isdigit():
        chip = int(chip)
        player_bank -= chip
        dealer_bank -= chip
        bets += (chip * 2)
    else:
        bets += (player_bank + dealer_bank)
        player_bank, dealer_bank = 0, 0
        
    return bets

def game_monitor(cards, table_money):
    """
        shows remaining cards count, player bank and bet
    """
    print("\nGAME MONITOR:\n" + 
          f"REMAINING CARDS = {len(cards)}\n" + 
          f"PLAYER BANK = {player_bank}\n" + 
          f"BET = {table_money}")
    
def cards_on_table(p_cards, d_cards, hide):
    """
        shows cards on the table
    """
    player_cards = []
    dealer_cards = []
    
    for p, d in zip(p_cards, d_cards):
        # get symbols
        player_cards.append(p[0])
        dealer_cards.append(d[0])
        
    if hide:
        dealer_cards[1] = "*"
    
    print(f"\nTABLE:\n" +
        f"DEALER CARDS = {dealer_cards}\n" +
        f"PLAYER CARDS = {player_cards}")

def current_score(p_cards, d_cards, hide):
    """
        keeps scores track
    """
    player_score = []
    dealer_score = []
    
    for p, d in zip(p_cards, d_cards): 
        # get score
        player_score.append(p[1])
        dealer_score.append(d[1])
        
    # show scores
    if hide:
        print(f"DEALER SCORE = {dealer_score[0]}")
        dealer_score = sum(dealer_score)
    else:
        dealer_score = sum(dealer_score)
        print(f"DEALER SCORE = {dealer_score}")
        
    player_score = sum(player_score)
    print(f"PLAYER SCORE = {player_score}")

    return player_score, dealer_score
        
def cards_deal(cards, num):
    """
        deal player 2 cards and dealer 2 cards (1 one card face down)
    """
    player_cards = []
    dealer_cards = []
    
    for card in range(0, num):
        # deal cards for player
        random_card = choice(cards)
        player_cards.append(random_card)
        cards.remove(random_card)
        
        # deal cards for dealer
        random_card = choice(cards)
        dealer_cards.append(random_card)
        cards.remove(random_card)
        
    return player_cards, dealer_cards, cards

def main():
    """
        main game logic
    """
    
    """ clear terminal, show logo, shuffle the decks"""
    clear_terminal()
    print(logo)
    shuffled_cards = shuffle_decks(deck = blackjack_cards, deck_count = deck_count)
    print(f"TOTAL CARD NUMBER = {len(shuffled_cards)}, DECK NUMBER = {deck_count}")

    """ ask a player for a chip amount and reject incorrect input """    
    while True:
        print(f"\nPLAYER CASH = {player_bank}")
        player_chip = input("What is your chip choice? '1', '5', '25', '50', '100', 'YOLO'?  > ").lower()
        if player_chip in chips:
            money_on_table = set_bet(player_chip)
            break
        elif not player_chip:
            print("Only offered values please!")
        else:
            print(f"{player_chip.upper()} isn't in the offer ...")

    """ deal the cards """
    player_cards, dealer_cards, remaining_cards = cards_deal(shuffled_cards, 2)
    
    """ game monitor for the visiblity """
    game_monitor(cards = shuffled_cards, table_money = money_on_table)
    
    """ show cards on the table """
    cards_on_table(p_cards = player_cards, d_cards = dealer_cards, hide = True)
    
    """ show scores """
    player_score, dealer_score = current_score(p_cards = player_cards, d_cards = dealer_cards, hide = True)
    
    """ double logic """
    while True:
        double = input("\nDouble X2? 'yes' or 'enter' to continue: ").lower()
        if double == "yes":
            # double function
            break
        elif not double:
            break
        else:
            print("Wrong choice, choose again ...")
            
    """ a player choose """
    while True:
        hit_stand = input("\n'Hit' or 'Stand'? Which one is it?: ").lower()
    
        if hit_stand == "hit":
            player_cards += cards_deal(remaining_cards, 1)[0]
            print(player_cards)
            
            break
        elif hit_stand == "stand":
            pass
            break
        else:
            print("Wrong choice, choose again ...")
    


if __name__ == '__main__':
    main()
    







"""
Blackjack is a card game played between a dealer and one or more players. 
The objective of the game is to have a hand value of 21 or as close to 21 as 
possible, without going over.

Here's a rundown of the basic rules:

The game is played with one or more decks of standard playing cards.

The cards are ranked as follows: Ace can be worth either 1 or 11, face cards 
(King, Queen, Jack) are worth 10, and all other cards are worth their face value.

The game begins with each player receiving two cards and the dealer receiving one
card face up and one card face down.

The player can choose to "hit" (take another card) or "stand" (keep their current hand). 
The player continues to hit until they either have a hand value of 21 or over, or they choose to stand.

If the player goes over 21, they "bust" and lose the game.

After the player has finished their turn, the dealer reveals their face-down card and hits or stands according 
to a set of rules. In most versions of Blackjack, the dealer must hit until their hand value is at least 17.

If the dealer busts, all remaining players win.

If neither the player nor the dealer busts, the hand with the highest value less than or equal to 21 wins.

A "Blackjack" is a hand that consists of an Ace and any 10-point card (10, Jack, Queen, King). 
Blackjacks pay out at 3:2 odds, unless the dealer also has a Blackjack, in which case the game is a 
"push" (tie) and the player's bet is returned.

"""