# [] - this is used to make the list

friends = [ "apple" , "banana" , 10 , True , False , 20.9999 ] 
friends.append("Pankaj")  # append is used to add at the last of the list 
print(friends)  # List will change everytime when you do anything 

num = [ 1, 3, 4, 6, 2, 7, 10, 9]
num.sort()
print(num)

num.reverse()
print(num)

num.insert(0, 11)
print(num)

num.__delitem__(0)
num.__delitem__(2)
print(num)

num.extend(["Shubham", "Dogra"])
print(num)

num.remove("Shubham")
print(num)

print(num.index("Dogra"))

remove = num.pop(6)
print(remove)
print(num)

num.clear()
print(num)

int = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(int.count(3)) 
print(int.count(10))

print(friends.count("banana"))   
print(friends.count("Pankaj"))

print(friends.count(10))
print(friends.count(True))

print(friends.count(False)) 
