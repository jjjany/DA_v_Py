# Lekce 2, úkol 6: Průměr

# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
# Sestavte v Python konzoli výraz (vzoreček), který spočítá průměrnou hodnotu 
# v takovém seznamu. Otestujte jej na seznamech různých délek.

s1 = [1, 5, 7]
s2 = [2, 8.9, 6, 3, 2.1]
s3 = [2, 8.9, 6, 3, 2.1, 3.3]
s4 = [7, 8, 1, 6]

prumer1 = sum(s1)/len(s1)
prumer2 = sum(s2)/len(s2)
prumer3 = sum(s3)/len(s3)
prumer4 = sum(s4)/len(s4)

print(prumer1)
print(prumer2)
print(prumer3)
print(prumer4)
