print ("Datos de la primera persona")

# Para cargar por teclado una cadena de caracteres utilizamos la funcion input
# Las variables pueden tener muchas funciones aqui tenes una la utilizamos para almacenar el valor introducido por teclado
nombre1=input("Ingrese nombre del producto:")
precio1=int(input("Ingrese un precio:"))
nombre2=input("Ingrese nombre del producto:")
precio2=int(input("Ingrese un precio:"))

# Esta es una constante
BONIFICACION = 20
""" OPERADORES ESTAS COMILLAS SON PARA PONER COMENTARIOS MAS LARGO QUE UNA LINEA """
# PARA COMENTARIOS  UNA LINEA UTILIZAMOS ESTE SIGNO #
# Sumamos los dos precios y su resultado lo guardamos en una variable
precio_compra_total = precio1 + precio2
# Comprobamos siel precio1 es mayor o igual que el precio2
comparar = precio1 >= precio2 # operador de comparacion
logico = (precio1 < precio2 and precio1 == precio2) # operador logico

cabecera="Resultado del producto {0}. y del producto {1}.:"
# Concatenamos las cadenas de texto de varias formas aqui  tenes una con la funcion format
print (cabecera.format(nombre1, nombre2))
print ("EL precio del primer valor es mayor o igual que el precio del segundo valor:")
print (comparar)
# concatenar se puede hacer de esta manera con el sign + y en la variable la propiedad str
print ("la suma total de los dos productos es:" + str(precio_compra_total))
print ("precio1 < precio2 and precio1 == precio2")
print (logico)
""" VEMOS EL OPERADOR DE ASIGNACION AQUI ABAJO """
precio_compra_total += BONIFICACION
print ("La precio total le incrementamos su valor que tiene la constante:" + str(precio_compra_total))
