import random

#    this code was written by Anna Zwiggelaar and Lieke Spoelstra

bingo_list = []
random_bingo_list = []


def generate_random_list(words_list, rand_list):     # randomize the list of words from the text file
    while len(rand_list) < 25:
        new_word = random.choice(words_list)
        if new_word in rand_list:
            continue
        else:
            rand_list.append(new_word.rstrip("\n"))


def generate_card(words_list, rand_list):            # create a bingo card
    generate_random_list(words_list, rand_list)
    x = rand_list
    a = 0
    card = [[x[a], x[a + 1], x[a + 2], x[a + 3], x[a + 4]], [x[a + 5], x[a + 6], x[a + 7], x[a + 8], x[a + 9]],
              [x[a + 10], x[a + 11], x[a + 12], x[a + 13], x[a + 14]],
              [x[a + 15], x[a + 16], x[a + 17], x[a + 18], x[a + 19]],
              [x[a + 20], x[a + 21], x[a + 22], x[a + 23], x[a + 24]]]
    return card


def print_card(card):                                 # print the bingo card, row by row
    for row in card:
        print("{: >20} {: >20} {: >20} {: >20} {: >20}".format(*row))


def mark_word(coordinate1, coordinate2, card):         # cross off a word based on user input
    card[coordinate1][coordinate2] = "X"


def play_game(words_list, rand_list):                   # play the game by calling all other functions
    card = generate_card(words_list, rand_list)
    print_card(card)
    for i in range(25):
        index1 = int(input("Please enter the first coordinate of the word (x coordinate) : "))
        index2 = int(input("Please enter the second coordinate of the word (y coordinate): "))
        mark_word(index1, index2, card)
        print_card(card)


with open("assessment.txt", "r") as myfile:      # add words in file to bingo list
    for word in myfile:
        bingo_list.append(word.rstrip("\n"))

print("This program will generate a bingo card at random from the words you "
      "entered in program 1.\nProgram 2 draws words from the pool of 35 words "
      "entered by you.\nWhen a word comes up in program 2 that is on your "
      "bingo card, you need to enter the coordinates of that word on your "
      "card in order to mark it.\nThe way to do this is to enter the coordinate "
      "of the row (the x coordinate) first and then enter the coordinate of "
      "the word on that row (the y coordinate).\nThe first row has coordinate 0, "
      "the second row has coordinate 1, etc. The first word on a row has "
      "coordinate 0, the second word has coordinate 1, etc.\nSo, the second "
      "word on the third row would have coordinates 2 (for the row) and 1 "
      "(for the word).")

ready_to_start = input("Enter 'yes' when ready to start the game: ")    # only start when the user is ready
if ready_to_start == "yes":
    play_game(bingo_list, random_bingo_list)

new_game = input("Do you want to play another game? (yes or no) ")    # only play a new game when the user wants to
if new_game == "yes":
    del random_bingo_list[0:len(random_bingo_list)+1]
    play_game(bingo_list, random_bingo_list)
elif new_game == "no":
    print("Thank you for playing. You may close all programs.")
