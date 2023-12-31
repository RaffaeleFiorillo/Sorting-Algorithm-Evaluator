# Sorting-Algorithm-Evaluator
This project lets you run tests with both known sorting algorithm and custom. It then shows their speed performance based on the sorted list length

# Evaluation Modalities
The project currently allows two types of evaluation based on the same principle: Obtain the minimun, maximum and average times of execution of a certain algorithm for various arrays length.
  - The First Evaluation Modality test a specific algorithm and then shows a graph where the y axis represents the time it took to sort the array, and the x axis shows the array length. In this one graph min, max and avg are displayed together to get a sense of how the algorithm performs.
  - The Second Evaluation Modality tests a group of algorithms and displays their performance in 3 graphs (fone for each min, max and avg) similar to the one of the first modalitys.
  - The Third Evaluatin Modality tests if an algorithm works properly. If an array is completely sorted after applying this specific algorithm, then it works.

# How to Setup and Run:
1. install this libraries:
   - matplotlib;
2. Go to the settings.py file and change this variables according to your needs:
   - a_names: The names of the algorithms you want to test. For the names to be valid they must be keys inside the ALL_ALGORITHMS dicitonary.
   - testing_algorithm_name: Name of the algorithm you want to test (for single-* modalities)
   - max_list_length: The test will be performed with list of size 1 up to the value of this variable;
   - num_tests: Number of times each list length will be tested;
   - modality_type: The name of the Evaluation Modality you want to perform. There are three options, one for each modality (respectively):
       - single-speed,
       - multi-speed,
       - single-functioning
4. run the main.py file.

# Possible Future Updates
1. Create a Graphic interface for the project.
2. Create a coding invironment to create, test and save custom sorting algorithms;
3. Have a kind of "AlgoPedia" (Enciclopedia for Sorting Algorithms) with lots of insights about every algorithm.

# Possible future of this Project
This project emerged as an idea to have a simple and fast place to run basic tests on algorithms. In the future this repository may be Merged with an existing Repository called "AlgoData", which you can find [here](https://github.com/robertocarlosmedina/AlgoData). That repository is a graphic tool (created By Roberto Medina awith some contribution of mine) that allows you to visually see how sorting algorithms work. Mergin it with this repository could give birth to an all new project or just a more complete version of either one of the existing repositories.
