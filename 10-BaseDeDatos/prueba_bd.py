import psycopg2

conexion = psycopg2.connect(user='postgres', password = 'admin', host = '127.0.0.1', port ='5432', database = 'test_db')

#forma larga
# cursor = conexion.cursor()
# sentencia = 'SELECT * FROM persona'
# cursor.execute(sentencia)
# registros = cursor.fetchall()

# print(registros)

# cursor.close()
# conexion.close()
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = 1'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
  