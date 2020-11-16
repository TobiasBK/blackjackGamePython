#Blackjack Game for Python

import random

def main():

    playerCards = []
    dealerCards = []

    while len(playerCards) != 2:
        playerCards.append(random.randint(1, 11))
        if len(playerCards) == 2:
            print("You have ", playerCards)

    while len(dealerCards) != 2:
        dealerCards.append(random.randint(1, 11))
        if len(dealerCards) == 2:
            print("Dealer has X &", dealerCards[1])
    
   #summing the cards
    if sum(dealerCards) == 21:
        print("Dealer has 21 and wins!")
    elif sum(dealerCards) > 21:
        print("Dealer has busted!")

    while sum(playerCards) < 21:
        action = str(input("stay or hit?  "))
        if action == "hit":
            playerCards.append(random.randint(1, 11))
            print("You're total is " + str(sum(playerCards)) + " from these cards ", playerCards)
        else:
            print("The dealer's total is " + str(sum(dealerCards)) + " with ", dealerCards)
            print("You're total is " + str(sum(playerCards)) + " with ", playerCards)
            if sum(dealerCards) > sum(playerCards):
                print("Dealer wins!")
            else:
                print("You win!")
                break

    if sum(playerCards) > 21:
        print("That's a BUST. Dealer wins.")
    elif sum(playerCards) == 21:
        print("BLACKJACK! You Win!")

main()
