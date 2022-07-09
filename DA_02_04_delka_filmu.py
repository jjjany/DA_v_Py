# Lekce 2, úkol 4: Délka filmu

# V programu kin se často uvádí délka filmu v minutách. Například rozšířená verze 
# filmu Pán prstenů: Dvě věže trvá 223 minut. My bychom ovšem délku filmu raději 
# věděli v hodinách a minutách. Použijte operátory celočíselného dělení 
# a dělení se zbytkem, abyste spočetli, kolik hodin a minut trvá film 
# Pán prstenů: Dvě věže.
delka_min = 223
delka_hod = delka_min // 60
zbytek_min = delka_min % 60

print(f"Film Dvě věže trvá {delka_hod} hodin a {zbytek_min} minut.")