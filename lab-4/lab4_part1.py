#student name:
#student number:

import threading

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
    mid = len(testcase) // 2

    if firstHalf == True:
        sortedFirstHalf = sorted(testcase[:mid])
    else:
        sortedSecondHalf = sorted(testcase[mid:])

    

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """

    # indexs for first and second halves of the sorted lists
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

    # Check which index is smaller and append the rest to the SortedFullList.
    # i_firstHalf and i_secondHalf cannot be equal after the while loop above

    if i_firstHalf < i_secondHalf:
        SortedFullList.append(sortedFirstHalf[i_firstHalf:])
    else:
        SortedFullList.append(sortedSecondHalf[i_secondHalf:])
    
    


   

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 


    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)