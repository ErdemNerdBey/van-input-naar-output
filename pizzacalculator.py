#Erdem Uysal opdracht:pizza calculator
small_pizza_prijs = 5.69
medium_pizza_prijs = 6.97
large_pizza_prijs = 8.98

print('welkom bij Pizza Lakakakaa')
print('wat wilt u vandaag eten?')
print()
print('           MENU')
print('| small pizza: 5,69 euro   |')
print('| medium pizza: 6,97 euro  |')
print('| large pizza : 8,98 euro  |')
print()

print('Hoeveel small pizzas wilt u?')
aantal_small_pizza = float(input('small pizza: '))
print()

print('Hoeveel medium pizzas wilt u?')
aantal_medium_pizza = float(input('medium pizza: '))
print()

print('Hoeveel large pizzas wilt u?')
aantal_large_pizza = float(input('large pizzas: '))
print()

bedrag = aantal_small_pizza * small_pizza_prijs + aantal_medium_pizza * medium_pizza_prijs + aantal_large_pizza * aantal_large_pizza

print(f'u heeft {int(aantal_small_pizza)} small pizzas, {int(aantal_medium_pizza)} medium pizzas en {int(aantal_large_pizza)} large pizzas bestelt')
print(f'uw totale bedrag is {bedrag} euro')