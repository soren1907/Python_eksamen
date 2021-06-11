#   Module vs Script? (Hvilke modules er der?)

#   Jeg Bruger først et built in module -OS
#   Der skal oprettes en mappe, skiftes CWD, laves (open, w) og skrives til txt-fil

import os

print(os.getcwd());
os.mkdir("testfolder")
os.chdir("./testfolder")

my_file = open("info.txt", "w")
my_file.write(input())

#   Jeg laver mit eget module mymodule.py (verdens mest simple)
#   jeg kan hente det hele ned.

import mymodule
mymodule.say_my_name("soren")

#   Eller enkelte dele fra det

from mymodule import say_my_name
say_my_name("soren")

#   3rd party module:
#   Her kommer pip ind i billedet.. *Jeg viser pip uden docker*

#   Vis webpage.py

#   Docker og pip - *Jeg starter en container fra et python image*
#   hvad er der i pip list?
#   Installerer flask og opretter requirements.txt

#   Vise sidste del hvor et image laves og en container køres ud fra det image (ingen ${PWD})
#   brug projekt mappen på skrivebord




