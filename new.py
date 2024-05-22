
A , B = 2, 3
Txt = "@"
print(2*Txt*3)


A, B = '2', 3
Txt = "@"
print((A+Txt)*B)

A ,B = 2, 3
Txt = "Bhavy"
print(2*Txt*3)


A,B = 2,3
C=5
print(A+B*C)


A,B=13,25.0
C=(A//B)
print(C, A/B)


A,B= -12,5
C=A//B
print(C)


A,B=25,45
C=A%B
print(C)



#input in python

name = str(input ("name :"))
print(name)

age = int(input("age:"))
print(age)

work = str(input("work:"))
print(work)

time = float(input("time:"))
print(time)



# Conditional Statement: Lights

light = input("light:")
if(light== "Red"):
    print("Stop")

elif(light == "Green"):
    print("Go")

if(light== "Yellow"):
    print("Look ")

else:
    print("Light is Brocken")



# Conditional Statement: Marks

marks = int(input("marks :"))
if(marks >= 90):
    print("A")

elif(marks >= 80 and marks < 90):
    print("B")

elif(marks >= 70 and marks < 60):    
    print("C")
    
else:
    print("E")


# Conditional Statements: Singals Line If\ Ternary Operator

food = input("food: ")
eat = "Sweet" if food == "cake" or food == "Jalebi" else "Not Sweet"
print(eat)


age = int(input("age :"))
vote = ("Yes", "No") [age >18]

age = int(input("age :"))
vote = ("No", "Yes")[age > 18]


#relational oprator

a = 50
b = 20

print(a == b) #false
print(a <= b)
print(a < b)
print(a != b) #true
print(a >= b)
print(a > b)


#assignmental

num = 20
#num = num + 20
num **= 10
print("num:", num)


#logical operator
a = 50
b = 20
print(not (a<b))
print(not True)


val1 = True
val2 = False

#print("And Opration:", val1, val2)

print("Or Opration:", (a==b) or(a>b))
 

