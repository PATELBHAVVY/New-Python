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