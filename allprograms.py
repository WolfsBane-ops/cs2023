######################### PROGRAM 1 ####################################
def replace(s):
    strn=s.replace("a","*")
    strn=strn.replace("A","*")
    print(strn)
def reverse(s):
    lst=[]
    newstr=' '
    words=s.split(' ')
    for i in words:
        revword=i[::-1]
        lst.append(revword)
    newstr=' '.join(lst)
    print("original string is",s)
    print("reversed string is",newstr)

while(1):
    print("1.Replace 'a' and 'A' by '*' ")
    print("2.Reverse every word in a string")
    print("3.Quit")
    print()
    choice=int(input("enter your choice"))
    if (choice==1):
        s=input("enter the string")
        replace(s)
        print()
    elif(choice==2):
        s=input("enter the string")
        reverse(s)
        print()
    elif(choice==3):
        break
    else:
        print("wrong choice")



######################### PROGRAM 2 ####################################

print("CLINT MANAGEMENT USING STACK")
top=None
clint_file=[]

def isempty(clint_file):
    if(clint_file==[]):
        return True
    else:
        return False

def push(clint_file):
    global top
    while(True):
        clint_id=input("enter the clint ID:")
        clint_name=input("enter the clint name:")
        con_num=int(input("enter the contact number:"))
        record=[clint_id,clint_name,con_num]
        clint_file.append(record)
        op=int(input("press 1 to add another record to stack 0 to quit"))
        top=len(clint_file)-1
        if(op!=1):
            break
def peek(clint_file):
    global top
    if isempty(clint_file):
        print("Stack UNDERFLOWS!")
    else:
        top = len(clint_file)-1
        return top
def pop(clint_file):
    global top
    if isempty(clint_file):
        print("stack UNDERFLOWS")
    else:
        item=clint_file.pop()
        if(len(clint_file)==0):
            top=None
        top=len(clint_file)-1
        return item

def display(clint_file):
    global top
    if isempty(clint_file):
            print("stack UNDERFLOWS")
    else:
        return clint_file[top]

while(1):
    print("1.push 2.pop 3.display 4.peek 5.exit")
    ch=int(input("enter your choice:"))
    if(ch==1):
        push(clint_file)
    elif(ch==2):
        item=pop(clint_file)
        if(item!=None):
            print("top most element deleted is",item)
    elif(ch==3):
        display(clint_file)
    elif(ch==4):
        val=peek(clint_file)
        print("top most element in the stack is..",val)
    elif(ch==5):
        break
    else:
        print("invalid choice...try it again")


######################### PROGRAM 3 ####################################

def count_word():
    fin = open("file1.txt","r")
    str = fin.read()
    I = str.split()
    count_words = 0
    for i in I:
        count_words = count_words + 1
    print(count_words)
    fin.close()
def longest_word():
    fin = open("file1.txt","r")
    str = fin.read()
    words = str.split()
    max_len = len(max(words,key=len))
    for word in words:
        if len(word)==max_len:
            longest_word = word
            print(longest_word)
while True:
    print('''1.python program to count the number of words in a text file
1.python program to find longest word from text file
3.exit''')
    x=int(input("enter your choice:"))
    if x==1:
        count_word()
    elif x==2:
        longest_word()
    else:
        break
    

######################### PROGRAM 4 ####################################

import csv
def create():
    f1=open("file.csv","w+",newline='')
    wob=csv.writer(f1)
    n=int(input("enter the number of records:"))
    for i in range(n):
        user_id=input("enter the user id:")
        password=input("enter the password:")
        a=[user_id,password]
        wob.writerow(a)
    f1.close()
def search(y):
    f1=open("file.csv","r")
    rob=csv.reader(f1)
    for i in rob:
        if i[0]==y:
            print("password is:",i[1])
            break
        else:
            print("record not present")
while True:
    print('''1.create csv file with userid and password
2.search for password
3.exit''')
    x=int(input("enter your choice"))
    if x==1:
        create()
    elif x==2:
        x=input("enter the user id to search:")
        search(x)
    elif x==3:
        break
    else:
        print("entered a wrong choice")


######################### PROGRAM 5 ####################################

import csv
def createfile():
    csvfile=open("student.csv","w")
    csvobj=csv.writer(csvfile)
    while(True):
        rollno=int(input("enter the roll number of the student"))
        name=input("enter the name of the student")
        m1=float(input("enter the mark1"))
        m2=float(input("enter the mark2"))
        m3=float(input("enter the mark3"))
        m4=float(input("enter the mark4"))
        m5=float(input("enter the mark5"))
        total=m1+m1+m3+m4+m5
        avg=total/5
        rec=[rollno,name,m1,m2,m3,m4,m5,total,avg]
        csvobj.writerow(rec)
        print("record added successfully")
        ch=input("do you want to continue...Y/N")
        if(ch.lower()=='n'):
            break
        csvfile.close()
def updategrade():
    csvfile=open('student.csv','r')
    csvobj=csv.reader(csvfile)
    newlist=[]
    for row in csvobj:
        try:
            if(float(row[8]>=90)):
               row.append('A')
            elif(float(row[8])<90 and float(row[8])>=80):
                row.append('B')
            elif(float(row[8])<80 and float(row[8])>=60):
                row.append('C')
            elif(float(row[8])<60 and float(row[8])>=40):
                row.append('D')
            else:
                row.append('FAIL')
            newlist=newlist+[row,]
        except IndexError:
            pass
    csvfile.close()
    csvfile=open('student.csv','w')
    csvobj=csv.writer(csvfile)
    csvobj.writerows(newlist)
    print("Grade updated successfully")
    csvfile.close()

