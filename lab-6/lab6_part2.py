#student name: Kyle Groulx
#student number: 95104774

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list): 
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks 
    """
    def eatForAWhile():   #simulates philosopher eating time with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
    
    def thinkForAWhile(): #simulates philosopher thinking time with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

    # Returns True if philisopher successfuly acquires both chopsticks and eats. False otherwise.
    def attemptToPickUpChopsticksAndEat() -> bool:
        leftChopstick = id
        rightChopstick = (id + 1) % 5

        # Pick up the left chopstick first.
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")

        # Only keep the left one if the right one is available immediately.
        if chopstick[rightChopstick].acquire(False):
            print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")
            eatForAWhile()  #use this line as is

            print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
            chopstick[rightChopstick].release()
            print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
            chopstick[leftChopstick].release()
            return True
        else:
            # Could not get both chopsticks, so put the left one back and wait for a small delay
            print(f"DEBUG: philosopher{id} could not get chopstick{rightChopstick}, releasing chopstick{leftChopstick}")
            chopstick[leftChopstick].release()
            time.sleep(round(random.uniform(.01, .02), 3)) # Small delay of 10ms-20ms to avoid trying to acquire again too quickly

    for _ in range(6): #to make testing easier, instead of a forever loop we use a finite loop
        ate = False

        # Continue to loop until the philosopher succefully acquires both chopsticks and eats.
        while not ate:
            ate = attemptToPickUpChopsticksAndEat()

        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5

    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()
