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
chips = ['1', '5', '25', '50', '100', '500', '1000', 'yolo']

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

def set_bet(chip, existing_bet = False):
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
        if existing_bet:
            existing_bet += (chip * 2)
            bets = existing_bet
        else:
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
    
def deal(deck, num, existing_card = False):
    """
        recieves decks, picks a random card,
        returns the card and the remaining cards in the deck
    """
    if existing_card:
        cards = existing_card
    else:
        cards = []
        
    for _ in range(0, num):
        random_card = choice(deck)
        cards.append(random_card)
        deck.remove(random_card)
    
    return cards, deck
  
def show_cards(player_cards, dealer_cards, hide):
    """
        shows cards on the table for both
    """
    dealer_cards_list = []
    player_cards_list = []
    
    dealer_score_list = []
    player_score_list = []
    
    for dealer in dealer_cards:
        # get symbols
        dealer_cards_list.append(dealer[0])
        # get scores
        dealer_score_list.append(dealer[1])
        
    for player in player_cards:
        # get symbols
        player_cards_list.append(player[0])
        # get scores
        player_score_list.append(player[1])
    
    # hide dealer second card in a first round    
    if hide:
        dealer_cards_list[1] = "*"
    
    # show cards
    print(f"\nTABLE:\n" +
        f"DEALER CARDS = {dealer_cards_list}\n" +
        f"PLAYER CARDS = {player_cards_list}")
    
    # show scores
    if hide:
        # hide dealer's second card score
        print(f"DEALER SCORE = {dealer_score_list[0]}")
        dealer_score_list = sum(dealer_score_list)
    else:
        dealer_score_list = sum(dealer_score_list)
        print(f"DEALER SCORE = {dealer_score_list}")
        
    player_score_list = sum(player_score_list)
    print(f"PLAYER SCORE = {player_score_list}")

    return player_score_list, dealer_score_list

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
        print(f"\nPLAYER CHIP STACK = {player_bank}")
        player_chip = input("What is your chip choice? '1', '5', '25', '50', '100', '500', '1000', 'YOLO'?  > ").lower()
        if player_chip in chips:
            money_on_table = set_bet(player_chip)
            break
        elif not player_chip:
            print("Only offered values please!")
        else:
            print(f"{player_chip.upper()} isn't in the offer ...")    
    
    """ deal two cards for each """
    dealer_cards, remaining_cards = deal(deck = shuffled_cards, num = 2)
    player_cards, remaining_cards = deal(deck = remaining_cards, num = 2)
    
    """ show cards and scores for both """
    player_score, dealer_score = show_cards(dealer_cards = dealer_cards, player_cards = player_cards, hide = True)
    
    """ game monitor for the visiblity """
    game_monitor(cards = remaining_cards, table_money = money_on_table)   
    
    """ double X2 logic """
    if player_chip != "yolo":
        if player_bank >= int(player_chip):
            while True:
                double = input("\nDouble X2? 'yes' or 'enter' to continue: ").lower()
                if double == "yes":
                    money_on_table = set_bet(player_chip, money_on_table)
                    game_monitor(cards = remaining_cards, table_money = money_on_table)
                    break
                elif not double:
                    break
                else:
                    print("Wrong input ...")
            
    """ player play """
    dealer_won = False
    
    while True:
        hit_stand = input("\n'Hit' or 'Stand'? Which one is it?: ").lower()
        if hit_stand == "hit":
            player_cards, remaining_cards = deal(deck = remaining_cards, num = 1, existing_card = player_cards)
            player_score, dealer_score = show_cards(dealer_cards = dealer_cards, player_cards = player_cards, hide = True)
        
            if player_score == 21:
                print("**** BlackJack ****")
                break
            elif player_score > 21:
                print("\nBust!")
                dealer_won = True
                break
            
        elif hit_stand == "stand":
            player_score, dealer_score = show_cards(dealer_cards = dealer_cards, player_cards = player_cards, hide = False)
            
            if player_score < dealer_score:
                dealer_won = True
                print("Dealer wins!")
                break
            elif player_score == 21 and dealer_score == 21:
                print("Draw!")
                break
            else:
                print("Dealer's turn ..")
                break
        else:
            print("Wrong input ...")
            
    """ dealer play """
    if not dealer_won:
        print("\nDealer is playing now ...")


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