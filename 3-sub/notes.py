#   Fejl i synopsis
#   Hvad vil jeg vise?

#   Decorator - Hvad bruges det til?
#   Viser et eksempel på egne dekorator

#   vis en simpel funktion der dividere 2 tal

def divide(x,y):
    return x/y

#   Lav decorator der forhindre dividering med 0

def smart_divide(func):
    
    def inner(x,y):
        print("dividing ", x, "and ", y )
        if y == 0:
            print("can't divide")
            return

        return func(x,y)

    return inner


#   dekorer divide og giv den returnerede funktion fra decoratoren et navn
result = smart_divide(divide)
print(result(8,3))

#   Decorate divide-funktionen fra før med @ istedet 

@smart_divide
def divide2(x,y):
    return x/y

# Test den nye funktion både med 0 og uden
result2 = divide2(50,5)
print(result2)


#   Iterator class vs Generators func
#   Problem der skal løses ved begge typer:
#   gange et tal med self selv x antal gange

#   klassen laves med next og iter - metode

class AddSameNumber:

    def __init__(self, number, times):
        self.number = number
        self.times = times

    def __iter__(self):
        self.start = 0
        return self
    
    def __next__(self):

        if self.start >= self.times:
            raise StopIteration
        
        self.number += self.number
        self.start += 1
        return self.number

#   Der testes ved at lave en instans af klasse & iterator af objektet
#   Brug next til at komme med input
addSameNumber = AddSameNumber(1,5)
iterate = iter(addSameNumber)

print(next(iterate))
print(next(iterate))
print(next(iterate))


#   interrate klassen AddSameNumber med forloop

for i in AddSameNumber(1,5):
    print(i)

#   Samme eksempel laves nu med en generator
#   ingen __iter__ , __next__ & stopIteration, men yield i stedet
#   forskel på yield og return

def add_same_number(number, times):
    start = 0
    while start < times:
        start +=1
        number += number
        yield number
    
#   Der Laves en iterator ud fra metoden

it = add_same_number(1,4)
print("----------")
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#   metoden bruges i et forloop

for i in add_same_number(10,4):
    print(i)

