# create a random list of deposits
accounts = [1000, 1235, 1982, 29462, 189263, 102372, 27]

# set an interest rate to be applied (as fraction)
rate = 0.05


# iterate through deposits and determine new value
for deposit in accounts:
    balance = deposit * (1 + rate)
    print("Balance was " + str(deposit) + ", now is " + str(balance))

