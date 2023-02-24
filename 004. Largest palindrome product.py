#####################################################################################################################################################
#   Source Name     : 004. Largest palindrome product.py                                                                                            #
#   Version         : 1.0                                                                                                                           #
#   Link            : https://projecteuler.net/problem=4                                                                                            #
#   Created date    : 15/02/2023                                                                                                                    #
#   Last updated    : 15/02/2023                                                                                                                    #
#   Auther          : Mohammed El-Mustafa Ahmed                                                                                                     #
#   Description     : This program can find all the prime factors of 600851475143 (generally n) and print the largest factor.                       #
#####################################################################################################################################################

#----------------------- Project Euler Problem -----------------------#

###############################################################################
#   Find the largest palindrome made from the product of two 3-digit numbers. #
###############################################################################

def is_palindrome(n):
    return n == int(str(n)[::-1])

palin = 0
for i in range(999, 99, -1):
    if i * 999 < palin:
        break
    for j in range(999, i - 1, -1):
        n = i * j
        if n > palin and is_palindrome(n):
            palin = n
            break
        elif n < palin:
            break

print(palin)