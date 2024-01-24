# Video alternative: https://youtu.be/Y-6WZfJ9I6c&t=1054s

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.
# Completed

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.
# Completed

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.
# Completed

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!

moves_made = 0

def play_game(n):
  board = [["." for col in range(n)] for row in range(n)]
  player = "X"
  while not is_game_over(board, n) and moves_made < n*n:
    print(not is_game_over(board, n) and moves_made < n*n)
    print(print_board(board))
    print("It's " + player + "'s turn.")
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    board = make_move(board, row, column, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(print_board(board))
  print("Game over!")

def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, row, column, player):
  if board[row][column] != ".":
    print("Place already occupied, Try Again!")
    row = int(input("Enter a row: "))
    column = int(input("Enter a column: "))
    make_move(board, row, column, player)
  board[row][column] = player
  global moves_made
  moves_made += 1
  return board


# This function will extract three cells from the board
def get_cells(board, coords):
  return [board[coord[0]][coord[1]] for coord in coords]

# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, group):
  cells = get_cells(board, group)
  return "." not in cells
  

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, coords):
  cells = get_cells(board, coords)
  return len(set(cells)) == 1

# We'll make a list of groups to check:

def groups_to_check(n):
  group_rows = [[(i, j) for j in range(n)] for i in range(n)]

  group_columns = [[(i, j) for i in range(n)] for j in range(n)]

  group_diagonal1 = [[(i, i) for i in range(n)]]

  group_diagonal2 = [[(n-1-i, i) for i in range(n)]]

  all_groups = group_rows + group_columns + group_diagonal1 + group_diagonal2

  return all_groups



def is_game_over(board, n):
  all_groups = groups_to_check(n)
  # We go through our groups
  for group in all_groups:
    # If any of them are empty, they're clearly not a
    # winning row, so we skip them.
    if is_group_complete(board, group):
      if are_all_cells_the_same(board, group):
        return True # We found a winning row!
        # Note that return also stops the function
  return False # If we get here, we didn't find a winning row

# And test it out:

print("Game time!")
n = int(input("What size of board do you want? "))
play_game(n)
