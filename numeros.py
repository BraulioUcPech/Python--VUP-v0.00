
# el residuo de una divicion utiliza el Operador de Modulo "%"
# Poner parectesis hace que la operacion de ejecute primero.
print(3 % 2)
print(8** 2)
print(5 - 3 / 5 * 3**2)
print((5 - 3) / 5 * 3**2)# el que tenga el parectesis se va a ejecutar
print(5 - 3 / (5 * 3**2))#lo mismo pasa aqui.
print((5 - 3) / (5 * 3**2))#se resuelve los que tienen parectesis y luego se divide.

print(type(5))
print(type(342.324))

#el "input" es para escribri en pantalla ya se un numero entero o flotante hasta un string.
#puedes hacer que cambio un string a entero o arrevez con cual quierer tipo de dato y tambien puede ser contatenado.
edad = input("Insete su edad: ")
#print(edad)
#print(type(int (edad)))
edad_nueva = int(edad) + 5
print("Listo tu edad es: {0}".format(edad_nueva))
