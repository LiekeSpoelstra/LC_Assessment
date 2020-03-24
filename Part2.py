import random


rwg = random.Random()
terms_list = []
random_words_list = []

with open("assessment.txt") as myfile:
    for word in myfile:
        terms_list.append(word)

print(terms_list)

for i in range(len(terms_list)):
    random_words_list.append(random.choice(terms_list))

print(random_words_list)