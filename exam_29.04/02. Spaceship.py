from math import floor
shirina_korab = float(input())
daljina_korab = float(input())
visochina_korab = float(input())
sredna_visochina_astronavti = float(input())
obem_na_raketata = shirina_korab * daljina_korab * visochina_korab
obem_na_staq = (sredna_visochina_astronavti + 0.40) * 2 * 2
mqsto = floor(obem_na_raketata / obem_na_staq)

if 3 <= mqsto <= 10:
    print(f"The spacecraft holds {mqsto} astronauts.")
if mqsto < 3:
    print("The spacecraft is too small.")
if mqsto > 10:
    print("The spacecraft is too big.")

