# Lekce 3, úkol 5: Seznamy čísel

# Mějme zadaný následující seznam

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]

# Vytvořte seznam, který obsahuje

# 1. každé z čísel ze seznamu cisla vynásobené dvěma,
c1 = [cislo * 2 for cislo in cisla]
print()
print(c1)

# 2. každé z čísel ze seznamu cisla s opačným znaménkem,
c2 = [cislo * -1 for cislo in cisla]
print()
print(c2)

# 3. každé z čísel ze seznamu cisla umocněné na druhou,
c3 = [cislo ** 2 for cislo in cisla]
print()
print(c3)

# 4. každé z čísel ze seznamu cisla jako řetězec.
c4 = [str(cislo) for cislo in cisla]
print()
print(c4)