

# Creating a board 

board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"],
]

# Ask the two opponents who they want to be.
# Noughts or Crosses
# Player 1 = Noughts
# Player 2 = Crosses



## Function to print board to CLI
def printBoard(board):

  # Loop through each element in board array and print another board on the 
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()
    

# Function so the user can use the Q key to quit the game
def quit(user_input):
  if user_input == "q": 
    print("Thanks for playing")
    return True
  else: 
    return False

    
# Function that checks if user input is inbetween set boundaries
def bounds(user_input):
  if user_input > 9 or user_input < 1:
    return False
  else:
    return True

    
# Function to check if input is a number
def check_Input(user_input):
  
  if not isNum(user_input):
    return False
  user_input = int(user_input)
  if not bounds(user_input):
    return False

    
# Check if the user input is a valid integer
def isNum(user_input):
  if not user_input.isnumeric():
    print("This is not a valid number")
    return False
  else:
    return True


# Function to check if a space has been taken
def placeTaken(coords, board):
  row = coords[0]
  col = coords[1]
  if board[row[c]]


# Function to determine coordinates 
def coordinates(user_input):
  row = int(user_input / 3)
  col = user_input
  if col > 2:
    col = int(col % 3)
    return (row, col)
  

def add_to_board(coords, board, active_user):
  row = coords[0]
  col = coords[1]
  board[row][col] = active_user

def current_user(user):
  if user: return "x"
  else: return "o"

def isWin(user, board):
  if check_row(user, board): return True
  if check_col(user, board): return True
  if check_diag(user, board): return True
  return False


def check_row(user, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != user:
        complete_row = False
        break
    if complete_row: return True
  return False 

def check_column(user, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False

def check_diag(user, board):
  #top left to bottom right
  if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
  elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
  else: return False


  ## Loop which prints the board after each user input
while turns < 9:
  active_user = current_user(user)
  print_board(board)
  user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit:")
  if quit(user_input): break
  if not check_input(user_input):
    print("Please try again.")
    continue
  user_input = int(user_input) - 1
  coords = coordinates(user_input)
  if istaken(coords, board):
    print("Please try again.")
    continue
  add_to_board(coords, board, active_user)
  if iswin(active_user, board): 
    print(f"{active_user.upper()} won!")
    break
  
  turns += 1
  if turns == 9: print("Tie!")
  user = not user
