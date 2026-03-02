s = set()  # sets are mutable (not immutable) , SETS IS A collection of well defined objects
s.add(3)  # adding an element to the set
print(s.pop())
# NOTE:
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. You cannot change items in a set, but you can add/remove
# 4. Sets cannot contain duplicate values.

g = set()

# Taking input from user and adding to set
for i in range(3): 
    inp = int(input("Enter numbers here: "))
    g.add(i)

print("Set g:", g)
print("Length of s:", len(s))

#) will give error if element not present, so we check remove(
if 2 in s:
    s.remove(2)
    print("2 removed from s")
else:
    print("2 is not present in set s")
print(s)

