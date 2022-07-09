# Lekce 3, úkol 4: Chytřejší čísla jako text

# Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána 
# nikoliv v seznamu ale v řetězci oddělená mezerou.

from ntpath import join


hodnoty = '12.1 1.68 7.45 -11.51'
print(hodnoty)

# K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto
# hodnoty = '12.1 1.68 7.45 -11.26'
# Určitě se vám budou hodit metody split a join.
# Řešení úkolu 3:

seznam = hodnoty.split(' ')
seznam[-1] = str(float(seznam[-1]) + 0.25)
hodnoty = ' '.join(seznam)
print(hodnoty)

# Úkol 4
# Zkuste vymyslet, jak udělat zápis příkazů z předchozího cvičení co nejúspornější. 
# Dá se dojít až k tomu, že celé řešení bude na jeden řádek v Python konzoli.

print(' '.join('12.1 1.68 7.45 -11.51'.split(' ')[:-1] + [str(float('12.1 1.68 7.45 -11.51'.split(' ')[-1])+ 0.25)]))
