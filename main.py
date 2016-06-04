import multiprocessing
import psutil
import time
import sys


def process_dummy_example(f):
	i = 0

	while i < 10000000:
		f.write('{}\n'.format(i))
		i = i + 1

	return True

if __name__ == '__main__':
	f = open("output.txt", "w")

	process_m = multiprocessing.Process(target=process_dummy_example, args=(f,))
	process_m.start()

	pid = process_m.pid

	print('Process - pid {}, Run for 5s'.format(pid))

	# using http://pythonhosted.org/psutil/#processes
	try:
		process_p = psutil.Process(pid=pid)

	except psutil.NoSuchProcess:
		#no process with this pid
		print("Error: No such process with {}".format(pid))
		
		process_m.terminate()
		process_m.join()

		sys.exit()

	except psutil.ZombieProcess:
		print("Error: Zombie process")

		process_m.terminate()
		process_m.join()

		sys.exit()

	except psutil.AccessDenied:
		print("Error: Access denied")

		process_m.terminate()
		process_m.join()

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

	f.close()