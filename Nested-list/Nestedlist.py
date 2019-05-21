# hackerrank - Used Python 3  Final Code
#!/bin/python3
if __name__ == '__main__':
    StudentDetails= []
    StGrades =[]
    FinalList=[]
    MaxStudents = int(input())
   
    for N in range(0,MaxStudents):
        name = input()
        score = float(input())
        StudentDetails.append([name,score])
        StGrades.append(score)

    LowScoreList= sorted(StGrades, reverse=False)
    Lowestscore=LowScoreList[0]
    
    A=0
    B=1
    while LowScoreList[A] == LowScoreList[B]:  #Make sure there is no dups inlowest score
        A=B
        B=B+1

    SecLowScore=LowScoreList[B]       
    A=0
    FinalList =[]                               #Final Score List - ready to print
    for N in StudentDetails:                    #Loop with originalfile - every record
   
        if N[1]==SecLowScore:             #check if 2 part of rec(score)=lowestscore calc
  
            FinalList.append(StudentDetails[A]) #add onto new list - just what we print
        A=A+1                               #Regardless incr index couter

    FinalList.sort()                        #Sort final list alphabetically
    for i in FinalList:
        print(i[0], sep="\n")               #Just print name part of rec
    
    StudentDetails= []
    StGrades =[]
    FinalList=[]
    MaxStudents = int(input())
   
    for N in range(0,MaxStudents):
        name = input()
        score = float(input())
        StudentDetails.append([name,score])
        StGrades.append(score)

    LowScoreList= sorted(StGrades, reverse=False)
    Lowestscore=LowScoreList[0]
    
    A=0
    B=1
    while LowScoreList[A] == LowScoreList[B]:  #Make sure there is no dups inlowest score
        A=B
        B=B+1

    SecLowScore=LowScoreList[B]       
    A=0
    FinalList =[]                               #Final Score List - ready to print
    for N in StudentDetails:                    #Loop with originalfile - every record
   
        if N[1]==SecLowScore:             #check if 2 part of rec(score)=lowestscore calc
  
            FinalList.append(StudentDetails[A]) #add onto new list - just what we print
        A=A+1                               #Regardless incr index couter

    FinalList.sort()                        #Sort final list alphabetically
    for i in FinalList:
        print(i[0], sep="\n")               #Just print name part of rec
    
