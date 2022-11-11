rus_sogl = ('БВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
rus_gl = ('АЕЁИОУЫЭЮЯ')
ang_sogl = ('BCDFGHJKLMNPQRSTVWXZ')
ang_gl = ('AEIOUY')
while True:
    a = input('Exit введите слова: ')
    cont = 0
    cont1 = 0

    for i in a.upper():
        if i in rus_sogl:
            cont +=1
    for i in a.upper():
        if i in rus_gl:
            cont1 +=1
    for i in a.upper():
        if i in ang_gl:
            cont1 +=1
    for i in a.upper():
        if i in ang_sogl:
            cont +=1
    if a.upper() == 'EXIT' or a.upper() == 'УЧШЕ':
        break
    cont2 = (100/(cont + cont1))* cont
    cont3 = (100/(cont + cont1))* cont1
    l = len(a)
    print(f'слово: {a}')
    print(f'Количество букв: {l}')
    print(f'Согласных букв: {cont}')
    print(f'Гласных букв: {cont1}')
    print(f'Гласные/Согласные: {cont3}%/{cont2}%')





