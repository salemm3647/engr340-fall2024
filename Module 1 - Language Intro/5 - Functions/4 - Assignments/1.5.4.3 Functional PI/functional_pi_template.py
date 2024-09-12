import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    #starting pi variables
    a = 1
    b = 1 / (math.sqrt(2))
    t = 1 / 4
    p = 1

    pi_func=0
    #the difference between real value and estimated value needs to fall below the target error
    while (math.pi-pi_func)>target_error:
        A=(a+b)/2
        B=math.sqrt(a*b)
        P=2*p
        T=t-p*(A-a)**2

        a=A
        b=B
        p=P
        t=T

        pi_func=((a+b)**2)/(4*t)


    # change this so an actual value is returned
    return pi_func



desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
