# student name: Kyle Groulx
# student number: 95104774

# A command-line 2048 game

import random

board: list[list] = []  # a 2-D list to keep the current status of the game board

def init() -> None:  # Use as is
    """ 
        initializes the board variable
        and prints a welcome message
    """
    # initialize the board cells with ''
    for _ in range(4):     
        rowList = []
        for _ in range(4):
            rowList.append('')
        board.append(rowList)
    # add two starting 2's at random cells
    twoRandomNumbers = random.sample(range(16), 2)   # randomly choose two numbers between 0 and 15   
    # correspond each of the two random numbers to the corresponding cell
    twoRandomCells = ((twoRandomNumbers[0]//4,twoRandomNumbers[0]%4),
                      (twoRandomNumbers[1]//4,twoRandomNumbers[1]%4))
    for cell in twoRandomCells:  # put a 2 on each of the two chosen random cells
        board[cell[0]][cell[1]] = 2

    print(); print("Welcome! Let's play the 2048 game."); print()


def displayGame() -> None:  # Use as is
    """ displays the current board on the console """
    print("+-----+-----+-----+-----+")
    for row in range(4): 
        for column in range(4):
            cell = board[row][column] 
            print(f"|{str(cell).center(5)}", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def promptGamerForTheNextMove() -> str: # Use as is
    """
        prompts the gamer until a valid next move or Q (to quit) or E (to shuffle) is selected
        (valid move direction: one of 'W', 'A', 'S' or 'D')
        returns the user input
    """
    print("Enter one of WASD (move direction) or Q (to quit) or E (to shuffle board)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'Q', 'E'): # a valid move direction or 'Q'
            break
        print('Enter one of "W", "A", "S", "D", or "Q" or "E" to shuffle') # otherwise inform the user about valid input
    return move

def addANew2Or4ToBoard() -> None:
    """ 
        Adds a new 2 or 4 to the board.
        Selects a spot that has the greatest difference in value with neighbouring cells.
        This make it harder to immediately do a slide/merge
    """
    # Randomly choose between 2 and 4 with a weight of 2/3 for 2
    new_value = 2 if random.random() < (2/3) else 4

    # Find the empty cell that would have the largest difference in value with the new 2 or 4. 
    largest_difference = -1
    row, col = None, None
    for r in range(4):
        for c in range(4):
            if board[r][c] != '':
                continue

            neighbor_diffs = []
            # Up
            if r - 1 >= 0 and board[r - 1][c] != '':
                neighbor_diffs.append(abs(new_value - board[r - 1][c]))
            # Down
            if r + 1 < 4 and board[r + 1][c] != '':
                neighbor_diffs.append(abs(new_value - board[r + 1][c]))
            # Left
            if c - 1 >= 0 and board[r][c - 1] != '':
                neighbor_diffs.append(abs(new_value - board[r][c - 1]))
            # Right
            if c + 1 < 4 and board[r][c + 1] != '':
                neighbor_diffs.append(abs(new_value - board[r][c + 1]))

            smallest_difference = min(neighbor_diffs) if neighbor_diffs else 0

            if smallest_difference > largest_difference:
                largest_difference = smallest_difference
                row, col = r, c

    # Set the new value at the found row and col if they are found (board has some empty cells)
    if row is not None and col is not None:
        board[row][col] = new_value


def isFullAndNoValidMove() -> bool:
    """ 
        returns True if no empty cell is left, False otherwise 
    """
    # Iterate through the board and check for any empty cells
    for row in board:
        for cell in row:
            if cell == '':
                return False

    # Check if there are any rows with adjacent cells that have the same number  
    for row in range(4):
        for col in range(3):
            if board[row][col] == board[row][col + 1]:
                return False

    # Check if there are any cols with adjacent cells that have the same number
    for col in range(4):
        for row in range(3):
            if board[row][col] == board[row + 1][col]:
                return False

    # No empty cells found and no valid move found
    return True

def getCurrentScore() -> int:
    """
        calculates and returns the current score
        the score is the sum of all the numbers currently on the board
    """
    score = 0
    for row in board:
        for cell in row:
            if cell != '':
                score += cell

    return score

def updateTheBoardBasedOnTheUserMove(move: str):
    """
        updates the board variable based on the move argument by sliding and merging
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right

    """
    # Steps to update each board
    # 1. For each row/col (depending on WASD). Get a list that contains the row/col WITHOUT any empty cells
    # 2. Iterate through the list and merge any cells that are the same number and adjacent to each other
    # 3. Pad the front or end of the list with empty cells (depending on WASD)

    if move == 'A': # left
        for row in range(4):
            line = [cell for cell in board[row] if cell != '']
            merged = []
            cell = 0
            while cell < len(line):
                if cell + 1 < len(line) and line[cell] == line[cell + 1]:
                    merged.append(line[cell] * 2)
                    cell += 2
                else:
                    merged.append(line[cell])
                    cell += 1
            merged += [''] * (4 - len(merged))
            board[row] = merged
    elif move == 'D': # right
        for row in range(4):
            line = [cell for cell in board[row] if cell != '']
            line.reverse() # Reverse since we are shifting from left to right
            merged = []
            cell = 0
            while cell < len(line):
                if cell + 1 < len(line) and line[cell] == line[cell + 1]:
                    merged.append(line[cell] * 2)
                    cell += 2
                else:
                    merged.append(line[cell])
                    cell += 1
            merged += [''] * (4 - len(merged))
            merged.reverse() # Reverse again to proper order
            board[row] = merged
    elif move == 'W': # up
        for col in range(4):
            line = []
            for row in range(4):
                if board[row][col] != '':
                    line.append(board[row][col])
            merged = []
            cell = 0
            while cell < len(line):
                if cell + 1 < len(line) and line[cell] == line[cell + 1]:
                    merged.append(line[cell] * 2)
                    cell += 2
                else:
                    merged.append(line[cell])
                    cell += 1
            merged += [''] * (4 - len(merged))
            for row in range(4):
                board[row][col] = merged[row]
    elif move == 'S': # down
        for col in range(4):
            line = []
            for row in range(4):
                if board[row][col] != '':
                    line.append(board[row][col])
            line.reverse()
            merged = []
            cell = 0
            while cell < len(line):
                if cell + 1 < len(line) and line[cell] == line[cell + 1]:
                    merged.append(line[cell] * 2)
                    cell += 2
                else:
                    merged.append(line[cell])
                    cell += 1
            merged += [''] * (4 - len(merged))
            merged.reverse()
            for row in range(4):
                board[row][col] = merged[row]


#up to two new functions allowed to be added (if needed)
#as usual, they must be documented well
#they have to be placed below this line

def shuffleBoard() -> None:
    """
        Randomly shuffles all values on the board
        This allows user to possible get out of a position if they are stuck
    """
    # Flatten board into single list and shuffle it randomly
    flattenBoard = [cell for row in board for cell in row]
    random.shuffle(flattenBoard)

    # Iterate through the board and set it to the flattened shuffled list
    for row in range(len(board)):
        for col in range(len(board[0])):
            board[row][col] = flattenBoard[row * 4 + col]


if __name__ == "__main__":  # Use as is  
    init()
    displayGame()
    while True:  # Super-loop for the game
        print(f"Score: {getCurrentScore()}")
        userInput = promptGamerForTheNextMove()
        if(userInput == 'Q'):
            print("Exiting the game. Thanks for playing!")
            break

        if(userInput == "E"):
            shuffleBoard()
        
        updateTheBoardBasedOnTheUserMove(userInput)
        addANew2Or4ToBoard()

        displayGame()

        if isFullAndNoValidMove(): #game is over once all cells are taken
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break
