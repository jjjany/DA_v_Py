# Lekce 3, úkol 6: Seznamy řetězců

# Mějme zadaný následující seznam

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

# Vytvořte seznam, který obsahuje

# 1. počty písmen ve všech jménech,
c1 = [len(jmeno) for jmeno in jmena]
print()
print(c1)

# 2. všechna jména napsaná velkými písmeny,
c2 = [jmeno.upper() for jmeno in jmena]
print()
print(c2)

# 3. všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména),
c3 = [jmeno + 'a' for jmeno in jmena]
print()
print(c3)

# 4. všechna jména převedená na malá písmena s koncovkou '@email.cz'.
c4 = [jmeno.lower() + '@email.cz' for jmeno in jmena]
print()
print(c4)