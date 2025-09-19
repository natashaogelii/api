# ordered, mutable, unique keys, fast lookups.
# Basic usage

# empty dictionary
new_dict = {}
print(type(new_dict))

new_dict2 = {
    "name" :"Jason",
    "number":123456,
    "units":[1,2,3,4,5,6]
}
print(f"The name {new_dict2["name"]} ")

# print(new_dict2)

# Updating
new_dict2["number"] = 987654
# print(new_dict2)

# Adding new key
new_dict2["id_num"] = 258147
# print(new_dict2)

print(new_dict2.keys())
print(new_dict2.values())
print(new_dict2.items())

# Iterating
# getting key and value
for key,value in new_dict2.items():
    print(f"key is {key} value is {value}")



