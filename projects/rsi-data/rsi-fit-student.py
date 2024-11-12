from lib2to3.fixes.fix_imports import alternates

import pandas as pd
import numpy as np
import scipy
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt


"""
Preamble: Load data from source CSV file
"""
### YOUR CODE HERE
data = np.loadtxt("all_participant_data_rsi.csv", usecols= (1,2,3), skiprows=1, delimiter=  ',')
force_plate = data[:,0]
accelerometer = data[:,1]
percent_error = data[:,2]


"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph two each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE
#Find Mu and Std for both data sets
mean_force = np.mean(force_plate)
mean_accel = np.mean(accelerometer)
std_fp = np.std(force_plate)
std_accel = np.std(accelerometer)

#plot FP
xf = np.linspace(start=-1, stop=3, num=1000)
yf = norm.pdf(xf, loc=mean_force, scale=std_fp)
plt.plot(xf,yf, label='Force Plate Normal', color='#450084')

#Plot Accel.
xa = np.linspace(start=-1, stop=3, num=1000)
ya = norm.pdf(xa, loc=mean_accel, scale=std_accel)
plt.plot(xa,ya, label='Accelerometer Normal', color='#AD9C65')

#Setup for both to be put on the same graph
plt.title('Fitted Normal Distribution for Force Plate and Accelerometer Data')
plt.xlabel('Measured Data')
plt.ylabel('Probability')
plt.legend(loc="upper right")
plt.show()

#Printouts for Q1
print('\n' + "The Mu of the Force Plate Data is " + str(mean_force))
print("The std of the Force Plate Data is " + str(std_fp))
print('\n' + "The Mu of the Accelerometer Data is " + str(mean_accel))
print("The std of the Accelerometer Data is " + str(std_accel))


"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), with the 10th bin encompassing [2,inf). An alpha=0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE
#Establish Alpha. Used later.
alpha=0.05

# Create the Bins
bins = np.linspace(start=0, stop=2, num=9)
bins = np.r_[-np.inf, bins, np.inf]

# Place observations into bins
observed_counts, observed_edges = np.histogram(accelerometer, bins=bins, density=False)

# CDF difference gives probabilities for each bin. Provided probability of
expected_prob = np.diff(norm.cdf(bins, loc=mean_force, scale=std_fp))

# Expected frequency for each bin
expected_counts = expected_prob * len(accelerometer)

# Conduct chi2
(chi_stat, p_value) = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat for Accelerometer: ', chi_stat, ' \n P-value for Accelerometer: ', p_value)
if p_value < alpha:
    print('It is not a fit. \n')
else:
    print('It is a fit. \n')

"""
Force Plate
"""
### YOUR CODE HERE

#Create the Bins
bins = np.linspace(start=0, stop=2, num=9)
bins = np.r_[-np.inf, bins, np.inf]

#Place observations into bins
observed_counts, observed_edges = np.histogram(force_plate, bins=bins, density=False)

#CDF difference gives probabilities for each bin. Provided probability of
expected_prob = np.diff(norm.cdf(bins, loc=mean_force, scale=std_fp))

#Expected frequency for each bin
expected_counts = expected_prob * len(force_plate)

#Conduct chi2
(chi_stat, p_value) = chisquare(f_obs=observed_counts, f_exp=expected_counts, ddof=2)
print('Chi2 stat for Force Plate: ', chi_stat, ' \n P-value for force plate: ', p_value)
if p_value < alpha:
    print('It is not a fit.')
else:
    print('It is a fit.')


"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE
#Proform a two-sided ttest comparing FP and Accel.
(statistic, pvalue) = scipy.stats.ttest_ind(force_plate, accelerometer,  alternative='two-sided')

#Report the pvalue
print("The Pvalue of the Ttest is " + str(pvalue))

#Print out of Fit
if pvalue < alpha:
    print("These two data sets are not equal.")
else:
    print("These two data sets are equal.")


"""
Question 4 (Bonus): Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE
RSIError = force_plate - accelerometer

#Find Mu and Std
mean_error = np.mean(RSIError)
std_error = np.std(RSIError)

#Set up Normal Dist.
xe = np.linspace(start=-1, stop=1, num=1000)
ye = norm.pdf(xe, loc=mean_error, scale=std_error)
plt.plot(xe,ye, label='RSI Error Normal', color='#450084')

# Bin and plot samples
num_bins = 16
count, bins, ignored = plt.hist(RSIError, bins=num_bins, density=True, label='Sampled and Binned Normal Distribution',
                                edgecolor='k', color='#CBB677')


plt.title('Fitted Normal Distribution for RSI Error')
plt.xlabel('Measured Error')
plt.ylabel('Probability')
plt.legend(loc="upper right")

plt.show()