from sagittal_brain import *



sample = np.array([[0,0,0], [0,0,0], [1,1,1]])
np.savetxt('brain_sample.csv', sample, delimiter=',', fmt='%i') #save as csv and integers

expected = np.asarray([[0, 0, 1]])
np.savetxt('brain_expected.csv',expected, delimiter=',', fmt='%i') #save as csv and integers