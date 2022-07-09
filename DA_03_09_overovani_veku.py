# Lekce 3, úkol 9: Ověřování věku

# Následující seznam obsahuje věky uživatelů naší malé sociální sítě.

veky = [35, 12, 44, 11, 18, 21, 28, 18]

# 1. Vytvořte pomocí chroustání seznamů seznam celých čísel, které udávají, 
# kolik jednotlivým uživatelům zbývá do 18ti let. Záporná čísla budou znamenat, 
# že uživatel už věk překročil.
v1 = [18 - vek for vek in veky]
print()
print(f'Našim uživatelům zbývá {v1} let do 18.')

# 2. Vytvořte pomocí chroustání seznamů seznam pravdivostních hodnot, 
# které udávají, který uživatel je starší 18ti let.
v2 = [18 - vek for vek in veky]
print()
print(v2)

# 3. Vytvořte pomocí chroustání seznamů seznam pravdivostních hodnot, 
# které udávají, který uživatel má přesně 18 let.
