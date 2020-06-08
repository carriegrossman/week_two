# # #1
# def madlib(name, subject):
#     name = input("Choose a name: \n")
#     subject = input("Choose a subject \n")
#     print("%s enjoys %s" % (name, subject))
#     return
# madlib('name', 'study')

#2
# def temp():
#     temperature = int(input('What is the temperature in celsius degrees? \n'))
#     degrees = (temperature * 9/5) + 32
#     print('It is %s degrees Farenheit outside' % degrees)
# temp()

##second way to do it 
# def convert(celsius):
#     degrees = (celsius * 9/5) + 32
#     # print('It is %s degrees Farenheit outside' % degrees)
#     return degrees
# temperature = int(input('What is the temperature in celsius degrees? \n'))
# print(convert(temperature))

#3
# def temp2():
#     temperature = int(input("What is the temperature in farenheit degrees? \n"))
#     degrees = (temperature - 32) * 5/9
#     print('It is %s degrees Celsius outside' % degrees)
#     return
# temp()

# #4
# def even(num):
#     result = False
#     if num % 2 == 0:
#         result = True
#     return result

# print(even(2))
# print(even(5))

# #5
# def odd(num):
#     result = False
#     if num % 2 != 0:
#         result = True
#     return result

# print(odd(2))
# print(odd(5))

# #6
# def is_evens(list):
#     evens_list = []
#     for i in list:
#         if i %2 == 0:
#             evens_list.append(i)
#     return evens_list
# print(is_evens([11, 20, 42, 97, 23, 10]))

# #7
# def is_odd(list):
#     odds_list = []
#     for i in list:
#         if i %2 != 0:
#             odds_list.append(i)
#     return odds_list
# print(is_odd([11, 20, 42, 97, 23, 10]))
