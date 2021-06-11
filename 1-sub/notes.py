#   De 4 "built-in data structures"
#   Synopsis: gennemgår kun iterating for list  

#   List vs Tuples - Hvad er forskellen på de 2. 
#   Hvornår skal man bruge tuples?

#   syntax for lists?: (lists af colors 3)
colors_list = ['red', 'blue', 'green']

#   syntax for tubles?: (samme)
colors_tuple = ('red', 'blue', 'green')

#   indexing: Få et element fra hver
color1 = colors_list[-1]
color2 = colors_tuple[0]

#   Slicing for beggec - returnerer del af list/tuple
#   (list de første, tuple 2 sidste)
new_colors_list = colors_list[:2] 
new_colors_tuple = colors_tuple[1:]

#   ændre elementer i list
colors_list[1] = "grey"

#   tilføje og fjerne fra list (fjern både med pop og remove)
colors_list.append("purple")
colors_list.pop(2) #tom parantes fjerner sidste
colors_list.remove("grey")

#   tuples 2 metoder.. count og index

print(colors_tuple.index("red"))
print(colors_tuple.count("red"))

#   Dictionary - regler for key - mutable
#   *Lav en dictionary, tiløj 1 ny key/value 
#   og ændre en af farverne(value) efter

colors_dict = {1: "red", 2: "blue", 4: "yellow"}
colors_dict[5] = "white"
colors_dict[1] = "purple"
print(colors_dict)

#   {Set} - Regler: immutable(?), unique, unordered
#   *Lav sæt, tilføj element, slet element
colors_set = {"blue", "red", "brown"}
colors_set.add(42)
colors_set.remove("blue")

#   Set operation (Union , intersection, difference, Symmetric Difference)
#   Viser kun intersection

a = {"blue", "red", "brown"}
b = {"green", "red", "grey"}

print(a & b)

#   *Iterating the list - Vis både for-loop & iter

for i in colors_list:
    print(f"color: {i}")

iter_list = iter(colors_list)
print(next(iter_list))

#   list coprehension (hvis der er tid?)
#   *brug list comprehension til at få colors med mere 
#   end 3 bogstaver til en ny list

new_list = [x for x in colors_list if len(x) > 3]

