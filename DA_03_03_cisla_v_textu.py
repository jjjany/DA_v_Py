# Lekce 3, úkol 3: Čísla v textu

# Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána 
# nikoliv v seznamu ale v řetězci oddělená mezerou:

hodnoty = '12.1 1.68 7.45 -11.51'
print(hodnoty)

# K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto

# hodnoty = '12.1 1.68 7.45 -11.26'

# Určitě se vám budou hodit metody split a join.

seznam = hodnoty.split(' ')
seznam[-1] = str(float(seznam[-1]) + 0.25)
hodnoty = ' '.join(seznam)
print(hodnoty)

