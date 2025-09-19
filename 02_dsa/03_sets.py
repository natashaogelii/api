# mutable, unordered, unique items only

# empty set not {}
new_set1 = set()

# set with values
new_set = {1,1,2,3,3,4,5}
print(type(new_set))
print(new_set)

# Remove duplicates
new_list = [1,1,2,3,3,4,5]
print(new_list)
print(set(new_list))

# Remove
new_set.remove(2)    # error if not found
new_set.discard(10)  # safe remove
new_set.pop()        # remove random element because it is unordered
new_set.clear()

# Membership test
print(1 in new_set)
print(6 in new_set)

# Adding and removing
print(new_set)

new_set.add(25)
print(new_set)

new_set.discard(2)
print(new_set)
