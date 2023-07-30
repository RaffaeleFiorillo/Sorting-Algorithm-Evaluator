import matplotlib.pyplot as plt
from settings import ALGORITHMS, a_names


def create_algorithm_plot(x_data, min_times, avg_times, max_times):
	plt.plot(x_data, min_times, label="Minimum time")
	plt.plot(x_data, avg_times, label="Average time")
	plt.plot(x_data, max_times, label="Maximum time")

	plt.xlabel("List Length")
	plt.ylabel("Time taken (seconds)")
	plt.title("Sorting Algorithm Performance")
	plt.legend()
	plt.grid(True)
	plt.show()


def create_algorithms_plot(x_data, algorithms_data, title, x_label, y_label, n):
	plt.figure(n)
	for algorithm_name in a_names:
		plt.plot(x_data, algorithms_data[algorithm_name], label=algorithm_name)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	plt.legend()
	plt.grid(True)
	plt.show()
