# hackerrank - Used Python 3 
#!/bin/python3

# Input: number of countries to enter, list of actual country names (may be duplicate)
#Output: total number of unique countries 
if __name__ == '__main__':
CountrySet = []
MaxCountry = int(input())
 
#enter in list of countries
for Counter in range(0,MaxCountry) :
    CountryName=input()
    CountrySet.append(CountryName)
#    print ('Name = ',CountrySet[Counter])
    
UniqueList =[]
for OriginalCountry in CountrySet:
    if OriginalCountry not in UniqueList:
        UniqueList.append(OriginalCountry)

print(len(UniqueList))
#for Counter in range(0, len(UniqueList)):
#    print ('Name = ',UniqueList[Counter])
    

