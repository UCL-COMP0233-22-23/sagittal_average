import numpy as np
from sagittal_brain import run_averages

input = np.zeros((20,20))
input[-1] = np.ones(20)

np.savetxt('brain_sample.csv', input,'%d', ',')
run_averages()

output = np.loadtxt('brain_average.csv', dtype=float, delimiter=',')

expected = np.zeros(20)
expected[-1] = 1

print(input)
print(output)
print(expected)

np.testing.assert_array_equal(output, expected)
