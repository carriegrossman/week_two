# import random

# class Dice():
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
        

# six_sided_dice = Dice('6',random.randint(1,6))
# twelve_sided_dice = Dice('12',random.randint(1,12))
# twenty_sided_dice = Dice('20',random.randint(1,20))

# # count_dice_rolled = {}
# # count = 1

# while True:
#     try:
#         user = int(input("Choose a dice to roll: 6, 12, or 20 sided dice \n"))
#     except ValueError:
#         print("That's not a number!")
    

#     if user == 6:
#         rolled = six_sided_dice.value
#         count +=1
#         count_dice_rolled.update({count: rolled})
#     elif user == 12:
#         rolled = twelve_sided_dice.value
#         count +=1
#         count_dice_rolled.update({count: rolled})
#     elif user == 20:
#         rolled = twenty_sided_dice.value
#         count +=1
#         count_dice_rolled.update({count: rolled})
#     else:


#clint in class
import random

class Dice():
    def __init__(self, sides):
        self.sides = sides
        self.rolls = []

    def roll(self):
        roll = random.randint(1, self.sides)
        print("You rolled a : %s" % roll)
        self.rolls.append(roll)

dice = {
    "d6": Dice(6),
    "d12": Dice(12),
    "d20": Dice(20)
}

dice["d6"].roll()