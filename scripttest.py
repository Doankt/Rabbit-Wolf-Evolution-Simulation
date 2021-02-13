import matplotlib.pyplot as plt
from time import sleep

if __name__ == '__main__':
	fig, ax1 = plt.subplots()
	x = [1, 2, 3]
	y1 = [2, 4, 6]
	ax1.plot(x, y1)
	ax1.plot(5, 8)

	# plt.show(block=False)
	# for n in range(10):
	# 	x.append(n)
	# 	y1.append(n*5)
	# ax1.plot(x, y1)
	plt.show()
	print(plt)