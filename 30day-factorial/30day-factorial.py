# hackerrank - Used Python 3 
#!/bin/python3

# Input: integer
# Output:  factorial of that number (if inout =3, output=3x2x1=6)
#!/bin/python3

import math
import os
import random
import re
import sys

# Factorial function
def factorial(n):
    if n==1:                #return 1 if end of factorial and strat unravelling
        return(1)
    else:
        return(n*factorial(n-1))    #multiply number with call factorial fn again


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
