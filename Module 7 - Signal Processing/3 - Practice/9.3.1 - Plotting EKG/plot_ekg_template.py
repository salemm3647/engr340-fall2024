
import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
load = np.loadtxt(path, skiprows=2, delimiter=  ',')

# save each vector as own variable

### Your code here ###
seconds = load[:,0]
MLII= load[:,1]
V1= load[:,2]

# use matplot lib to generate a single

### Your code here ###
##plt.plot(seconds,MLII)
plt.plot(seconds,V1)
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.show()