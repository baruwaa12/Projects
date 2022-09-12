

# Creating a board 

board = [["_", "_", "_"],
         ["_", "_", "_"]
         ["_", "_", "_"]
]

# Ask the two opponents who they want to be.
# Noughts or Crosses
# Player 1 = Noughts
# Player 2 = Crosses

player1 = input("W")


## Function to print board to CLI

def printBoard(board):

  # Loop through each element in board array and print another board on the 
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()
    



printBoard(board)


def quit(user_input):
  if user_input == "q": return False
  else: return True 

while True:
  user_input input("Please enter a position 1 through 9 \")