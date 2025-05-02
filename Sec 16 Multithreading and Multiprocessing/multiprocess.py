import time
import multiprocessing


def square_numbers():
    try:
        for i in range(5):
            time.sleep(1)
            print(f"Square : {i*i}")
    except Exception as e:
        print(f"Error in square_numbers: {e}")

def cube_numbers():
    try:
        for i in range(5):
            time.sleep(1.5)
            print(f"Cube : {i*i*i}")
    except Exception as e:
        print(f"Error in cube_numbers: {e}")

if __name__=="__main__":
    try:
        # Creating 2 processes
        p1 = multiprocessing.Process(target=square_numbers)
        p2 = multiprocessing.Process(target=cube_numbers)

        # Start the processes
        p1.start()
        p2.start()

        # Wait for the processes to complete
        p1.join()
        p2.join()
        
    except Exception as e:
        print(f"Error in main process: {e}")