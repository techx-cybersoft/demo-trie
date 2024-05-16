arrChar = ["cat", "bat", "card", "man", "women", "bag", "bimbim"]

getChar = input("Insert your word: ")

matching_words = [word for word in arrChar if word.startswith(getChar)]

if matching_words:
    print(f"Words start with '{getChar}': {', '.join(matching_words)}")
else:
    print(f"No word starts with '{getChar}'")

# def find_word(arrChar, getChar):
#     word_found = []
#     for word in arrChar:
#         if getChar in word:
#             word_found.append(word)

#     return word_found

# find = find_word(arrChar, getChar)
# for word in find:
#     print(word)

