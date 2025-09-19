# mutable, ordered, allows duplicates, slicing
# Creating and accessing

mylist = [15,1,2,1,3,4,5,6,7]
print(mylist)
# accessing the first item
print(mylist[0])

# accessing the last item
print(mylist[-1])

# # replace
mylist[0] = 936
print(mylist[0])

# # Adding elements
# insert at an index
mylist.insert(0,25)
print(mylist[0])

# append / ass item at the end
mylist.append(258)
print(mylist)

# Removing elements
mylist.remove(1)
print(mylist.remove(3))   # remove by value (error if not found)
mylist.pop()       # remove last
mylist.pop(1)      # remove at index
del mylist[0]      # delete index
mylist.clear()     # empty the list

print(f"Show all values {mylist}")
# List slicing
# start
print(f"Start from 4th index {mylist[4:]}")

# stop
print(f"Stop before index 5  {mylist[:5]}")

# start and stop
print(f"Start and index 3 stop before index 6 {mylist[3:6]}")

print(mylist)
# List comprehension - one liner
new_list = [x * 2 for x in mylist]
print(new_list)

# Nesting (2D lists)
new_list2 = [[1,2,3],
             [4,5,6]]
print(new_list2[1][2])

