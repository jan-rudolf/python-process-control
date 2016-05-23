import multiprocessing
import psutil
import time


def process_dummy_example():
	f = open("output.txt", "w")

	i = 0

	while i < 100000000:
		f.write('{}\n'.format(i))
		i = i + 1

	f.close()


m_process = multiprocessing.Process(target=process_dummy_example)
m_process.start()

print('pid {}'.format(m_process.pid))

m_process.join()
