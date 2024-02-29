#request input from user (input should be a sentence)
#save input in a variable called "str_manip"
#calculate and display the length of "str_manip"
#find the last letter in "str_manip" and replace every occurence of this with "@"
#print the last 3 character in "str_manip" backwards
#create a five-letter word that is made up of the the first three characters and the last two characters in "str_manip"

str_manip = input("Enter a sentence:")
str_manip_2 = str_manip[-1]
str_manip_3 = str_manip.replace(str_manip_2, "@")
str_manip_4 = str_manip[-3:]
str_manip_5 = str_manip[:4]
str_manip_6= str_manip[-2:]


print(len(str_manip))
print(str_manip_2)
print(str_manip_3)
print(str_manip_4[::-1])
print(str_manip_5 + str_manip_6)
