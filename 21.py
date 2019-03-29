import os, sys
import random

cards = [ 2, 2, 2, 2,
          3, 3, 3, 3,
          4, 4, 4, 4,
          5, 5, 5, 5,
          6, 6, 6, 6,
          7, 7, 7, 7,
          8, 8, 8, 8,
          9, 9, 9, 9,
          10, 10, 10, 10,
          11, 11, 11, 11,
          12, 12, 12, 12,
          13, 13, 13, 13,
          14, 14, 14, 14]

random.shuffle(cards)
player = 0
dealer = 0
    


def mana(player):
    hand = []
    for i in range(2):
        random.shuffle(cards)
        card = cards.pop()
        if card == 11:card = "A"
        if card == 12:card = "J"
        if card == 13:card = "Q"
        if card == 14:card = "K"
        hand.append(card)
    return hand

def hit_cards(hand):
    #if card == 11:card = "A"
    #if card == 12:card = "J"
    #if card == 13:card = "Q"
    #if card == 14:card = "K"
    human = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            human = human + 10
        elif card == "A":
            if human >= 11: human = human + 1
            else: human = human + 11
        else:
            human = human + card

    return human

def game(p_hand, d_hand):
    if hit_cards(p_hand) == 21:
        print("player has: ", p_hand)
        print("dealer has: ", d_hand)
        print("bravo, ai castigat!")
        alegere = input("do you want to play again?  y/n ")
        if alegere == "y":
            reset()
        else:
            print("papa")
            exit()

    if hit_cards(d_hand) == 21:
        print("player has: ", p_hand)
        print("dealer has: ", d_hand)
        print("dealerul a castigat!")
        alegere = input("do you want to play again?  y/n ")
        if alegere == "y":
            reset()
        else:
            print("papa")
            exit()

    if hit_cards(p_hand) > 21:
        clear()
        print("player has: ", p_hand)
        print("dealer has: ", d_hand)
        print("player busted")
        reset()
    
    if hit_cards(d_hand) > 21:
        clear()
        print("player has: ", p_hand)
        print("dealer has: ", d_hand)
        print("dealer busted")
        reset()


def play():
    alegere = 0
    print("les play")
    p_hand = mana(cards)
    d_hand = mana(cards)
    while alegere != "q":
        print("player has: ", p_hand)
        print("dealer has: ", d_hand)
        game(p_hand, d_hand)
        alegere = input("do you want to hit or stand?  y/n ")
        if alegere == "y":
            hit(p_hand)
            game(p_hand, d_hand)
        elif alegere == "n":
            hit(d_hand)
            game(p_hand, d_hand)
        elif alegere == "q":
            print("papa")
            exit()

def hit(hand):
    card = cards.pop()
    if card == 11:card = "A"
    if card == 12:card = "J"
    if card == 13:card = "Q"
    if card == 14:card = "K"
    hand.append(card)
    return hand

    
def clear():
    if os.name == 'posix':
        os.system('clear')

def reset():
    restart = input("do you want to play again?  y/n ")
    if restart == "y":
        player = 0
        dealer = 0
        cards = [ 2, 2, 2, 2,
          3, 3, 3, 3,
          4, 4, 4, 4,
          5, 5, 5, 5,
          6, 6, 6, 6,
          7, 7, 7, 7,
          8, 8, 8, 8,
          9, 9, 9, 9,
          10, 10, 10, 10,
          11, 11, 11, 11,
          12, 12, 12, 12,
          13, 13, 13, 13,
          14, 14, 14, 14]
        play()
    else:
        print("papa")
        exit()


play()
