import time
import threading

def printNumbers():
      for i in range(5):
           time.sleep(2)
           print(i)

def printLetters():
      for let in "Keshav":
            time.sleep(1)
            print(let)

## Creating 2 threads.
t1 = threading.Thread(target=printNumbers)
t2 = threading.Thread(target=printLetters)

t1.start()
t2.start()

## Wait for the threads to complete.
t1.join()
t2.join()

