#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
                           ╔╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤╗
                           ╟┼┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┼╢
                           ╟┤ __________ _   _ ____     ___  _____       _ _   _ ___ ____ _____ ├╢
                           ╟┤|__  / ____| | | / ___|   / _ \|  ___|     | | | | |_ _/ ___| ____|├╢
                           ╟┤  / /|  _| | | | \___ \  | | | | |_     _  | | | | || | |   |  _|  ├╢
                           ╟┤ / /_| |___| |_| |___) | | |_| |  _|   | |_| | |_| || | |___| |___ ├╢
                           ╟┤/____|_____|\___/|____/___\___/|_|____ _\___/_\___/|___\____|_____|├╢
                           ╟┤        |  _ \|  _ \| ____/ ___|| ____| \ | |_   _/ ___|           ├╢
                           ╟┤        | |_) | |_) |  _| \___ \|  _| |  \| | | | \___ \           ├╢
                           ╟┤        |  __/|  _ <| |___ ___) | |___| |\  | | |  ___) |          ├╢
                           ╟┤       _|_|  _|_| \_\_____|____/|_____|_| \_| |_|_|____/ __        ├╢
                           ╟┤      | __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /        ├╢
                           ╟┤      |  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' /         ├╢
                           ╟┤      | |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \         ├╢
                           ╟┤      |____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\        ├╢
                           ╟┼┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┼╢
                           ╚╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╧╝
