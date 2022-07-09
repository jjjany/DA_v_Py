# Lekce 2, úkol 10: Střed seznamu

# Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed 
# v zadaném seznamu s. Tentokrát však u seznamů sudé délky vyberte jako střed 
# číslo blíž k začátku seznamu.

s1 = [2, 8.9, 6, 3, 2.1]
s2 = [2, 8.9, 6, 3, 2.1, 3.3]


stred1 = s1[-(len(s1) // 2 + 1)]    # alter: stred = s[(len(s) - 1) // 2]
stred2 = s2[-(len(s2) // 2 + 1)]

print(stred1)
print(stred2)