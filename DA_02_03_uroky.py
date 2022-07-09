# Lekce 2, úkol 3: Úroky

# Fíha banka a.s. nabízí na svých stránkách spořící účet s úrokem 2.4 %. 
# Když si na takový účet uložíte 1 000 000 kč, kolik peněz nastřádáte za 10 let?

urok = 0.024
ulozeno = 1000000

zustatek_za_1_rok = ulozeno * (1 + urok)
zustatek_za_2_roky = zustatek_za_1_rok * (1 + urok)
zustatek_za_3_roky = zustatek_za_2_roky * (1 + urok)
zustatek_za_4_roky = zustatek_za_3_roky * (1 + urok)
zustatek_za_5_let = zustatek_za_4_roky * (1 + urok)
zustatek_za_6_let = zustatek_za_5_let * (1 + urok)
zustatek_za_7_let = zustatek_za_6_let * (1 + urok)
zustatek_za_8_let = zustatek_za_7_let * (1 + urok)
zustatek_za_9_let = zustatek_za_8_let * (1 + urok)
zustatek_za_10_let = zustatek_za_9_let * (1 + urok)

print(zustatek_za_10_let)

# požadované řešení
za_10_let = ulozeno * (1 + urok)**10
print(za_10_let)

# pokročilejší řešení
na_uctu = 1000000
for i in range(10):
    na_uctu = na_uctu * (1 + urok)
print(na_uctu)