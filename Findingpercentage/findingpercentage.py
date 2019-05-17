# hackerrank - Used Python 3  Final Code
#!/bin/python3
if __name__ == '__main__':
    n = int(input())                                #Input number of students to enter
    student_marks = {}          
    for _ in range(n):                     #For each student record
        name, *line = input().split()      #Input student details with spaces (name followed by scores)
        scores = list(map(float, line))     
        student_marks[name] = scores                #Store student scores
    NameStored =False

    while not NameStored :                  #Loop records stored until you get one wanted
        query_name = input()
        if query_name in student_marks: 
            NameStored =True
        else:
            print('Ooops - try again')              #Display error message

    for RecIndex in student_marks:         
        if query_name==   RecIndex:                 #If found student
            AverageMark=student_marks[RecIndex]     #Calculate average scores stored
            Numsubjectmarks=len(student_marks[RecIndex])
            print("%.2f"%(sum(AverageMark)/Numsubjectmarks))
    