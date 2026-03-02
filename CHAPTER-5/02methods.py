# Dictionary initialization with mixed key types
marks = {
    0: 20,
    'a': "Yo",
    "Shub": 2000,
    # no special charater initilization ! : 90,
}

print(marks.get('a'))  # Print value for key 'a'
print(marks.get("Shub"))  # Print value for key "Shub"

print(marks.keys())  # Print all keys in the dictionary
print(marks.values())  # Print all values in the dictionary
print(marks.items())  # Print all key-value pairs as tuples

num = marks.update({'a': 40})  # Update value for key 'a'
print(num)  # update() returns None

print(marks.pop('a'))  # Remove key 'a' and print its value
print(marks)  # Print dictionary after removal

print(marks.popitem())  # Remove and print the last inserted key-value pair
print(marks)  # Print dictionary after popitem

# Another dictionary example
number = {
    1: 20,
    2: 30,
    3: 40,
}

print(number.clear())  # Remove all items from the dictionary (returns None)
print(number)  # Print empty dictionary

# Copying a dictionary
name = {
    1: "Shubham",
    2: "Pankaj"
}
c = name.copy()  # Create a copy of the dictionary
print(c)

print(name.setdefault(2))  # Return value for key 2, does not change dictionary
print(name.setdefault(3, "Rupali"))  # Add key 3 with value "Rupali" if not present

# Creating dictionary from keys with default value
keys = [1, 2, 3, 4]
d = dict.fromkeys(keys, 0)  # All keys initialized to 0
print(d)
d[1] = 20  # Update value for key 1
d[2] = 30  # Update value for key 2
d[3] = 40  # Update value for key 3
d[4] = 30  # Update value for key 4
print(d)

# Update dictionary values from user input
for i in d:
    value = input("enter the values ")
    d[i] = value

print(d)

#------------------------------------------------#
# Another example of fromkeys and user input
keys1 = [20, 30, 40, 50]
d1 = dict.fromkeys(keys1)

for j in keys1:
    num = input("Enter the key values")
    d1[j] = num

print(d1)

#------------------------------------------------#
# Yet another example with fromkeys and user input
shu = [2, 3, 4, 5]
s = dict.fromkeys(shu, 0)
print(s)

for s1 in shu:
    inp = input("Enter number in shu ")
    s[s1] = inp

print(s)
if 2 in shu:
    print("exists")  # Check if 2 is in the list shu

print(len(shu))  # Print length of the list shu
