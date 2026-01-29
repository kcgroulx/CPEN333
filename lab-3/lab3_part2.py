#student name: Kyle Groulx
#student number: 95104774

import multiprocessing

def checkList(list_to_check: list) -> bool:
    """
    param list_to_check: a list

    Returns True if and only if the list contains exactly the digits 1-9 each once.
    Returns False if the list has the wrong length, contains non-integers,
    or has duplicates/missing values.
    This function does not mutate the input list.
    This function serves as an agnostic way to check if a list follows valid sudoku rules.
    """
    # Check len of list
    if len(list_to_check) != 9:
        return False
    # Check if all values in list are ints
    if not all(type(x) is int for x in list_to_check):
        return False
    # Sort list and check if it contains the values 1-9
    sorted_list = sorted(list_to_check)
    for i in range(1, 10):
        if sorted_list[i - 1] != i:
            return False

    # Valid list
    return True

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Extract column from puzzle
    columnList = []
    for row in puzzle:
        columnList.append(row[column])

    # Check if the extracted column is valid and print
    valid = ""
    if checkList(columnList):
        valid = "valid"
    else:
        valid = "not valid"
    print(f"Column {column} {valid}")

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Check if the row is valid and print
    valid = ""
    if checkList(puzzle[row]):
        valid = "valid"
    else:
        valid = "not valid"
    print(f"Row {row} {valid}")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    # Get row and col offsets based off the subgrid index
    row_offset = (subgrid // 3) * 3
    col_offset = (subgrid % 3) * 3
    
    # Extract subgrid into a list
    subgridList = []
    for row in range (0,3):
        for col in range (0,3):
            subgridList.append(puzzle[row + row_offset][col + col_offset])

    # Check if extracted subgrid is valid and print
    valid = ""
    if checkList(subgridList):
        valid = "valid"
    else:
        valid = "not valid"
    print(f"Subgrid {subgrid} {valid}")


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    test3 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [8, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 3 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, "hello world", 4, 1.0, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 50 ]
            ]
    test4 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    
    testcase = test2   #modify here for other testcases
    SIZE = 9

    processes = []

    for col in range(SIZE):  #checking all columns
        process = multiprocessing.Process(target=checkColumn, args=(testcase, col))
        processes.append(process)
        process.start()

    for row in range(SIZE):  #checking all rows
        process = multiprocessing.Process(target=checkRow, args=(testcase, row))
        processes.append(process)
        process.start()

    for subgrid in range(SIZE):   #checking all subgrids
        process = multiprocessing.Process(target=checkSubgrid, args=(testcase, subgrid))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
