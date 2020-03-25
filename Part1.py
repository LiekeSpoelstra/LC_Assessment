
list_of_terms = []

while len(list_of_terms) < 35:      # add 35 terms to the list
    new_word = input("Please enter a word: ")
    if new_word not in list_of_terms:       # only add term when it is not in the list yet
        list_of_terms.append(new_word)
    elif new_word in list_of_terms:
        print("You have already added this word. Please add a new word.")

print("Thank you! Please proceed to the next program.")

with open("assessment.txt", "a") as myfile:     # write the list of terms to a text file
    for word in list_of_terms:
        myfile.write(word)
        myfile.write("\n")

frequencies = {}        # create an empty dictionary
for word in list_of_terms:
    frequencies[word] = frequencies.get(word, 0) + 1        # count the number of times a word was added

print(frequencies)

