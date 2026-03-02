# Creating an empty set
s = set()
s.add(10)  # Add element 10 to the set
print(s)

print(s.pop())  # Remove and return an arbitrary element from the set
s.update([1, 2, 5])  # Add multiple elements to the set

s.discard(10)  # Remove element 10 if present (no error if not found)
s.remove(5)    # Remove element 5 (raises error if not found)

print(s)
s.clear()  # Remove all elements from the set

#---------------------------------#
A = {1, 2, 3, 4}
B = {3, 9, 8, 7}
C = A.union(B)  # Union of sets A and B
print(type(A))  # Print type of A (should be 'set')
print(C)        # Print union result

#---------------------------------#
D = A.intersection(B)  # Intersection of sets A and B
print(D)

#-------------------------#
print(A.difference(B))  # Elements in A but not in B
print(B.difference(A))  # Elements in B but not in A

#----------------------#
print(A.symmetric_difference(B))  # Elements in A or B but not both

#--------------------#
B.intersection_update(A)  # Update B to keep only elements also in A
print(B)

#-------------------------#
E = {1, 4}
F = {1, 4}
# E.symmetric_difference_update(F)  # Update E to symmetric difference with F (commented out)

print(E)
print(E.issubset(F))     # Check if E is subset of F
print(E.issuperset(F))   # Check if E is superset of F
print(E.isdisjoint(F))   # Check if E and F have no common elements
