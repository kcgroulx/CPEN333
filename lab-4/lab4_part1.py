#student name:
#student number:

import threading

import random # Used for testing

# Simple merge sort algorithm
# Based from here: https://www.geeksforgeeks.org/dsa/merge-sort/
# nlog(n) Time complexity
def merge_sort(arr):
    # Return once we divide into a single element
    if len(arr) == 1:
        return arr

    # Recursivly call merge_sort for left and ride side of the list
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    # Merge step
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append leftovers
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    global sortedFirstHalf
    global sortedSecondHalf
    middle = len(testcase) // 2

    if firstHalf == True:
        sortedFirstHalf = merge_sort(testcase[:middle])
    else:
        sortedSecondHalf = merge_sort(testcase[middle:])

    

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    i_firstHalf = 0
    i_secondHalf = 0
    global sortedFirstHalf
    global sortedSecondHalf
    global SortedFullList

    # Create two pointers that start at the beginning of the sorted half lists.
    # Check which is smaller and append that to the SortedFullList
    while i_firstHalf < len(sortedFirstHalf) and i_secondHalf < len(sortedSecondHalf):
        if sortedFirstHalf[i_firstHalf] < sortedSecondHalf[i_secondHalf]:
            SortedFullList.append(sortedFirstHalf[i_firstHalf])
            i_firstHalf += 1
        else:
            SortedFullList.append(sortedSecondHalf[i_secondHalf])
            i_secondHalf += 1

    # Check which index is smaller and append the remaining of the other half list to the SortedFullList
    # i_firstHalf and i_secondHalf cannot be equal after the while loop above

    if i_firstHalf < i_secondHalf:
        SortedFullList += sortedFirstHalf[i_firstHalf:]
    else:
        SortedFullList += sortedSecondHalf[i_secondHalf:]
   

if __name__ == "__main__":
    
    # Specific test cases
    testcase1 = [0,-1,10,-3,2,99,12,1]
    testcase2 = [8,5,7,7,4,1,3,2]
    testcase3 = [5,-2,0,5,-2,3,3,1]
    testcase4 = [100,50,-100,0,25,-25,75,-75]
    testcase5 = []
    testcase6 = [42]
    testcase7 = [3,2,-1]
    testcase8 = [8,7,6,5,4,3,2,1]
    testcase9 = [
        73, -4, 19, 0, 88, -15, 42, 7, -91, 33,
        5, 5, -60, 24, 18, -2, 99, -37, 61, 11,
        -8, 56, 3, -77, 29, 14, -50, 1, 72, -6,
        40, 9, -12, 68, -30, 22, 4, -99, 81, 16,
        -23, 58, 2, -45, 36, 27, -5, 90, -71, 13,
        6, -18, 47, 31, -33, 64, -1, 84, 21, -10,
        52, -26, 8, 70, -40, 25, 12, -63, 97, 15,
        -7, 59, 20, -55, 34, 28, -3, 76, -82, 10,
        44, -14, 62, 17, -28, 66, -9, 86, 23, -20,
        54, -32, 30, -48, 38, 26, -11, 92, -70, 35
    ]
    
    # Randomly generated test case
    randomTestcase = [random.randint(-100000, 100000) for i in range(1000)]

    # Shared variables
    testcase = randomTestcase
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
 
    # Threads
    t1 = threading.Thread(target=sortingWorker, args=(True,))
    t2 = threading.Thread(target=sortingWorker, args=(False,))
    t3 = threading.Thread(target=mergingWorker)

    # Start sorting threads
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Start merge thread
    t3.start()
    t3.join()

    # Print the sorted list
    print("The final sorted list is ", SortedFullList)

    # Verify if my implementation is correct
    print("Successful sort:", sorted(testcase) == SortedFullList)
