# Lekce 2, úkol 2: Seznamy

# Mějme seznam pohybů na nějakém bankovním účtu:
pohyby = [1200, -250, -800, 540, 721, -613, -222]

# 1. Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])

# 2. Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])

# 3. Vypište kolik je všech pohybů dohromady
print(len(pohyby))

# 4. Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(max(pohyby))
print(min(pohyby))

# 5. Spočítejte celkový přírůstek na účtu za dané období. 
#    Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))
