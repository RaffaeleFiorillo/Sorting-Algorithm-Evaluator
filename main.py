import Testing as Tst
import settings as s


if __name__ == "__main__":
	if s.modality_type == "single-speed":
		Tst.test_and_plot(s.ALL_ALGORITHMS[s.testing_algorithm_name])
	elif s.modality_type == "multi-speed":
		Tst.test_various_and_plot()
	elif s.modality_type == "single-functioning":
		Tst.test_if_works(s.ALL_ALGORITHMS[s.testing_algorithm_name])
