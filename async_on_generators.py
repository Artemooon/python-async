import time
from collections import deque

queue = deque()

def counter():
    counter = 0

    while True:
        print(counter)
        counter += 1
        yield

def printer():
    counter = 0
    while True:
        if counter % 2 == 0:
            print("Printer!")
        counter += 1
        yield

def main():

    while True:
        g = queue.popleft()
        next(g)
        queue.append(g)
        time.sleep(0.5)

if __name__ == '__main__':
    queue.append(counter())
    queue.append(printer())
    main()