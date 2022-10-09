import random

Spades = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Hearts = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Diamonds = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Clubs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

hand = random.sample(cards, 5)
print(hand)


# Create a 2D array to store all suits of cards


# Function checks whether 2 lists have the same elements regardless of order
def check_Same_contents(hand):

  royalFlush = [cards[0], cards[8], cards[9], cards[10], cards[11], cards[12]]

  for x in set(hand + royalFlush):
    if hand.count(x) != royalFlush.count(x):
        return False
    return True



# Function to check the type of hand that has been dealt
def HandType(hand):

  royalFlush = [cards[0], cards[8], cards[9], cards[10], cards[11], cards[12]]

  FourKind = ["2", "2", "2", "2", "2"]

  Straight = ["10", "9", "8", "7", "6"]

  Flush = [] 
  

  
  
  
    
  if hand == royalFlush:
    print("You have a royal flush")

  if hand == Straight:
    print("You have a straight")

  if hand == FourKind:
    print("You have four of a kind")

  if hand == Flush:
    print("You have a Flush")

  
HandType(hand)

