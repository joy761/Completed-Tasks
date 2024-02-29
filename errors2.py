animal = "Lion"
#synthax error: "Lion" should have "" as a string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
#Logical error: "number_of_teeth" and "animal_type" are positioned 
#Logical error: #added "f" to "full_spec" to call the contents of the curled brackets

print(full_spec)
#synthax error: Missing parentheses