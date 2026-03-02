# () - this is used to make tuple in python 

a = (1, 2, 3, 4 , "Shubham" , "Shubham" , "Pankaj")

print(type(a))
print(a)

# a[0] = "Shubham"  TypeError: 'tuple' object does not support item assignment
# We cannot chnage tuple value like string 

b = (20 , 1 , 2 , 5, 10)

count = a.count("Shubham")

print(count)  # this will return 2 bcz there are 2 shubham in the tuple 

print(a.index(3))
print(a.index("Shubham"))

print(len(a))
print(min(b))
print(max(b))

print(sum(b))
print(sorted(b))

c = a + b
print(c)

d = a * 2
print(d)

print(1 in a)
print("shubham" in a)

print(200 not in a)
print(1 not in a)
# Tuple Slicing
e = (1, 2, 3, 4, 5, 6, 7, 8)
print(e[1:4])
print(e[4:8])
print(e[-7:])

# Tuple unpacking

f = (1, 2, 3)
a , b , c = f
print(f)
print(a, b, c)

# Nested Touple 
g = (1, 2, (3, 4), (5, 7))
print(g[2][0])
print(g[3][0])
print(g[0])

# Convert list to tuple
lsst = [1, 2, 3, 4]
t = tuple(lsst)
lsst.append(30)
print(lsst)

print(t)
print(type(t))

# Convert tuple into list (useful because tuple is immutable)
h = (20, 30, 40, 50)
lst = list(h)

lst.append(20)
print(lst)

# Tuple of different data types
t = (10, "hello", 3.5, True)
print(t)

# Tupples as dictinary keys 
i = {(1, 2): "Shubham" }
j = { 
    (1, 2): "Point A" ,
    (3, 4): "Point B" ,
    (5, 6):"Point c"
    } 

print(j[1, 2])

print(j[3, 4])

print(j[5, 6])
