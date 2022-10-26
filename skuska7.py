#skusanie druhej mocniny

cislo = float(input('zadaj číslo:'))

od = 0
do = cislo

x = (od + do) / 2

pocet = 0
while abs(x**2 - cislo) > 0.001:
    if x**2 > cislo:
        do = x
    else:
        od = x
    x = (od + do) / 2
    pocet += 1

print('druhá odmocnina', cislo, 'je', x)
print('počet prechodov while-cyklom bol', pocet)