def display():
    csvfile=open('student.csv','r')
    csvobj=csv.reader(csvfile)
    print("STUDENT ACADEMIC DETAILS")
    print("********************************")
    print("Rollno\tName\tMark1\tMark2\tMark3\tMark4\tMark5\tTotal\tAverage\tGrade")
    print("*********************************************************************************")
    for row in csvobj:
        try:
            for x in range(10):
                print(row[x],end='\t')
            print()
        except IndexError:
            pass
    csvfile.close()
    print("*********************************************************************************")

while True:
    print("1.To create student file using csv, 2.Update grade, 3.Display all the records, 4.Exist")
    x=int(input("Enter your choice:"))
    if x==1:
        createfile()
    elif x==2:
        updategrade()
    elif x==3:
        display()
    else:
        break



######################### PROGRAM 6 ####################################

import pickle
def createfile():
    file=open('employee.dat','wb')
    while(True):
        empno=int(input("Enter the employee number"))
        empname=input("Enter the employee number")
        salary=float(input("Enter the salary"))
        rec={'EmpNo:':empno,'EmpName:':empname,'Salary:':salary}
        pickle.dump(rec,file)
        ch=input("Do you want to continue....Y/N")
        if(ch.lower()=='n'):
            break
    file.close()
def updatesalary(empno,sal):
    file=open('employee.dat','rb')
    v=0
    re=[]
    while(True):
        try:
            data=pickle.load(file)
            re.append(data)
        except EOFError:
            break
    file.close()
    file=open('employee.dat','wb')
    for i in range(len(re)):
        if(re[i]['EmpNo:']==empno):
            re[i]['Salary:']=sal
            v=1
    for x in re:
        pickle.dump(x,file)
    if(v==0):
        print("Entered employee number is not found in the file")
    else:
        print("Employee record updated successfully")
    file.close()
def display():
    file=open('employee.dat','rb')
    print("******Employee Details******")
    print("______________________________________________________")
    print("Employee Number\t\tEmployee Name\t\tSalary")
    print("*************************************************************")
    try:
        while(True):
            rec=pickle.load(file)
            print(' ',rec['EmpNo:'],"\t\t",rec['EmpName:'],"\t\t",rec['Salary:'])
            print()
    except EOFError:
        pass
    print("**************************************************************")
    file.close()
print("Binary File Handling = Employees")
while(True):
    print("1.Create File and Append data 2.Update record 3.Display the file content 4.Quit")
    ch=int(input("Enter your choice"))
    if(ch==1):
        createfile()
    elif(ch==2):
        empno=int(input("Enter the employee number to be searched"))
        sal=float(input("Enter the new salary"))
        updatesalary(empno,sal)
    elif(ch==3):
        display()
    elif(ch==4):
        break
    else:
        print("Invalid input")
        


######################### PROGRAM 7 ####################################

def startthegame(mylist):
    count=1
    while(count<=6):
        randnum=random.randint(1,6)
        mylist.append(randnum)
        count+=1
    return mylist
import random
mylist=[]
newlist=[]
numlist=startthegame(mylist)
print("*******Simulating Dice-Random Number Generation*******")
for x in range(1,7):
    print("Number generated at the",x,"time of dice thrown..",numlist[x-1])
print("***************************************************")
if(len(numlist)==len(set(numlist))):
    print("All the numbers in the range 1 to 6 have been generated successfully")
else:
    print("Some number has been generated for multiple times")
    for x in numlist:
        if(x not in newlist):
            newlist.append(x)
            if(numlist.count(x)>1):
                print(x,"has been generated for",numlist.count(x),"times")
        else:
            continue


######################### PROGRAM 8 ####################################

'''create a student dictionary containing names and marks as key:value pairs for 5 students.
write a stack inplementation program with seperate user defined functions for the following
1. to push the names of the students from dictionary into the stack whose marks>=75.
2. to remove the student details from the stack
3. to display the client details stored in the stack
4. to search for the existence of the given student name in the stack'''
top=None
student=[]
print("STUDENT MANAGEMENT USING STACK")
def push(stud):
    global top
    c=0
    for x in stud:
        if (stud[x]>=75):
            student.append(x)
            c+=1
    print(c,"number of records with marks >=75 pushed into the stack")
    top=len(student)-1
def pop(student):
    global top
    if(student==[]):
        print("stack UNDERFLOWS")
    item=student.pop()
    if(len(student)==0):
        top=None
    top=len(student)-1
    return item
def display(student):
    global top
    top=len(student)-1
    if(student==[]):
        print("stack UNDERFLOWS")
    else:
        print(student[top],"<--top")
        for i in range(top-1,-1,-1):
            print(student[i])
def search(student):
    global top
    if(student==[]):
        print("stack UNDERFLOWS")
    else:
        c=0
        data=input("enter the name to be searched :")
        for x in student:
            if(x==data):
                print("reccord found successfully")
                break
        else:
            print("record not found")
while(True):
    print('''1.add student records
2.delete record from 'student' stack
3.display all records from 'student' stack
4.search and display records from 'student' stack
5.exit''')
    ch=int(input("enter your choice"))
    if(ch==1):
        stud={}
        for x in range(5):
            name=input("enter the student name :")
            marks=float(input("enter the marks (out of 100) :"))
            stud[name]=marks
        print("student dictionary here.........",stud)
        push(stud)
    elif(ch==2):
        item=pop(student)
        if(item!=None):
            print("top most element deleted is...",item)
    elif(ch==3):
        display(student)
    elif(ch==4):
        search(student)
    elif(ch==5):
        break
    else:
        print("invalid choice...try it again")

