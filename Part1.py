
list_of_terms = []

for i in range(5):
    new_word = input("Please enter a word: ")
    list_of_terms.append(new_word)

print(list_of_terms)

with open("assessment.txt", "w") as myfile:
    myfile.write(str(list_of_terms))
