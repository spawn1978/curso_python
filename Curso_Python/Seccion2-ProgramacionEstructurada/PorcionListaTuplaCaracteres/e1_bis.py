def meses_faltantes(numero):
    # meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    meses=('1','2','3','4','5','6','7','8','9','10','11','12')
    return meses[numero:]


# bloque principal
#Se recupera desde el mes indicado hasta el final de la lista
print("Imprimir los nombres de meses que faltan hasta fin de año")
numero=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numero)
print(mesesfalta)
