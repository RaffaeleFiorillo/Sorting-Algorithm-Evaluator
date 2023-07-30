import SortingAlgorithms as Sa

ALL_ALGORITHMS = {
	"quick_sort": Sa.quick_sort,
	"merge_sort": Sa.merge_sort,
	"insertion_sort": Sa.insertion_sort,
	"selection_sort": Sa.selection_sort,
	"bubble_sort": Sa.bubble_sort,
	"python_sort": Sa.python_sort,
	"tim_sort": Sa.tim_sort,
	"og_sort": Sa.og_sort
}

# algorithms to be tested (in case you only want to test some instead of all)
a_names = ["quick_sort", "merge_sort", "python_sort", "tim_sort"]
ALGORITHMS = {name: algorithm for name, algorithm in ALL_ALGORITHMS.items() if name in a_names}

max_list_length = 4000  # Change this to the maximum list length you want to test
num_tests = 4  # Number of times to test each list length
