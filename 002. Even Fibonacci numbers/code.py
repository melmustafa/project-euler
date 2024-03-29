#####################################################################################################################################################
#   Source Name     : code.py                                                                                                #
#   Version         : 1.0                                                                                                                           #
#   Link            : https://projecteuler.net/problem=2                                                                                            #
#   Created date    : 12/02/2023                                                                                                                    #
#   Last updated    : 13/02/2023                                                                                                                    #
#   Author          : Mohammed El-Mustafa Ahmed                                                                                                     #
#   Description     : This code will find the sum of even fibonacci terms less than 4 million.                                                      #
#####################################################################################################################################################

#----------------------- Project Euler Problem -----------------------#

#################################################################################################################################
#   Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first  #
#   10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...                                                                    #
#   By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the             #
#   even-valued terms.                                                                                                          #
#################################################################################################################################

#----------------------- Description of the Solution -----------------------#

#########################################################################################################################################
#   The fact that this is a Fibonacci problem let me think there is a relation between the terms, turns out it is as follows:           #
#   ef(n) = 4 * ef(n - 1) + ef(n - 2)                                                                                                   #
#   using this relation we can directly find the even terms of the Fibonacci sequence.                                                  #
#########################################################################################################################################

#----------------------- Brute force Solution -----------------------#

# This solution just calculate all terms of the Fibonacci

n0, n1 = 0, 1           # The first 2 even Fibonacci

sum = 0

nn = n1 + n0            # The next term

while nn < 4000000:
    if nn % 2 == 0:     # Only add the evens
        sum = sum + nn
    # find the next term
    n0 = n1
    n1 = nn
    nn = n1 + n0

print(sum)

#----------------------- A good solution -----------------------#

n0, n1 = 0, 2           # The first 2 even Fibonacci

sum = n0 + n1

nn = 4 * n1 + n0        # The next term

while nn < 4000000:
    sum = sum + nn
    # find the next term
    n0 = n1
    n1 = nn
    nn = 4 * n1 + n0

print(sum)