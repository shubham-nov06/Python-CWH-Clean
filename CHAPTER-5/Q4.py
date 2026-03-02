s = set()  # Creating an empty set

s.add(18)  # Adding an integer → 18
s.add(18.0)  # Adding a float → 18.0 (BUT: 18 == 18.0, so this is NOT added again)
s.add('18')  # Adding a string → '18' (different from number 18)
s.add("18")  # Adding another string → "18" (same as '18', so NOT added again)

print(s, len(s))  # Prints the set and its size
