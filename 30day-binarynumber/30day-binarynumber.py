# hackerrank - Used Python 3 
#!/bin/python3

# Input: integer
#Output: total number of consecutive 1's in the binary representation of the number
if __name__ == '__main__':
    #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())        #Enter decimal integer
    IntNum=(bin(n)[2:])     #Convert dec integer into binary [2:] gets rid of b at front
 
    StoreOnes=(IntNum.split("0"))    #Get rid of the zeros and store 1s as lists
   
    GrabOnes=max(StoreOnes) 
    NumOnes=len(GrabOnes)
    print(NumOnes)
