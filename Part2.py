import random


print("This program will draw words at random. The next program contains "
      "your bingo card.\nIf one of the word drawn here is on your bingo "
      "card, you can cross it off in the next program.\nPlease answer "
      "'yes' when ready for the next word.")
bingo_list = []
random_bingo_list = []

with open("assessment.txt", "r") as myfile:      # add words from file to bingo list
    for word in myfile:
        bingo_list.append(word)

for i in range(len(bingo_list)):            # add words from bingo list to random bingo list
    word = random.choice(bingo_list)        # choose random word from bingo list
    if word in random_bingo_list:           # if word is already in random list, do not add and continue
        continue
    else:
        random_bingo_list.append(word)          # if word is not in random list, add to random list
        answer = input("Are you ready to see the word? ")
        if answer == "yes":
            print(word)