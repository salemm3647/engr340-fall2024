"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
#variables
Ain=30792 #In state total
Aout=47882 #Out state total
#calculations
#In order to donate 1 year of tuition every year,
# the interest (5% must be equal to cost of tuition
in_state_gift=Ain/.05
out_state_gift=Aout/.05

print("In-state tuition is "+str(Ain))
print("Out-of-state tuition is "+str(Aout))
print("Principle for In-state-gift is "+str(in_state_gift))
print("Principle for Out-of-state-gift is "+str(out_state_gift))
