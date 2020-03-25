bingo_card = [[1, 2, 3, 4, 5], [6, 7, 8, "pet", 10],
              [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]

index1 = int(input("Enter the first coordinate of the word on your card: "))
index2 = int(input("Enter the second coordinate of the word on your card: "))

print(bingo_card[index1][index2])

word1 = bingo_card[index1][index2]


def strikethrough(word):
    result = ""
    for letters in word:
        result = result + letters + "\u0336"
    return result


print(strikethrough(bingo_card[1][3]))




answer = input("Do you want to play another game? ")

if answer == "yes":
    generate new card
elif answer == "no":
    print("Thank you for playing. You may now close this window.")
    break
