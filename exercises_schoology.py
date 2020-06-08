# #1
# words = {
#     "noun" : [
#         'car', 'dog', 'house'
#     ], 
#     "noun2" : [
#         'pool', 'cat', 'tree'
#     ],
#     "verb" : [
#         'ate', 'jumped', 'ran', 'climbed'
#     ]
# }
# noun = words["noun"][1]
# noun2 = words["noun2"][0]
# verb = words["verb"][1]

# def sentence(noun, verb, noun2):
#     return "The %s %s, the %s!" % (noun, verb, noun2)
# print(sentence(noun, verb, noun2))


import random

def make_random_sentence():
  words = {
      'noun' : ["car", "cat", "girl", "house"],
      'verb' : ["ran", "hit", "jumped", "drove"]
  }
