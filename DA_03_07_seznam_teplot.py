# Lekce 3, úkol 7: Seznam teplot

# Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu 
# ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
  [2.1, 5.2, 6.1, -0.1],
  [2.2, 4.8, 5.6, -1.0],
  [3.3, 6.5, 5.9, 1.2],
  [2.9, 5.6, 6.0, 0.0],
  [2.0, 4.6, 5.5, -1.2],
  [1.0, 3.2, 2.1, -2.0],
  [0.4, 2.7, 1.3, -2.8]
]


# 1. Vytvořte seznam průměrných teplot pro každý den.
c1 = [sum(t)/len(t) for t in teploty]
print()
print(f'Průměrné denní teploty: {c1}')

# 2. Vytvořte seznam ranních teplot.
c2 = [teplota[0] for teplota in teploty]
print()
print(f'Ranní teploty: {c2}')

# 3. Vytvořte seznam nočních teplot.
c3 = [teplota[3] for teplota in teploty]
print()
print(f'Noční teploty: {c3}')

# 4. Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
c4 = [[teplota[1],teplota[3]] for teplota in teploty]
print()
print(f'Polední a noční teploty: {c4}')

# 5. Spočítejte celkovou průměrnou teplotu za celý týden.
c5 = sum([sum(t) for t in teploty])/sum([len(t) for t in teploty])
print()
print(f'Celková průměrná teplota je {c5} °C.')