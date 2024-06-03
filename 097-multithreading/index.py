import threading
import time
from concurrent.futures import ThreadPoolExecutor


def sleep_function(seconds):
    time.sleep(seconds)
    print(f"Slept for {seconds} seconds.")
    return seconds


def main():
    # Run normally
    time_one = time.perf_counter()
    # Threads
    sleep_function(2)
    sleep_function(3)
    sleep_function(4)
    time_two = time.perf_counter()
    print(time_two - time_one)

    # Run the program concurrently (Threading)
    time_three = time.perf_counter()
    thread_one = threading.Thread(target=sleep_function, args=[4])
    thread_two = threading.Thread(target=sleep_function, args=[3])
    thread_three = threading.Thread(target=sleep_function, args=[2])
    thread_one.start()
    thread_two.start()
    thread_three.start()
    thread_one.join()
    thread_two.join()
    thread_three.join()
    time_four = time.perf_counter()
    print(time_four - time_three)


# main() # Call function to run


def pooling_demo():
    with ThreadPoolExecutor() as executor:
        future_one = executor.submit(sleep_function, 2)
        future_two = executor.submit(sleep_function, 3)
        future_three = executor.submit(sleep_function, 4)
        print(future_one.result())
        print(future_two.result())
        print(future_three.result())
        # Iterating seconds from a list
        # number_list = [1, 2, 3]
        # results = executor.map(sleep_function, number_list)
        # for result in results:
        #     print(result)


pooling_demo()
