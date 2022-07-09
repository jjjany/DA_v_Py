# Lekce 3, úkol 2: Čísla jako text


# Mějme seznam desetinných čísel zadaných jako text

hodnoty = ['12', '1', '7', '-11']

# Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:
# hodnoty = ['12', '1', '11', '-11']

# Před tím, než se podíváte na následující kroky, sami si rozmyslete postup, 
# jak toto provést. Až když si nejste jistí, pokračujte podle následujících kroků.

hodnoty[2]= str(int(hodnoty[2])+4)
print(hodnoty)


# 1. Uložte si hodnotu na třetí pozici v seznam do nějaké proměnné.
# 2. Převeďte tuto hodnotu na číslo a přičtěte k němu 4. Výsledek uložte do proměnné 
# vysledek.
# 3. Převeďte hodnotu v proměnné vysledek zpět na řetězec a uložte ji 
# na třetí pozici v seznamu hodnoty.

