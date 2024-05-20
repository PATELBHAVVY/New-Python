'''
marks = input("marks :")
if(marks > 90):
    print("A")

elif(marks > 80 and marks < 90):
    print("B")

elif(marks > 70 and marks < 60):    
    print("C")
    
elif(marks <= 50 and marks < 35):    
    print("D")

else:
    print("E")
    '''

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
    


if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F") 
