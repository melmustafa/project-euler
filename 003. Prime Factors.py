#####################################################################################################################################################
#   Source Name     : 003. Multiples of 3 or 5.py                                                                                                   #
#   Version         : 1.0                                                                                                                           #
#   Link            : https://projecteuler.net/problem=3                                                                                            #
#   Created date    : 13/02/2023                                                                                                                    #
#   Last updated    : 13/02/2023                                                                                                                    #
#   Auther          : Mohammed El-Mustafa Ahmed                                                                                                     #
#   Description     : This program can find all the prime factors of 600851475143 (generally n) and print the largest factor.                       #
#####################################################################################################################################################

#----------------------- Project Euler Problem -----------------------#

#####################################################################
#   What is the largest prime factor of the number 600851475143 ?   #
#####################################################################

#----------------------- The Solution -----------------------#

# The idea is just to use the divison method to find all factors.
# We start by 2 then add the 2 to the factor list and divide the number by 2 until it can't be divided by it anymore.
# Then we start iterating the odd numbers starting by 3 and whenever a number is a factor we add it to the list and 
# divide n by it until it can't be divided anymore. The resulting list is sure to have only prime numbers since only
# the smallest numbers are divided first then those small numbers are sure to be primes.


def prime_factorization(n):
    factors = []                # empty factor list

    if n % 2 == 0:              # check if the number can be divided by 2
        factors.append(2)       # add 2 to the factor list
        n = n / 2
        while n % 2 == 0:       # divide the number by 2 until it can't be divided anymore.
            n = n / 2
    
    i = 3                       # starting the search in the odd numbers
    while n != 1:
        if n % i == 0:          # check if a number is a factor
            factors.append(i)   # add the number to the factor lists
            n = n / i           
            while n % i == 0:   # divide the number by the factor until it can't be divided anymore.
                n = n / i
        i = i + 2               # the next odd number
    return factors

n = 600851475143
print(max(prime_factorization(n)))