# Initialize an empty dictionary to store names and their best languages
dict = {}

# Take first user's name and best language as input
name = input("Enter you name = ")
lang = input("Enter your best language = ")

# Update the dictionary with the first user's data
dict.update({name:lang})

# Take second user's name and best language as input
name = input("Enter you name = ")
lang = input("Enter your best language = ")

# Update the dictionary with the second user's data
dict.update({name:lang})

# Take third user's name and best language as input
name = input("Enter you name = ")
lang = input("Enter your best language = ")

# Update the dictionary with the third user's data
dict.update({name:lang})

# Take fourth user's name and best language as input
name = input("Enter you name = ")
lang = input("Enter your best language = ")

# Update the dictionary with the fourth user's data
dict.update({name:lang})

# Print the final dictionary containing all users and their best languages
print("Your best languages are ", dict)
