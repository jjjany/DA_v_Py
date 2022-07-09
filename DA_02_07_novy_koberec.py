# Lekce 2, úkol 7: Nový koberec
# Do místnosti tvaru čtverce o rozloze 30 m2 potřebujeme koupit nový koberec. 
# Jakou délku má mít strana koberce? Vejde se nám srolovaný do dodávky 
# s nákladovým prostorem dlouhým 5 m?
strana = 30**0.5
if strana <= 5:
    odpoved = 'vejde'
else:
    odpoved = 'nevejde'

print(f"Strana koberce má délku {strana} metrů a proto se do nákladového prostoru dodávky {odpoved}.")