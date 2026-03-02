# Create an empty set to store unique numbers
s = set()

# Take input from the user 7 times and add each number to the set
num = int(input("Enter your number = "))  # Take first number input
s.add(int(num))  # Add the number to the set

num = int(input("Enter your number = "))  # Take second number input
s.add(int(num))  # Add the number to the set

num = int(input("Enter your number = "))  # Take third number input
s.add(int(num))  # Add the number to the set

num = int(input("Enter your number = "))  # Take fourth number input
s.add(int(num))  # Add the number to the set

num = int(input("Enter your number = "))  # Take fifth number input
s.add(int(num))  # Add the number to the set

num = int(input("Enter your number = "))  # Take sixth number input
s.add(int(num))  # Add the number to the set

num = int(input("Enter your number = "))  # Take seventh number input
s.add(int(num))  # Add the number to the set

# Print the set containing all unique numbers entered by the user
print(s)