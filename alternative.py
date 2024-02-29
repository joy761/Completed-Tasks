string = ("Hello World")
new_string = ""

for i in range(len(string)):
#for loop for repeat operation
    if i % 2 == 0:
        new_string += string[i].upper()
        #if item index divides by 2, then convert to uppercase
    else:
        new_string += string[i].lower()
       #otherwise convert to lowercase
print(new_string)


string = ("I have a new house")      

split_string = string.split()                         
#to store the split string -creates a list

final_string = ""                                     
#to compile the resulting string

for i in range(len(split_string)):                      
    #for loop for repeat operation

    if i % 2 == 0:
        final_string += split_string[i].upper() + " "   
        #if item index divides by 2 then convert to uppercase

    else:
        final_string += split_string[i].lower() + " "   
        #otherwise convert to lowercase

print(final_string)