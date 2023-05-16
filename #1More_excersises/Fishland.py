    price_skumriq_kg = float(input())
    price_caca_kg = float(input())
    ьkg_palamud = float(input())
    kg_safrid = float(input())
    kg_midi = int(input())

    price_palamud = (price_skumriq_kg * 0.6) + price_skumriq_kg
    sum_palamud = price_palamud * kg_palamud
    cena_safrid = (price_caca_kg * 0.8) + price_caca_kg
    sum_safrid = cena_safrid * kg_safrid
    sum_midi = kg_midi * 7.5

    total_price = sum_palamud + sum_safrid + sum_midi
    print(f"{total_price:.2f}")
