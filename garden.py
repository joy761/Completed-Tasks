import spacy
nlp = spacy.load('en_core_web_sm')

#List two garden path sentences and then add three to the list
gardenpathSentences = [
    "The old man the boat",
    "The sour drink from the ocean"]
gardenpathSentences.append("Mary gave the child a Band-Aid")
gardenpathSentences.append("That jill is never here hurts")
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi")
print(f"\nGarden Path Sentences: ")


for sentence in gardenpathSentences:
    print(f"\m{sentence}")


#Iterate through the path sentences to tokenize and extract named entities using spacy's NER function
for sentence in gardenpathSentences:
    doc=nlp(sentence)

    tokens = [token.text for token in doc] 
    print(f"\nTokenised sentence: {tokens}")

    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Named entities: {entities}")

    #use spacy.explain to look up and print the meaning of each sentence
    for ent_text, ent_label in entities:
        explain = spacy.explain(ent_label)
        print(f"Meaning of '{ent_text}' (entity label '{ent_label}'): {explain}")

        #write comment on entity explanation
        if ent_text == "Mary":
            print("\nComment: The entity 'Mary' correctly identified as a 'Person', and this makes sense in terms of the word associated in the sentence ")
        elif ent_text == "Mississippi":
            print("\nComment: The entity 'Mississippi' is labeled a 'Geopolitical entity. within the context of the sentence, it is appropriate because Mississipi is indeed the name of a place" )

   