#####################################################################################################################################################
#   Source Name     : code.py                                                                                                   #
#   Version         : 1.0                                                                                                                           #
#   Link            : https://projecteuler.net/problem=1                                                                                            #
#   Created date    : 12/02/2023                                                                                                                    #
#   Last updated    : 13/02/2023                                                                                                                    #
#   Auther          : Mohammed El-Mustafa Ahmed                                                                                                     #
#   Description     : This code will calculate the sum of all multiplies of 3 or 5 (generally x or y) below 1000 (generally n).                     #
#####################################################################################################################################################

#----------------------- Project Euler Problem -----------------------#

#########################################################################
#   Find the sum of all the multiples of 3 or 5 below 1000.             #
#########################################################################

#----------------------- Description of the Solution -----------------------#


# The fact that we want all multiplies of x or y can give us the idea of just summing over all the multiplies of each,
# but some multiplies are common between x and y like x * y so we use the inclusion-exclusion principle, and we sum
# over them and then take out all the common multiplies since they will be counted twice otherwise.

#----------------------- The easy solution -----------------------#

x = []
y = []
l = []
i = 1
while(i * 3 < 1000):
    x.append(i*3)
    i = i + 1
i = 1
while(i * 5 < 1000):
    y.append(i*5)
    i = i + 1
i = 1
while(i * 15 < 1000):
    l.append(i * 15)
    i = i + 1
sum = sum(x) + sum(y) - sum(l)

print(sum)

#----------------------- The Normal Solution -----------------------#

x = 3
y = 5
l = 15
sum = 0
i = 1
while(i * x < 1000):
    sum = sum + x * i
    i = i + 1
i = 1
while(i * y < 1000):
    sum = sum + y * i
    i = i + 1
i = 1
while(i * l < 1000):
    sum = sum - l * i
    i = i + 1

print(sum)

#----------------------- Constant time solution -----------------------#

x = 3
y = 5
l = 15          # The least common multiply of 3 and 5
n = 1000
nx = (n-1) // x  # Number of multiplies of 3 less than 1000
ny = (n-1) // y  # Number of multiplies of 5 less than 1000
nl = (n-1) // l  # Number of multiplies of 15 less than 1000

# Now we calculate the sum based on the fact that those series are arithmetic series.
# The rule is n * (f + l) / 2 where n is the number of terms, f is the first term, and l is the last term.
# In our case since we always wants multiplies of a certain number then always the first term is x and the last term is n*x
# then the new rule becomes n * (x + n * x) / 2 -> n * (n + 1) * x / 2
sumx = nx * (nx + 1) * x / 2
sumy = ny * (ny + 1) * y / 2
suml = nl * (nl + 1) * l / 2
# The Inclusion-Exclusion Principle.
sum = sumx + sumy - suml

print(sum)



#----------------------- The General Solution -----------------------#

def gcd(a, b):
    r = a % b
    while (r != 0):
        a = b
        b = r
        r = a % b
    return b

print("This program finds the sum of all multiplies of x or y below n.")
x = int(input("Please input x: "))
y = int(input("Please input y: "))
n = int(input("Please input n: "))
l = x * y // gcd(x, y)

nx = (n-1) // x
ny = (n-1) // y
nl = (n-1) // l

sumx = nx * (nx + 1) * x // 2
sumy = ny * (ny + 1) * y // 2
suml = nl * (nl + 1) * l // 2

sum = sumx + sumy - suml

print(sum)