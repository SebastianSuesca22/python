import psycopg2

conexion = psycopg2.connect (user ='postgres', password ='admin', host = '127.0.0.1', port ='5432', database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            entrada = input('Proprociona el id persona a eliminar: ')
            valores = (tuple(entrada.split(','),))
            cursor.executemany(sentencia,valores)

            #conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros eliminados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()