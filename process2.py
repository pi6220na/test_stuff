# https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/
from time import sleep
import time

from multiprocessing import Process, current_process

def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    sleep(2)
    proc_name = current_process().name
    print('{0} doubled to {1} by: {2}'.format(
        number, result, proc_name))


if __name__ == '__main__':
    startTime = time.time()

    numbers = [5, 10, 15, 20, 25]
    procs = []
    proc = Process(target=doubler, args=(5,))

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    proc = Process(target=doubler, name='Test', args=(2,))
    proc.start()
    procs.append(proc)

    for proc in procs:
        proc.join()

    elapsedTime = time.time() - startTime
    print('Elasped time: {} '.format(elapsedTime))
    print()

    startTime = time.time()
    for index, number in enumerate(numbers):
        doubler(number)
    doubler(2)
    elapsedTime = time.time() - startTime
    print('Elasped time: {} '.format(elapsedTime))

