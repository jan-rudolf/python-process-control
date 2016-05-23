import multiprocessing
import psutil
import time


def process_dummy_example():
    f = open("output.txt", "w")

    i = 0

    while i < 10000000:
        f.write('{}\n'.format(i))
        i = i + 1

    f.close()


process_m = multiprocessing.Process(target=process_dummy_example)
process_m.start()

pid = process_m.pid

print('Process - pid {}, Run 5s'.format(pid))

# using http://pythonhosted.org/psutil/#processes
process_p = psutil.Process(pid=pid)

time.sleep(5)

print(' Suspend/Pause - {}, Wait for 20s'.format(time.strftime("%X")))
process_p.suspend()

time.sleep(20)

print(' Resume - {}, Run for 20s'.format(time.strftime("%X")))
process_p.resume()

time.sleep(20)

print(' Terminate - {}'.format(time.strftime("%X")))
process_m.terminate()
process_m.join()