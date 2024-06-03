def impuestos(pago_sin_impuesto,impuesto):
    pago_total= pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)
    return pago_total

pago_sin_impuesto= float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Ingrese el valor de inpuesto: '))

pago_con_impuesto=impuestos(pago_sin_impuesto,impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')




