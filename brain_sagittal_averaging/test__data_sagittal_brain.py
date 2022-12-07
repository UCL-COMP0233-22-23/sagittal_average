import numpy as np
from sagittal_brain import run_averages

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

expected  = np.zeros(20)
expected[-1] = 1
result = run_averages()
assert np.array_equal(result,expected)

