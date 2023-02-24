#####################################################################################################################################################
#   Source Name     : 005. Smallest multiple.py                                                                                                     #
#   Version         : 1.0                                                                                                                           #
#   Link            : https://projecteuler.net/problem=5                                                                                            #
#   Created date    : 15/02/2023                                                                                                                    #
#   Last updated    : 15/02/2023                                                                                                                    #
#   Auther          : Mohammed El-Mustafa Ahmed                                                                                                     #
#   Description     : This program can find all the prime factors of 600851475143 (generally n) and print the largest factor.                       #
#####################################################################################################################################################

#----------------------- Project Euler Problem -----------------------#

###############################################################################
#   Find the largest palindrome made from the product of two 3-digit numbers. #
###############################################################################

import math

# def gcd(a, b):
  # while b != 0:
    # a, b = b, a % b
  # return a
# 
# m = 20
# for i in range(1, 20):
  # m = m * i // gcd(i, m)
# print(m)


primes = [2, 3, 5, 7, 11, 13, 17, 19]
m = 1
for i in primes:
    m = m * ( i ** int(math.log(20, i)) )
print(m)


# m = (2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19
# print(m)