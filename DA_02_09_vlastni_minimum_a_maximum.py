# Lekce 2, úkol 9: Vlastní minimum a maximum

# Prohlédněte si funkce pro práci se seznamy uvedené dříve v obsahu lekce. 
# Představte si, že bychom neměli k dispozici funkce min() a max(). 
# Dokázali byste vytvořit výraz, který zjistí minimální resp. maximální hodnotu 
# v seznamu uloženém v proměnné s? Můžete v tomto vzorečku použít cokoliv, 
# co jsme probrali na lekci kromě samotných funkcí min() a max().

s = [2, 8.9, 6, 3, 2.1, 3.3]

maximum = sorted(s)[-1]
minimum = sorted(s)[0]

print(sorted(s))
print(maximum)
print(minimum)