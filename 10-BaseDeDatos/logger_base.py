import logging as log

log.basicConfig(level=log.DEBUG, format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', datefmt='%I:%M:%S %p', handlers = [log.FileHandler('Capa_datos.log'),log.StreamHandler()])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensjae a nivel de error')
    log.critical('Mensaje a nivel de critical') 