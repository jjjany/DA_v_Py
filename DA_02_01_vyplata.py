# Lekce 2, úkol 1: Výplata

# 1. Spočítejte svůj měsíční příjem víte-li, že pracujete 7 hodin denně 
# se mzdou 450 Kč na hodinu. Řekněme, že měsíc má 21 pracovních dní.
7 * 450 * 21

# 2. Uložte si počet pracovních hodin za den do proměnné hodin, 
# hodinovou mzdu do proměnné mzda a počet pracovních dní do proměnné dni. 
# Spočítejte svou výplatu s použitím těchto proměnných.
hodin = 7
mzda = 450
dni = 21
vyplata = hodin * mzda * dni
print(vyplata)

# 3. Pokud pracujete na živnostenský list, můžete si odečíst 60 % příjmů jako paušál 
# a ze zbytku zaplatíte 15% daň. Uložte si tyto hodnoty do proměnných paušál 
# a dan a spočítejte svůj příjem po zdanění.
pausal = vyplata * 0.6
dan = vyplata * 0.4 * 0.15
zdaneny_prijem = pausal + (vyplata * 0.4) - dan
print(zdaneny_prijem)
