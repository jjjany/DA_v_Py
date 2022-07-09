# Lekce 2, úkol 5: Průměrné teploty

# Následující tabulka obsahuje průměrné roční teploty v České republice 
# za roky 2001 až 2010 (zdroj: Český hydrometeorologický ústav).

# rok 	teplota °C
# 2001 	7.8
# 2002 	8.7
# 2003 	8.2
# 2004 	7.8
# 2005 	7.7
# 2006 	8.2
# 2007 	9.1
# 2008 	8.9
# 2009 	8.4
# 2010 	7.2

# Vytvořte reprezentaci této tabulky pomocí seznamu seznamů. Zde existují dvě možnosti. 
# Nejprve vytvořte seznam, který obsahuje řádky tabulky jako dvouprvkové seznamy 
# a uložte jej do proměnné radky. Poté vytvořte seznam, který obsahuje sloupce tabulky,
# tedy dva seznamy po deseti prvcích. Uložte jej do proměnné sloupce.
radky = [[2001, 7.8],[2002, 8.7],[2003, 8.2],[2004, 7.8],[2005, 7.7],[2006, 8.2],
[2007, 9.1],[2008, 8.9],[2009, 8.4],[2010, 7.2]]
sloupce = [[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
[7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]]

# Pro obě tyto reprezentace vyřešte následující úkoly

# 1. Získejte teplotu na třetím řádku tabulky.
print(radky[2][1])
print(sloupce[1][2])
print()

# 2. Získejte rok na pátém řádku tabulky.
print(radky[4][0])
print(sloupce[0][4])
print()

# 3. Získejte poslední řádek tabulky jako seznam.
print(radky[-1])
print([sloupce[0][-1], sloupce[1][-1]])
print()

# 4. Vytvořte tabulku bez prvních dvou řádků.
print(radky[2:])
print([sloupce[0][2:], sloupce[1][2:]])
print()

# 5. Vytvořte tabulku pouze z prvních dvou řádků.
print(radky[:2])
print([sloupce[0][:2], sloupce[1][:2]])
print()

# 6. Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8.
print(radky[4:8])
print([sloupce[0][4:8], sloupce[1][4:8]])
print()

# 7. Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti.
# Šlo by to i pomocí proměnné radky, ale to ještě neumíme.
print([sorted(sloupce[1])])
print()
# obměna
seznam_teplot = sloupce[1]
seznam_teplot.sort()
# seznam_teplot.reverse()  # vrátilo by otočený seznam
print(seznam_teplot)
