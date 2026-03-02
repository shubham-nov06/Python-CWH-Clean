time = float(input("Enter time in hours "))
if time > 0 and time < 5:
    print("Also Night")

elif time >= 5 and time <= 11:
    print("Morning")
elif time > 12 and time <= 16:
    print("Good afternoon ")
    
elif time > 17 and time <= 20:
    print("Good evening ")
    
elif time > 21 and time < 24:
    print("Night ")      
else: 
    print("Invalid input")
    
