# #print() is a function () = argumentt of the function
# print("Hi!", "There")

# #len() is a function
# my_list = ["1", "2", "3"]
# len(my_list)

# #you can execute a function inside of a function
# print(type(my_list))

#creating/declaring your own function and does nothing else!!
# def my_func():
#     my_item = "This is nice"
#     return my_item
# #or 
#     #return "I created a function"

# results = my_func()

# print(results)
#*****************************************************

#another example
# def droid_count(start_count, destoryed_count):
#     results = start_count - destoryed_count
#     return results
       
# print(droid_count(100,23))
# print(droid_count(200,34))


#making a function without return value and it will return None
# def count_quotes():
#     print(len("Quotes"))

# result = count_quotes()
# print(result)

# #Saving in dictionary
# def count_quotes():
#     print(len("Quotes"))
#     return "done"

# thing = {}
# thing["bar"] = count_quotes()
# print(thing)

# #Saving in a list
# def count_quotes():
#     print(len("Quotes"))
#     return "done"

# thing = []
# thing.append(count_quotes())
# print(thing)

##practice
# yoda_quotes = ["wars not make great one", "you will be....you will be."]

# def better_count_quotes(quote_list):
#     return len(quote_list)
#     print('The quote list is complete.')

##first quote on outside while having another quote inside the block 
quote = "The ability to speak does not make you intelligent."
def make_quote():
    quote = "This is not true"
    print(quote)

make_quote()
print(quote)

##This way a way to use recursion in place of a while loop.
def get_word(word = None):
    word = input("Give me a word:\n")
    if not word:
        get_word(word)
    else:
        print("Print your word is: %s" % word)
get_word()