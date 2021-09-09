toegangticket = 745   #cents
minuut_kosten = 8  #cents

print('Hoeveel personen zijn jullie?')
personen = int(input('Personen: '))
print()

print('Minuten VR wilt u spelen?')
minuten_vr = int(input('Aantal minuten VR: '))

print(f'Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {minuten_vr} minuten VR kost je maar {personen * toegangticket + personen * minuten_vr * minuut_kosten} cent')