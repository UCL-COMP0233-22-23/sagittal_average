from sagittal_brain import *
import subprocess
#RUN FROM BASH TERMINAL

import numpy as np


sample = np.array([[0,0,0], [0,0,0], [1,1,1]])
np.savetxt('test_brain_sample.csv', sample, delimiter=',', fmt='%i') #save as csv and integers

expected = np.asarray([[0, 0, 1]])
np.savetxt('test_brain_expected.csv',expected, delimiter=',', fmt='%i') #save as csv and integers




subprocess.run(['python', 'sagittal_brain.py'], shell=True) #run the main py file and create the test_brain_average result file

read_output = np.loadtxt('brain_average.csv', delimiter=',') #read the file (ie convert to array)


#test:
np.testing.assert_array_equal(read_output, expected)