'''

import random
import os
import time as t 
from IPython.display import clear_output # Used to clear the output of each player input.
suits = ('♥', '♣', '♦', '♠')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
actions = {1:'hit',2:'stand',3:'insurance',4:'split',5:'double down',6:'surrender'}
empty_card_lines = [
    '{}┌─────────┐{}',
    '{}│ {:2}      │{}',
    '{}│         │{}',
    '{}│         │{}',
    '{}│    {}    │{}',
    '{}│         │{}',
    '{}│         │{}',
    '{}│       {:2}│{}',
    '{}└─────────┘{}'
]
hidden_card_lines = [
    '{}┌─────────┐{}',
    '{}│░░░░░░░░░│{}',
    '{}│░░░░░░░░░│{}',
    '{}│░░░░░░░░░│{}',
    '{}│░░░░░░░░░│{}',
    '{}│░░░░░░░░░│{}',
    '{}│░░░░░░░░░│{}',
    '{}│░░░░░░░░░│{}',
    '{}└─────────┘{}'
]
print_empty_card_lines = [
    '           ',
    '           ',
    '           ',
    '           ',
    '           ',
    '           ',
    '           ',
    '           ',
    '           '
]
empty_chip_lines = [
    '{}    * * *    {} ',
    '{} * *  *  * * {} ',
    '{}*   ${:4}   *{} ',
    '{}*   Z.O.J   *{} ',
    '{} * *  *  * * {} ',
    '{}    * * *    {} ',
    '{} X{:5}       {} ',  
]
orange_color = '\033[33m'
magenta_color = '\033[35m'
black_color = '\033[30m'
green_color = '\033[32m'
red_color = '\033[31m'
white_color = '\033[37m'

turns = 0
#Card class:
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank +' of '+ self.suit
    
class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0)
#________________________Player class________________________#
class Player():
    def __init__(self, name, money,turn = True):
        self.name = name
        self.money = money
        self.hand = [[]] #is a list of lists to allow player to have multiple hands with different outcomes.
        self.turn = turn
        self.bet = ['0']
        self.insurance_bet = 0
        self.insurance_flag = False
        self.turns = 0
        self.card_status = []
        #self.number_of_hands = len(self.hand)
        self.hand_score = []
        self.hand_turn = [True]
        self.last_action = ['']
    """  
    ################################################--place_a_bet--########################################################
    Using this method The player will place a bet associated with the active hand when needed.
    Bet placements:
    -At the begining of a new game.
    -After a hand split.
    -When double down conditions are met.
    -When insurance is available but it is not bound to a hand.

    Placing a bet is a must at the begining of the game or a choice if the player decides to perform one of blackjack actions.

    Input:
         -index:refers to the active hand.

    Operation:
    This method will loop over and over until a valid input is entered.

    What is a valid input?
    A number greater than zero (0) and less thn or equal the available money.

    """        
    def place_a_bet(self,index):
        buffer = ' '
        while not buffer.isdigit() or int(buffer) <= 0:
            buffer = input("Please enter a valid bet (you have {}$):".format(self.money))
        if buffer.isdigit() and int(buffer) > 0:
            if index < len(self.bet):
                self.bet[index] = int(buffer)
            else:
                self.bet.append(int(buffer))
        if(self.bet[index] <= self.money):
            self.money -= self.bet[index]
            
        else:
            print('Guards!!! Remove that PUNK!!!')
            self.bet[index] = 0
        if self.money == 0:
            print('All in!! Be careful')
            t.sleep(1)

    """  
    ################################################--hit--########################################################
    Using this method will add a card to player's hand.

    Input:
         -card: is given by using "deal_one" from card class.
         -index: refering to the active hand.
    note: card status is used to print card whether face up or face down. Player cards are only printed face up. But
          dealer's second card is printed face down until the dealer gets his turn. because i used one method(in table class)
          to print player and deaer's hands.
    """             
    
    def hit(self, card, index):
        self.hand[index].append(card)
        self.card_status.append('Face up')
        print('{} is hitting'.format(self.name))
    
    def standing(self,index):
        self.hand_turn[index] = False
        if index == len(self.hand)-1:
            self.turn = False
        #print('{} is standing'.format(self.name))
    
    """ 
    ################################################--SPLITTING--########################################################
    Using this method will split the current hand into two groups. By using list of lists will facilitate the creation of
    multiple hands for each player.

    Splitting can only be done when the players just completed a hand of two similar numerical value cards or similar face
    cards.

    Splitting a hand is a choice for the palyer to take if desired.


    """ 
    def splitting(self,index):
        upper_half = []
        lower_half = []
        upper_half = [self.hand[index][0]]
        lower_half = [self.hand[index][1]]
        self.hand.pop(index)
        self.hand.append(upper_half)
        self.hand.append(lower_half)
        #self.number_of_hands += 1
        self.hand_turn.append(False)
        flag = True
        while flag:
            buffer = ' '
            while (not(buffer.isdigit()) or int(buffer) <= 0):
                buffer = input("You can raise your bet up to the original bet ({}$). Please enter a valid bet (you have {}$):"
                            .format(self.bet[index],self.money))
            if(int(buffer) <= self.money) and (int(buffer) > 0):
                if int(buffer) > self.bet[index]:
                    print('You can not raise your bet more than the original bet of{}$'.format(self.bet[index]))
                    t.sleep(2)
                else:
                    flag = False
                    self.money -= int(buffer)
                    self.bet.append(int(buffer))
    """  
    ################################################--double_down--########################################################
    Using this method will double the already placed bet and it can only be done if double down conditions are met.
    when to double down:
    if player hand sum a hard 9 or 10,
    or hand sum soft 16, 17 or 18,
    or hand sum of 11 (sof or hard).

    """             
        
    def double_down(self,card,index):
        flag = True
        while flag:
            buffer = ' '
            while (not(buffer.isdigit()) or int(buffer) <= 0):
                buffer = input("You can raise your bet up to the original bet ({}$). Please enter a valid bet (you have {}$):"
                            .format(self.bet[index],self.money))
            if(int(buffer) <= self.money) and (int(buffer) > 0):
                if int(buffer) > self.bet[index]:
                    print('You can not raise your bet more than the original bet of{}$'.format(self.bet[index]))
                    t.sleep(2)
                else:
                    flag = False
                    self.money -= int(buffer)
                    self.bet[index] += int(buffer)
                    if index < len(self.hand):
                        print('You will only dealt one card and your turn will be eneded for the current hand.')
                        t.sleep(1.5)
                    else:
                        print('You will only dealt one card and your turn will be eneded.')
                        t.sleep(1.5)
                    self.hit(card,index)
                    self.hand_turn[index] = False
                    if index == len(self.hand)-1:
                        self.turn = False

            
    """  
    ##################################################--insurance--########################################################
    Using this method the player will bet that the dealer will get a blackjack, usually when the dealer has an ace as
    face up card.

    """                   
    def insurance(self,index):
        flag = True
        while flag:
            if not self.insurance_flag:
                buffer = ' '
                while (not(buffer.isdigit()) or int(buffer) <= 0):
                    buffer = input("You can raise your bet up to the half original bet ({}$). Please enter a valid bet (you have {}$):"
                                .format((self.bet[index]/2),self.money))
                if(int(buffer) <= self.money) and (int(buffer) > 0):
                    if int(buffer) > (self.bet[index]/2):
                        print('You can not raise your bet more than half the original bet of{}$'.format(self.bet[index]))
                        t.sleep(2)
                    else:
                        flag = False
                        self.insurance_flag = True
                        self.money -= int(buffer)
                        self.insurance_bet += int(buffer)
            else:
                print('You have already placed insurance bet.')
                flag = False
                t.sleep(1.5)


        
    """  
    ##################################################--surrender--########################################################
    Using this method the player will end forfeit current hand and lose half of the original bet. Half is add back to the player,
    and the other half is added to the dealer's money.
    Input:
         -money: dealer's money.
         -index: the bet related to the active hand.
    """                 
    def surrender(self,money,index):
        self.hand_turn[index] = False
        self.bet[index] *= 0.5
        
        if index == len(self.hand) - 1:
            self.turn = False
            print('Half of your bet is lost.')
        else:
            print('Half of your bet is lost for the current hand.')
            
        self.money += self.bet[index]
        money += self.bet[index]
        self.bet[index] = 0
    """  
    ##################################################--bust--########################################################
    This method is used at the event of player's hand score become greater than 21.
    Input:
         -money: dealer's money.
         -index: the bet related to the active hand.
    """                   
    def bust(self,money,index):
        money += self.bet[index]
        self.bet[index] = 0
        self.hand_turn[index] = False
        if index == (len(self.hand)-1):
            self.turn = False
        
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards'
    
    
#------------------------------------------------------------------DEALER CLASS-----------------------------------------------  
class Dealer(): 
    def __init__(self,name='Alex',money = 9999999,turn = False):
        self.name = name
        self.hand = [[]]#even though the dealer only has one hand, but the method used to print dealer's hand is 
                        #the same method used to print player's hand so i needed to have the same infrastructure.
        self.money = money
        self.turn = turn
        self.card_status = []
        self.hand_score= 0
    """  
    ##################################################--hit--########################################################
    This method is used to let the dealer add card to his hand as long as his hand score less than 17
    Input:
         -card: is given by using "deal_one" from card class.
         -hand_score: given from table method "hand_score_calculator"
    """                   
    def hit(self, card, hand_score):
        if self.turn:
            if hand_score < 17:
                print('The dealer is hitting')
                self.hand[0].append(card)
                if len(self.hand[0]) ==2:
                    self.card_status.append('Face down')
                else:
                    self.card_status.append('Face up')
                return False
            else:
                return True
    """  
    ##################################################--standing--########################################################
    The dealer will stand if the hand score is 17 or more
    Input:
         -hand_score: given from table method "hand_score_calculator"
    """                 
    
    def standing(self,hand_score):
        if self.turn:
            if hand_score >= 17:
                self.turn = False
                print('The dealer is standing')
    
    def will_check_face_down_card(self):
        if self.hand[0][0].rank in ('10','J','Q','K','A'):
            print('The dealer is checking for BlackJack.')
            t.sleep(2)
            return True
        else:
            return False
        pass
    
#-----------------------------------------------------------TABLE CLASS-------------------------------------------------------
class Table():
    cash_chip = {'White':0,'Red':0,'Green':0,'Black':0,'Purple':0,'Orange':0}
    bet_chip = {'White':0,'Red':0,'Green':0,'Black':0,'Purple':0,'Orange':0}
    value = {'White':1,'Red':5,'Green':25,'Black':100,'Purple':500,'Orange':1000}
    key = ('White','Red','Green','Black','Purple','Orange')
    color_dictionary = {'White':white_color,'Red':red_color,
                        'Green':green_color,'Black':black_color,
                        'Purple':magenta_color,'Orange':orange_color}
    spaces = {'White':3,'Red':3,'Green':2,'Black':1,'Purple':1,'Orange':0}
    
    def __init__(self,player,dealer,deck):
        self.player = player
        self.dealer = dealer
        self.cash_chip = Table.cash_chip
        self.bet_chip = Table.bet_chip
        self.value = Table.value
        self.key = Table.key
        self.playing = True
        self.deck = deck
        
        
    """  
    ###############################################--convert_money_to_chip--#####################################################
    this method will conver money intger value to an animated interpretation of it.
    external values:
                   -value = {'White':1,'Red':5,'Green':25,'Black':100,'Purple':500,'Orange':1000}
                   -key = ('White','Red','Green','Black','Purple','Orange')
    #(number) notes:
    #1: the values are scanned backward to insure the least amount of chips are used to represent the money.

    For example: if a player has 1255$ money and want to convert them into chips
    1- The amount is compared with 1000$ chip: is 1250 > 1000--->True--then--> number of 1000 chips = int(1250/1000)
    = int(1.25) = 1--->after that---> money - (number of 1000 chips)*1000 = 1250 - 1*1000 = 250.
    2- is 250 > 500--->False.
    3- is 250 > 100--->True--Then-->number of 100 chips = int(250/100) = int(2.5) = 2--->
    after that---> money - (number of 100 chips) * 100 = 250 - 200 = 50.
    4-is 50 > 25--->True number of 25 chips = 2 and money = 0
    5-is 0 > 10---> False.
    6-is 0 > 1---> False.
    Input:
         -money: whether money or bet.
         -flag: boolean value used to select between returning money_chip or bet_chip

    """                    
    
    def convert_money_to_chip(self,money,flag):
        for i in range(len(self.key)-1,-1,-1): #1 refer to the "#(number) notes" above.
            self.cash_chip[self.key[i]] = 0
            if money >= self.value[self.key[i]]:
                if flag:
                    self.cash_chip[self.key[i]] = int(money / self.value[self.key[i]])
                    money = money - (self.value[self.key[i]] * self.cash_chip[self.key[i]])
                else:
                    self.bet_chip[self.key[i]] = int(money / self.value[self.key[i]])
                    money = money - (self.value[self.key[i]] * self.bet_chip[self.key[i]])
        if flag:
            return self.cash_chip
        else:
            return self.bet_chip
    """ 
    ##################################################--print_card_on_table--########################################################
    This method is used to print card like representation of each card class value in the active hand. it can print hands face up or
    face down with the correct color. An empty line string variable is used to add each line of each card to be printed
    side by side line by line.
    For example:
               if we want to print ***** ***** ,first we will add the first line of each card to variable called "line"
                                   * 8 * * 5 *
                                   ***** *****
               at line = 0:  line = + '*****' +'*****', print it, then move to the next line and erase what is inside line  variable.
               at line = 1:  line = + '* 8 *' +'* 5 *', print it, then move to the next line and erase what is inside line  variable.
               at line = 2:  line = + '*****' +'*****', print it, then move to the next line and erase what is inside line  variable.
                                   
    External values: 
                   -black_color = '\033[30m'---->for ♠ & ♣.
                   -red_color = '\033[31m'---->for ♦ & ♥.
    Input:
         -hand: player or dealer's hand.
         -card_status: to print cards face up or face down.
         -index: to print cards of the active hand.
    """                  
    
    def print_card_on_table(self,hand,card_status,index):
        for i in range(9):
            line = ''
            for j in range(len(hand[index])):
                if(hand[index][j].suit == '♦' or hand[index][j].suit == '♥') and card_status[j] == 'Face up':
                    if i == 1 or i == 7:
                        line = line + empty_card_lines[i].format(red_color,hand[index][j].rank,black_color)
                    elif i == 4:
                        line = line + empty_card_lines[i].format(red_color,hand[index][j].suit,black_color)
                    else:
                        line = line + empty_card_lines[i].format(red_color,black_color)

                elif(hand[index][j].suit == '♠' or hand[index][j].suit == '♣') and card_status[j] == 'Face up':
                    if i == 1 or i == 7:
                        line = line + empty_card_lines[i].format(black_color,hand[index][j].rank,black_color)
                    elif i == 4:
                        line = line + empty_card_lines[i].format(black_color,hand[index][j].suit,black_color)
                    else:
                        line = line + empty_card_lines[i].format(black_color,black_color)
                        
                elif(card_status[j] == 'Face down'):
                    if(hand[index][j].suit == '♦' or hand[index][j].suit == '♥'):
                        line = line + hidden_card_lines[i].format(red_color,black_color)
                    elif(hand[index][j].suit == '♠' or hand[index][j].suit == '♣'): 
                        line = line + hidden_card_lines[i].format(black_color,black_color)
            print(line)
        print('\n')
    """ 
    ##################################################--print_chips_on_table--########################################################
    This method will print money or bet in an animated chips form representing each value with its count underneath it.
    This method uses the same printing princible as the one above.
    """                      
        
    def print_chips_on_table(self,chips):
        for i in range(len(empty_chip_lines)):
            line = ''
            for j in range(len(self.key)):
                if i == 0 or i == 1 or i == 3 or i == 4 or i == 5:
                    line = line + empty_chip_lines[i].format(self.color_dictionary[self.key[j]],black_color)
                elif i == 2:
                    line = line + empty_chip_lines[i].format(self.color_dictionary[self.key[j]],
                                                             self.value[self.key[j]],black_color) 
                elif i == 6:
                    line = line + empty_chip_lines[i].format(self.color_dictionary[self.key[j]],chips[self.key[j]],black_color)
                
            print(line)
        print('\n')

    """ 
    ##################################################--split_check--########################################################
    This method checks if the player has splitable hand. A hand can be split if it is consists of 2 cards and have the 
    same rank. it returns true if a hand can be split, abd false otherwise.
    
    Input:
         -index: refering to the active hand.

    """                     
    def split_check(self,index):
        if self.player.hand[index][0].rank == self.player.hand[index][1].rank and len(self.player.hand[index]) == 2:
            return True
        else:
            return False
            
    
    """ 
    ############################################--player_blackjack_check--####################################################
    checks if a hand score = 21 and adds to player's money his bet + 1.5* bet and subtract 1.5*bet from dealer's money.
    
    """                  
    
    def player_blackjack_check(self,i):
        if self.hand_score_calc(self.player.hand,i) == 21:
            print('{} got a blackjack '.format(self.player.name))
            t.sleep(1.5)
            self.based_on_whats_on_table(i)
            self.player.money = self.player.money + (1.5 * self.player.bet[i]) + self.player.bet[i]
            self.dealer.money -= 1.5 *self.player.bet[i]
            self.player.bet[i] = 0
            self.player.hand_turn[i] = False
            if i == len(self.player.hand)-1:
                self.player.turn = False
            return True
        else:
            return False
    """
    ##################################################--player_standing--####################################################

    """ 
    def player_standing(self,i):
        print(actions[self.choice])
        self.player.standing(i)
        if i == (len(self.player.hand)-1):
            self.dealer.turn = True
    
    """
    ########################################--adding_cards_after_player_hand_splitting--####################################################

    """       
    def adding_cards_after_player_hand_splitting(self,i):
        print(actions[self.choice])
        if self.split_check(i):
            self.player.splitting(i)#player hand split 
        self.player.hit(self.deck.deal_one(),i)
        self.player.hit(self.deck.deal_one(),i+1)

    """
    ########################################--adding_cards_after_player_hand_splitting--####################################################

    """       
    def adding_cards_after_player_hand_splitting(self,i):
        print(actions[self.choice])
        if self.split_check(i):
            self.player.splitting(i)
        self.player.hit(self.deck.deal_one(),i)
        self.player.hit(self.deck.deal_one(),i+1)

    """
    ##################################################--double_down_check--####################################################
    This method checks if it is possible for the player to double down.
    Double down is possible:
    The player hand should only have 2 cards:
     -If player's hand score is 9 or 10.
     -If player's hand score is soft(contains Ace) 16, 17, or 18.
     -If player's hand score is 11.
    """    
    def double_down_check(self,i):
        if ((((self.hand_score_calc(self.player.hand,i) in (9,10) or
           (self.hand_score_calc(self.player.hand,i) in (16,17,18) and 
           (self.player.hand[i][0].rank=='A' or self.player.hand[i][1]=='A')))and len(self.player.hand[i])==2)or
            self.hand_score_calc(self.player.hand,i) == 11) and
            self.player.money >= self.player.bet[i]):
            self.player.bet[i]
            return True
        else:
            return False
    """
    ##################################################--Not_to_doubledown_check--####################################################
    This method checks if it is NOT GOOD IDEA for the player to double down.
    Double down is NOT RECOMMENDED:
    if The player hand have 2 cards and:
     -If dealer's hand face up card is an Ace.
     -If player's hand score is more than 11 and not contain an Ace.
    """    
    def Not_to_doubledown_check(self,i):
        if ((self.dealer.hand[0][0].rank == 'A' or (self.hand_score_calc(self.player.hand,i)>11 and
            (self.player.hand[i][0].rank!='A' or self.player.hand[i][1]!='A'))) and 
            (len(self.player.hand) == 2)):
            return True
        else:
            return False
        
    
    """
    ##################################################--insurance_check--####################################################
    This method lets the player bet on the dealer getting a blackjack as a side bet.
    """        
    def insurance_check(self):
        if ((self.dealer.hand[0][0].rank == 'A' and len(self.player.hand) == 1 and len(self.player.hand[0]) == 2) 
            and not self.player.insurance_flag):
            return True
        else:
            return False
        
        
    def surrender_check(self,i):
        if (((self.dealer.hand[0][0].rank in ('10','J','Q','K','A') and self.hand_score_calc in (12,13,14,15))
        or (self.dealer.hand[0][0].rank == 'A' and ((self.player.hand[0][0].rank == '8' or self.player.hand[0][1] == '8'))))
        and len(self.player.hand) == 2):
            return True
        else:
            return False
        
    """ 
    ##################################################--dealer_blackjack_check--####################################################
    checks if a hand score = 21 and adds to dealer's money player's bet and subtract it from player's money.
    Also if the player made and insurance bet, it will be paid back 2:1 with a total profit of 3X the
    insurance bet.
    This method is only used if the dealer has an Ace face up card.
    """                  
    
    def dealer_blackjack_check(self,i):
        if self.hand_score_calc(self.dealer.hand,0) == 21:
            self.dealer.turn = False
            new_table.dealer.card_status[1] = 'Face up'
            print('{} got a blackjack '.format(self.dealer.name))
            t.sleep(1.5)
            self.dealer.money += self.player.bet[i] 
            self.player.bet[i] = 0 
            self.dealer.turn = False
            if self.player.insurance_flag:#checks if the player made an insurance bet
                print('{} won the insurance bet.'.format(self.player.name))
                self.dealer.money -= 2*self.player.insurance_bet
                self.player.money += (3*self.player.insurance_bet)
                t.sleep(1.5)
            return True
        else:#if the dealer did not get a blackjack
            print('The dealer did not get a blackjack.')
            if self.player.insurance_flag:
                print('{} lost the insurance bet.'.format(self.player.name))
                self.dealer.money += self.player.insurance_bet
                t.sleep(1.5)
            return False
            
    """ 
    ##################################################--player_bust_check--########################################################
    Checks if a hand score > 21 and checks if the player has other hands if not, it ends player turn and strts dealers turn.
    """                 
    def player_bust_check(self,i):
        if self.hand_score_calc(self.player.hand,i) > 21:
            self.player.bust(self.dealer.money,i)
            print('{} hand is bust!'.format(self.player.name))
            t.sleep(1)
            
    """ 
    ##################################################--dealer_bust_check--########################################################
    This method checks if the dealers hand score is greater than 21, and ends dealer's turn in this case.
    """                 
    def dealer_bust_check(self):
        if self.hand_score_calc(self.dealer.hand,0) > 21:
            print('The dealer bust!')
            t.sleep(1)
            self.dealer.turn = False
            return True
        else:
            return False
    """ 
    ##################################################--hand_score_calc--########################################################
    This method calculates the total score of the active hand. ever card has one numerical score except Ace cards which can
    be 11 or 1 depending in the favourable score. If the total score with an Ace card is less 21 then the Ace card will has
    score of 11 otherwise 1.
    
    This method computes two sums: -low_sum which has Ace value of 1.
                                   -high_sum which has Ace value of 11.
    then each sum is checked if it is greater than 21.
    The highest Ace value is Favoured, thats why in the if statements it is checked first.
    
    Input:
         -hand: player or dealer's hands.
         -index: index of the active hand
                                   
    """                             
    def hand_score_calc(self,hand,index):
        hand_score = 0
        for i in range(len(hand[index])):
            if hand[index][i].rank != 'A':
                hand_score += hand[index][i].value
        for i in range(len(hand[index])):
            if hand[index][i].rank == 'A':
                small_value_flag = False
                high_value_flag = False
                low_sum = hand_score + 1
                high_sum = hand_score + 11
                if low_sum <= 21:
                    small_value_flag = True
                if high_sum <= 21:
                    high_value_flag = True  
                    
                if high_value_flag:
                    hand_score += 11
                elif small_value_flag:
                    hand_score += 1
        if 0 <= index < len(self.player.hand_score):
            self.player.hand_score[index] = hand_score
        else:
            self.player.hand_score.append(hand_score)
        return self.player.hand_score[index]  
    """ 
    ##############################################--player_choice--########################################################
    This method is used to get the proper input(integers) to select on of the six actions during player's
    turn. The input should be intgers only and between 1 and 6 including both ends.  
    """                 
    def player_choice(self):
        player_input = 'waiting'
        number = 0
        while (number > 6 or number < 1):
            player_input = input('choose a number that indicates your choice between 1 and 6:')
            if player_input.isdigit():
                number = int(player_input)
        return number

    """ 
    ##############################################--print_player_actions--########################################################
    This method select printing color for tha vailable actions which can be performed.
    color meaning:
    -white_color: The action can be performed but it is not recommended(might not induce high risk).
    -ornage_color: can be performed but at high risk of losing.
    -red_color: can't be performed since not all of the conditions are met.
    -green_color: highly recommended or the conditions are met for the action.
    """                 
    def print_player_actions(self,index):
#########################################--Hit & Stand color select--##############################################
        if self.player.turn and self.hand_score_calc(self.player.hand,index) in (4,5,6,7,8,9,10,11):
            hit_color = green_color
            stand_color = white_color
        elif self.player.turn and self.hand_score_calc(self.player.hand,index) in (12,13,14,15):
            hit_color = orange_color
            stand_color = orange_color
        elif ((self.player.turn and self.hand_score_calc(self.player.hand,index) >= 17) and
        self.hand_score_calc(self.player.hand,index) <= 20):
            hit_color = orange_color
            stand_color = green_color

        elif  not self.player.turn:
            hit_color = red_color
            stand_color = red_color
        else:
            hit_color = white_color
            stand_color = green_color
#####################################--Insurance color select--################################################
        if self.insurance_check():
            insurance_color = green_color
        else:
            insurance_color = red_color
#####################################--Split color select--#######################################################           
        if self.split_check(index):
            split_color = green_color
        else:
            split_color = red_color
######################################--Double down color select--######################################################           
        if self.double_down_check(index):
            double_down_color = green_color

        elif self.Not_to_doubledown_check(index):
            double_down_color = orange_color

        elif len(self.player.hand[index]) > 2 or not self.double_down_check(index):
            double_down_color = red_color
#######################################--surrender color select--#######################################
        if self.surrender_check(index):
            surrender_color = green_color
        else:
            surrender_color = red_color
#########################################################################################################
        print('{}1-Hit{}          {}2-Stand{}\n{}3-Insurance{}    {}4-Split{}\n{}5-Double down{}  {}6-Surrender{}'
              .format(hit_color, black_color, stand_color, black_color, insurance_color, black_color,
                      split_color, black_color, double_down_color, black_color, surrender_color, black_color))
    """ 
    ########################################--based_on_whats_on_table--########################################################
    This method will print the table containing money chips for the dealer, dealer's hand,
    dealer's hand score, player's hand, player's hand score, player's bet chips, player's money
    chips, player's actions, number of hands, and status messages.
    """                 
    def based_on_whats_on_table(self,index,flag):
        clear_output(wait=False)
        t.sleep(0.5)
        print('Dealer\'s Money:')
        self.print_chips_on_table(self.convert_money_to_chip(self.dealer.money,True))
        self.print_card_on_table(self.dealer.hand,self.dealer.card_status,0)
        if self.dealer.card_status[1] == 'Face up':
            print(self.hand_score_calc(self.dealer.hand,0))
        print('\n')
        self.print_card_on_table(self.player.hand,self.player.card_status,index)
        print(self.hand_score_calc(self.player.hand,index))
        print('\nPlayer\'s Bet:')
        self.print_chips_on_table(self.convert_money_to_chip(self.player.bet[index],False))
        print('Player\'s Money:')
        self.print_chips_on_table(self.convert_money_to_chip(self.player.money,True))
        self.print_player_actions(index)
        if len(self.player.hand) == 1:
            print('Player has {} hand'.format(len(self.player.hand)))
        else:
            print('Player has {} hands'.format(len(self.player.hand)))
        if (self.dealer.card_status[1] == 'Face down' 
        and self.hand_score_calc(self.player.hand,index) < 21 and flag):
            return self.player_choice()
    """ 
    #########################################--yes_or_no--################################################                          
      input: NONE.
      output: boolean value.
      notes: this function is used to continue playing or not. It only accepts 'Y' or 'N' as answers.
      A simple user validation messaging is implemented to help the use provide correct answer represenring 
      his decision. Also the game will be stopped if the player has no more money.
    """ 
    def yes_or_no(self):
        if self.player.money > 0:
            answer = 'wrong'
            while answer != 'Y' and answer != 'N':
                answer = input('Do you want to deal again?(Y/N)').capitalize()
                if answer != 'N' and answer != 'Y':
                    print('Please only answer with "y" or "n"')
                    clear_output(wait=True)
            if answer == 'N':
                return False
            else:
                self.dealer.hand[0].clear()
                self.player.bet.clear()
                for i in range(len(self.player.hand)):
                    self.player.hand[i].clear()
                return True 
        else:
            print("You don't have money! Get out")
            return False
    """
    """
    def game_logic(self):
        while self.playing:
            if self.player.money > 0:
                self.player.hand = [[]]
                self.player.bet = ['0']
                self.player.last_action = ['']
                self.player.insurance_bet = 0
                self.player.insurance_flag = False
                self.deck.shuffle()
                self.player.turn = True
                self.dealer.turn = True
                self.player.hit(self.deck.deal_one(),0)
                self.dealer.hit(self.deck.deal_one(),self.hand_score_calc(new_dealer.hand,0))
                self.player.hit(self.deck.deal_one(),0)
                self.dealer.hit(self.deck.deal_one(),self.hand_score_calc(new_dealer.hand,0))
                self.dealer.turn = False
                self.dealer.card_status[1] = 'Face down'
                self.player.place_a_bet(0)
                just_print = False
                return_action = True
                i = 0
                j = 0
                number_of_actions = 0#used to allow the player to choose single action befor the dealer
                #checks for blackjack
#----------------------------------------------------Player turn---------------------------------------------------------------#
                """
                """           
                while self.player.turn:
                    while i < len(self.player.hand):
                        self.player.hand_turn[i] = True
                        while self.player.hand_turn[i]:
                            if number_of_actions == 1:
                                if self.dealer.will_check_face_down_card():
                                    if self.dealer_blackjack_check(i):
                                        self.based_on_whats_on_table(i,just_print)
                                        self.player.hand_turn[i] = False
                                        if i == len(self.player.hand)-1:
                                            self.player.turn = False
                                            break
                            if self.hand_score_calc(player1.hand,i) < 21:
                                if self.player_bust_check(i):
                                        self.based_on_whats_on_table(i,just_print)

                                elif self.player_blackjack_check(i):
                                    self.based_on_whats_on_table(i,just_print)
                                self.choice = self.based_on_whats_on_table(i,return_action)
###################################################--Hit--########################################################################
                                if actions[self.choice] == 'hit':
                                    print(actions[self.choice])
                                    player1.hit(self.deck.deal_one(),i)
                                    #self.based_on_whats_on_table(i,just_print)
###################################################--Stand--######################################################################
                                elif actions[self.choice] == 'stand':
                                    self.player_standing(i)
                                    #self.based_on_whats_on_table(i,just_print)
###################################################--Split--#####################################################################
                                elif actions[self.choice] == 'split' and self.split_check(i):
                                    self.adding_cards_after_player_hand_splitting(i)
                                    #self.based_on_whats_on_table(i,just_print)
#################################################--Double down--##################################################################
                                elif ((actions[self.choice] == 'double down') and 
                                (self.double_down_check(i) or self.Not_to_doubledown_check(i))):
                                    print(actions[self.choice])
                                    self.player.double_down(self.deck.deal_one(),i)
                                    self.dealer.turn = True
                                    self.based_on_whats_on_table(i,just_print)
##################################################--Insurance--####################################################################
                                elif actions[self.choice] == 'insurance' and self.insurance_check():
                                    self.player.insurance(i)
                                    #self.based_on_whats_on_table(i,just_print)
##################################################--Surrender--###################################################################
                                elif actions[self.choice] == 'surrender':
                                    print(actions[self.choice])
                                    self.player.surrender(self.dealer.money,i)
                                    self.dealer.turn = False
                                    #self.based_on_whats_on_table(i,just_print)
###########################################--If the action is not possible--###################################################################                                
                                else:
                                    print('The conditions for {} are not met'.format(actions[self.choice]))
                                    t.sleep(2)
                                if i <= len(self.player.last_action):
                                    self.player.last_action[i] = actions[self.choice]
                                else:
                                    self.player.last_action.append(actions[self.choice])
#############################################--If player score >= 21--##################################################
                            elif self.player_blackjack_check(i):
                                pass
                                #self.based_on_whats_on_table(i,just_print)
                            else:
                                self.player_bust_check(i)
                                #self.based_on_whats_on_table(i,just_print)
                            number_of_actions += 1
                        i+=1
                        t.sleep(2)
#-------------------------------------------------Dealer turn-------------------------------------------------------------------#
                    for j in range(len(self.player.hand)):
                        if self.player.last_action[j] != 'surrender':
                            self.dealer.card_status[1] = 'Face up'
                            while self.dealer.turn and self.hand_score_calc(self.player.hand,j) < 21: 
                                if self.dealer_bust_check():
                                    pass
                                elif self.dealer_blackjack_check(j):
                                    pass
                                elif self.hand_score_calc(self.player.hand,j) != 21:
                                    self.based_on_whats_on_table(j,just_print)
                                    the_other_action = self.dealer.hit(self.deck.deal_one(),
                                                                            self.hand_score_calc(self.dealer.hand,0))
                                    if the_other_action:
                                        self.dealer.standing(self.hand_score_calc(self.dealer.hand,0))
                                    t.sleep(2)
                                else:
                                    self.dealer.turn = False
                        else:
                            pass            
#-------------------------------------------------Final score----------------------------------------------------------------------#
                    for j in range(len(self.player.hand)):
                        if self.player.last_action[j] != 'surrender':
                            if (self.hand_score_calc(self.player.hand,j)) != 21: 
                                self.based_on_whats_on_table(j,just_print)
##############################################################################################################################
                                if ((self.hand_score_calc(self.dealer.hand,0) < self.hand_score_calc(self.player.hand,j) 
                                    or self.hand_score_calc(self.dealer.hand,0) > 21) and self.hand_score_calc(self.player.hand,j) < 21 ):
                                    print('{} won'.format(self.player.name))
                                    self.player.money += 2 * self.player.bet[j]
                                    self.dealer.money -= self.player.bet[j]
                                    self.player.bet[j] = 0
                                    t.sleep(5)
############################################################################################################################
                                elif self.hand_score_calc(self.dealer.hand,0) == self.hand_score_calc(self.player.hand,j):
                                    print('Stand off! The bet is returnd to {}. Nobody wins.'.format(self.player.name))
                                    self.player.money += self.player.bet[j]
                                    self.player.bet[j] = 0
############################################################################################################################
                                else:
                                    print('{} lost'.format(self.player.name))
                                    self.dealer.money += self.player.bet[j]
                                    self.player.bet[j] = 0
                                    t.sleep(5)
                        else:
                            pass
###########################################################################################################################
                self.print_chips_on_table(self.convert_money_to_chip(self.player.money,True))
                self.print_chips_on_table(self.convert_money_to_chip(self.dealer.money,True))
                self.playing = self.yes_or_no()
                self.deck = Deck()
            else:
                print("You don't have money! Get out!")
                self.playing = False

#---------------------------------------------------THE-GAME--------------------------------------------------------------#
new_dealer =  Dealer()
player1 = Player('Luai',1000)
new_table = Table(player1, new_dealer,Deck())
new_table.game_logic()


# In[ ]:





# In[ ]:




