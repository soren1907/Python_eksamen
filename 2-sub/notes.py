#   Python OO   -   Class og instancer
#   synopsis dunder funtions i stedet for "built in funtions"
#   *Lav en klasse Dice (value, color) uden constructor og en roll metode

class Dice:
    
    value = None
    color = None

    def roll(self):
        print(f"my value is {self.value}")
    
#   *Lav instans af klasse og kald roll

dice1 = Dice()
dice1.roll()

#   laves nu med construcor (ikke private) 

class Dice():

    def __init__(self, value, color):
        self.__value = value
        self.__color = color
    
    def __str__(self):
        return "value: " + str(self.__value) + " color: " + self.__color

    def __add__(self, other):
        return self.__value + other.__value

    def roll(self):
        print("i landed on " + str(self.__value))


#   *Tilføj "dunder metoder" ^ en str og add
#   python datamodel - "built in funtions to interact with objects"
#   *test dem herunder*

dice1 = Dice(3, "white")
print(dice1)

dice2 = Dice(1, "white")
print(dice2+dice1)

#   Inherintance MagicDice der nedarver fra Dice. override roll

class MagicDice(Dice):
    
    def roll(self):
        print("i landen on the corner!")

#   test magic_dice her

magic_dice = MagicDice(4, "red")
dice1.roll()
magic_dice.roll()

#   *Gør attributter private i Dice-klassen^
#   Vis at man ikke kan få adgang til dem (med mindre?)

print(dice1._Dice__value)
print(dice1._Dice__color)


#   Getters and setters med @property og @value.setter
#   copy/paste Dice klasse og ændre herunder

class Dice():

    def __init__(self, value, color):
        self.value = value #bruger value.setter (bliver private)
        self.__color = color

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    
    def __str__(self):
        return "value: " + str(self.__value) + " color: " + self.__color

    def __add__(self, other):
        return self.__value + other.__value

    def roll(self):
        print("i landed on " + str(self.__value))

#   Set value & get value

dice1 = Dice(5, "green")
dice1.value = 1
print(dice1)


