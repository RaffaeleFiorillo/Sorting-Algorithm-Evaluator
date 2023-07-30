import random
import timeit
import Plotting as Plt
from settings import *


# creates a random list of a certain length
def generate_random_list(length):
	return [random.randint(1, 1000) for _ in range(length)]


def test_sorting_algorithm(sorting_algorithm, list_length):
	# print(list_length)
	times = []
	for _ in range(num_tests):
		test_list = generate_random_list(list_length)
		start_time = timeit.default_timer()
		_ = sorting_algorithm(test_list)
		end_time = timeit.default_timer()
		execution_time = end_time - start_time
		times.append(execution_time)
	return times


def test_algorithm(sorting_algorithm, x_data):
	min_times, avg_times, max_times = [], [], []

	for list_length in x_data:
		times = test_sorting_algorithm(sorting_algorithm, list_length)
		min_times.append(min(times))
		max_times.append(max(times))
		avg_times.append(sum(times) / num_tests)

	return min_times, avg_times, max_times


def test_and_plot(sorting_algorithm):
	x_data = list(range(1, max_list_length + 1))
	print(f"Iterations (nº tests * max array length): {max_list_length * num_tests}")
	start_time = timeit.default_timer()
	min_times, avg_times, max_times = test_algorithm(sorting_algorithm, x_data)
	end_time = timeit.default_timer()
	print(f"\tTotal Execution Time: {end_time - start_time}")
	Plt.create_algorithm_plot(x_data, min_times, avg_times, max_times)


def test_various_and_plot():
	x_data = list(range(1, max_list_length + 1))

	min_times = {algorithm_name: [] for algorithm_name in ALGORITHMS.keys()}
	max_times = {algorithm_name: [] for algorithm_name in ALGORITHMS.keys()}
	avg_times = {algorithm_name: [] for algorithm_name in ALGORITHMS.keys()}

	for algorithm_name, algorithm in ALGORITHMS.items():
		n_items = max_list_length * (max_list_length + 1) * 2  # 4*n(n+1)/2 = 1 + 2 + 3 + ... + n
		print(f"Algorithm: {algorithm_name} | Elements to order: {n_items} | Iterations: {max_list_length * num_tests}")
		start_time = timeit.default_timer()
		mn_times, a_times, mx_times = test_algorithm(algorithm, x_data)
		end_time = timeit.default_timer()
		min_times[algorithm_name] = mn_times
		max_times[algorithm_name] = mx_times
		avg_times[algorithm_name] = a_times
		print(f"\tTotal Execution Time: {end_time - start_time}")

	Plt.create_algorithms_plot(
		x_data,
		min_times,
		"Sorting Algorithm Performance (Minimum Time)",
		"List Length",
		"Minimum Time (seconds)",
		1)

	Plt.create_algorithms_plot(
		x_data,
		max_times,
		"Sorting Algorithm Performance (Maximum Time)",
		"List Length",
		"Maximum Time (seconds)",
		2)

	Plt.create_algorithms_plot(
		x_data,
		avg_times,
		"Sorting Algorithm Performance (Average Time)",
		"List Length",
		"Average Time (seconds)",
		3)
