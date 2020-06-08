#prints number of each letter from word given
word = input("Give me a word:\n")
letter_list = {}
for letter in word:
    if(letter in letter_list):
        letter_list[letter] += 1
    else:
        letter_list[letter] = 1
    
print(letter_list)

my_list = sorted(letter_list)
print(my_list)

#prints all of the separate keys
# top_3 = []
# for letter in letter_list:
#     print(letter)

#prints the highest 
# top_3 = []
# highest = 0
# for letter in letter_list:
#     if letter_list[letter]> highest:
#         highest = letter_list[letter]

# print(highest)

#prints 
# top_3 = []
# for i in range(0,2):
#     highest = None
#     highest_value = 0
#     for letter in letter_list:
#         if letter_list[letter] > highest_value:
#             highest_value = letter_list[letter]
#             highest = letter
#     print(highest, highest_value)
#     del letter_list[letter]
