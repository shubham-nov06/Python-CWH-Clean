side1 = int(input("Enter first side of triangle = "))
side2 = int(input("Enter 2nd side of triangale = "))
side3 = int(input("Enter 3rd side of triangle = "))

if side1 == side2 and side2 == side3:
    
    print("This is a Eqilateral Triangle ")
    
elif side1 == side2 or side2 == side3 or side1 == side3:
    
    print("This is a Isosceles Traiangle")
    
else: 
    print("This is scalene Triangle ")
