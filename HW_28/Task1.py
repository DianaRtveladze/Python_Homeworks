import threading


def find_even():
    even_numbers = [num for num in range(30, 51) if num % 2 == 0]
    print("Even numbers:", even_numbers)


def find_odd():
    odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
    print("Odd numbers:", odd_numbers)


if __name__ == "__main__":
    t1 = threading.Thread(target=find_even)
    t2 = threading.Thread(target=find_odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threads are finished.")
