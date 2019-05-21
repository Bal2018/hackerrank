# hackerrank - Used Python 3  Final Code
#!/bin/python3
if __name__ == '__main__':
n = int(input())                    #length of string
s = set(map(int, input().split()))  #actual string split by space
NumberActions=int(input())          #number of actions to enter
for _ in range (NumberActions):     #loop until end actions
    ActionRequired=(input().split())    #action with space
    if ActionRequired[0] == 'pop':      #no num required
    #    print ('popping list>>' )
        s.pop()
    elif ActionRequired[0] =='remove':  #first part of string
    #    print('remove stuff<<')
        s.remove(int(ActionRequired[1]))    #convert2nd part 2int
    elif ActionRequired[0] =='discard':
        s.discard(int(ActionRequired[1]))
 
print(sum(s))                               #sum of values left  