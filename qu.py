n = int(input("enter the size of queue: "))
queue = [0]*n


def enqueue():
    if queue.count(0) == 0:
        print("queue is overflow")
    else:
        top = int(input("enter the number for push: "))
        for i in range(0, n):
            if queue[i] == 0:
                queue[i] = top
                break


def dequeue():
    if queue.count(0) == len(queue):
        print("queue underflow")
    else:
        for i in range(0, n):
            if queue[i] != 0:
                queue[i] = 0
                break


def display():
    for i in queue:
        if i != 0:
            (n[i])


while (1):
    c = int(input("enter the choice: "))
    if c == 1:
        enqueue()
    elif c == 2:
        dequeue()
    elif c == 3:
        display()
    elif c == 4:
        print("exit")
        break
    else:
        print("invalid number")
 