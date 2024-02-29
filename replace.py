#Declare a string
#store string in a variable called "sentence"
#replace every "!" with space " "
#print new sentence in upper case
#print sentence backwards

 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog"
new_sentence = sentence.replace("!", " ")
sentence_2 = new_sentence.upper()
sentence_3 = sentence_2[::-1]

print(new_sentence)
print(sentence_2)
print(sentence_3)
