# Lekce 3, úkol 8: Čtení kódu

# Popište vlastními slovy co následující výrazy udělají se zadaným seznamem 
# seznam. Až když máte ve svojí hlavjénce jasno, tak je zkuste napsat 
# do Python konzole a ověřte, zda jste měli pravdu.

seznam = [1, 4, 9, 16, 25, 36, 49, 64]

#print([x**0.5 for x in seznam])  # odmocní, tj. [1, 2, 3, 4, 5, 6, 7, 8]

#print([x % 2 for x in seznam])  # zbytek po dělení 2, tj. [1, 0, 1, 0, 1, 0, 1, 0]

#print([[x // 2, x % 2] for x in seznam])   # dvojičky: vyděleno 2 a zbytek, tj. [[0, 1], [2, 0]..]

#print(seznam = ['12.03.2014', '10.01.2015', '06.06.1986']) # hodí chybu

#print([int(datum[3:5]) for datum in seznam])   # chyba

#print([int(datum[:2])-1 for datum in seznam])  # chyba a všude níž taky chyba

#print([[int(datum[:2]), int(datum[3:5]), int(datum[6:])] for datum in seznam])
#print([datum.split('.') for datum in seznam])
# print(['/'.join(datum.split('.')) for datum in seznam])

