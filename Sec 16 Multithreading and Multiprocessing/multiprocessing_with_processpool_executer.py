from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
      time.sleep(1)
      return f"Square : {number * number}"

numbers = [x for x in range(1,11)]

if __name__ == "__main__":
      with ProcessPoolExecutor(max_workers=3) as executer:
            results=executer.map(square_number, numbers)

      for result in results:
            print(result)