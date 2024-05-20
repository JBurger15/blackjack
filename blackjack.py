# -*- coding: utf-8 -*-
"""BlackJack.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QCtT-kA3mZ3lq8v37pyxxFXfGL3-vGQT
"""

import random
#To end game place bet of zero or less
#Program does not ask for splits, double downs, insurance, all aces play as 11
def game(buyin):
  deck = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  stack = buyin
  play = "y"
  bet = 1
  while bet > 0:
    if stack == 0:
      print("Player lost:(\nCome again soon!")
      bet = 0
      break
    outcome = ""
    bet = int(input("-----------------------------------------\nPlease place your bet: "))
    if bet < 0:
      print("You left the table with " + str(stack) + ". Come again soon!")
      break
    playerhand = []
    dealerhand = []
    while bet > stack or bet < 5:
      if bet < 5:
        print("There is a $5 minimum bet...")
      if bet > stack:
        print("You do not have sufficient funds...")
      bet = input("Please place your bet: ")
    print("-----------------------------------------\nDealing now...")
    playerhand.append(deck[random.randint(0, 12)])
    dealerhand.append(deck[random.randint(0, 12)])
    playerhand.append(deck[random.randint(0, 12)])
    dealerhand.append(deck[random.randint(0, 12)])
    playersum = (playerhand[0] + playerhand[1])
    dealersum = (dealerhand[0] + dealerhand[1])
    print("Player is playing a " + str(playersum) + "\nAgainst a dealer " + str(dealerhand[0]))
    if playersum == 21:
      print("Player has Black Jack!")
      bet = (bet * 1.5)
      outcome = "w"
    elif dealersum == 21:
      print("Dealer has Black Jack!")
      outcome = "l"
    else:
      hors = input("-----------------------------------------\nWould you like to hit or stand?(h/s): ")
      while hors.lower() == "h":
        playerhand.append(deck[random.randint(0, 12)])
        playersum = (playersum + playerhand[-1])
        print("Player has " + str(playersum))
        if playersum > 21:
          hors = "s"
          print("Player busts!")
          outcome = "l"
          continue
        else:
          hors = input("-----------------------------------------\nWould you like to hit or stand?(h/s): ")
      if playersum > 21:
        stack -= bet
        print("You have " + str(stack) + " in your stack.")
        continue
      elif hors.lower() == "s":
        print("Dealer has " + str(dealersum))
        if dealersum > 16:
          print("Dealer stays...")
          if dealersum > playersum:
            print("Dealer wins...")
            outcome = "l"
          elif dealersum < playersum:
            print("Player wins!")
            outcome = "w"
          else:
            print("Push!")
        else:
          while dealersum < 17:
            print("Dealer hits...")
            dealerhand.append(deck[random.randint(0, 12)])
            dealersum += dealerhand[-1]
            print(dealersum)
          if dealersum > 21:
            print("Dealer busts!")
            outcome = "w"
          elif dealersum > playersum:
            print("Dealer wins...")
            outcome = "l"
          elif dealersum < playersum:
            print("Player wins!")
            outcome = "w"
          else:
            print("Push!")
    if outcome == "w":
      stack += bet
    elif outcome == "l":
      stack -= bet
    else:
      None
    print("You have " + str(stack) + " in your stack.")

    # print("-----------------------------------------")











def main():
  buyin = 0
  print("\t\t    Welcome to Black Jack!\n\tDealer stays on soft 17 and pays black jack 3:2...\n")
  buyin = int(input("How much would you like to buy in for? "))
  print("Changing " + str(buyin) + "!")
  game(buyin)

main()