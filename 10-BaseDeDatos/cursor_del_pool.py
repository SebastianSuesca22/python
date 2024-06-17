from logger_base import *
from conexion1 import *

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    def __exit__ (self, tipo_exepcion, valor_excepcion, detaller_excepcion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion: {valor_excepcion} {tipo_exepcion} {detaller_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__' : 
    with CursorDelPool() as cursor:
        log.debug(f'Dentro del bloque with')
        cursor.execute('SELECT *FROM persona')
        log.debug(cursor.fetchall())
        
