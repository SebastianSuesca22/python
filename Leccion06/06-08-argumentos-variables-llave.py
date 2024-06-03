def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE= 'Integrated Development Environment', OOP= 'Object Oriented Programming',DBMS= 'Database Management System')
