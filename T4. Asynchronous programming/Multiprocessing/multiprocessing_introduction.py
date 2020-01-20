import time
import os, signal
import multiprocessing

count = 10
def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))

def calc_cube(numbers, count):
    time.sleep(1)
    while count:
        for n in numbers:
            print('cube ' + str(n*n*n))
        count -=1

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr, count))
    #p2.daemon = True

    time.perf_counter()
    p1.start()
    p2.start()

    # p1.join()
    #p2.join()
    print(p1.pid)
    p1.terminate()
    os.kill(p2.pid, signal.SIGTERM)
    print(p2.exitcode)

    print(p1.pid)
    print(p2.pid)
    time.sleep(5)
    print(p1.pid)
    print(p2.pid)

    print(p2.exitcode)
    print(f"Done in {time.perf_counter()}!")