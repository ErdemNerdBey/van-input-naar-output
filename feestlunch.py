croissant_kosten = 39   #cents
stokbrood_kosten = 278  #cents
kortingsbon_kosten = 50 #cents

print('Hoeveel croissanten wilt u?')
croissant_aantal = int(input('Crossanten: '))
print()

print('Hoeveel stokbrodn wilt u?')
stokbrood_aantal = int(input('Stokbrood: '))
print()

print('hoeveel kortings bonnen heeft u')
kortingsbon_aantal = int(input('kortingsbonnen: '))
print()

bedrag = (croissant_kosten * croissant_aantal + stokbrood_kosten * stokbrood_aantal) - kortingsbon_kosten * kortingsbon_aantal

print(f"De feestlunch kost je bij de bakke {bedrag} cent voor de {croissant_aantal} croissantjes en de {stokbrood_aantal} stokbroden als de {kortingsbon_aantal} kortingsbonnen nog geldig zijn!")