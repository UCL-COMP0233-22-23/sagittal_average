from sagittal_average.sagittal_brain import *
import subprocess
#RUN FROM BASH TERMINAL

import numpy as np


# sample = np.array([[0,0,0], [0,0,0], [1,1,1]])
# np.savetxt('brain_sample.csv', sample, delimiter=',', fmt='%i') #save as csv and integers

# expected = np.asarray([0., 0., 1.])
# np.savetxt('brain_expected.csv',expected, delimiter=',', fmt='%f') #save as csv and integers
# #NB: ik the expected csv looks different format to the output the arrays are the same format which is what matters for testing




# subprocess.run(['python', 'sagittal_brain.py'], shell=True) #run the main py file and create the brain_average result file

# read_output = np.loadtxt('brain_average.csv', delimiter=',') #read the file (ie convert to array)


# #test:
# np.testing.assert_array_equal(read_output, expected)



def test_brain(): #create the above into a function for pytest
    data_input = np.zeros((20, 20)) #20x20 instead of 1x3 like before
    data_input[-1, :] = 1 #make last row = 1

    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')


    # The expeted result is all zeros, except the last one, it should be 1
    expected = np.zeros(20)
    expected[-1] = 1

    run_averages(file_input="brain_sample.csv",
    file_output="brain_average.csv")

    result = np.loadtxt( "brain_average.csv",  delimiter=',')


    return np.testing.assert_array_equal(result, expected)


