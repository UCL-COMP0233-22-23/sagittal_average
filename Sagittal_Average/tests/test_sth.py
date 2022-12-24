import numpy as np
from Sagittal_Average.sagittal_brain import *
def test_sth():
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

    # The expected result is all zeros, except the last one, it should be 1
    expected = np.zeros(20)
    expected[-1] = 1

    run_averages(file_input="brain_sample.csv",
             file_output="brain_average.csv")

    result = np.loadtxt("brain_average.csv",  delimiter=',')

    np.testing.assert_array_equal(result, expected)