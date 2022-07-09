# Lekce 2, úkol 10: Střed seznamu

# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám 
# padne mezi dvě čísla. V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

s1 = [2, 8.9, 6, 3, 2.1]
s2 = [2, 8.9, 6, 3, 2.1, 3.3]


stred1 = s1[len(s1) // 2]
stred2 = s2[len(s2) // 2]

print(stred1)
print(stred2)