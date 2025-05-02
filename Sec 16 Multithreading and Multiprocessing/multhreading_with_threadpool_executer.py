from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
      time.sleep(1)
      return f"Number : {number}"

numbers = [x for x in range(1, 11)]

with ThreadPoolExecutor(max_workers=3) as executer:
      results=executer.map(print_number, numbers)

for result in results:
      print(result)