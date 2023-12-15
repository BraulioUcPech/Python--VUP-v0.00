myStr = "Hola Mundo"
# Operador de Contatenacion
print("Este Es Mi Primer Programa Llamado0" + myStr)
print("Este Es Mi Primer Programa Llamado1", myStr)
# Poner "f" en el String y poner la variable dentro del String con esto "{} y adentro el nombre de la variable estamos haciendo que la "f" busca en los "{}" para saber si tiene una varible dentro para que el momento de interpretarlo de imprimirlo lo puestro entre pantalla.
print(f"Este Es Mi Primer Programa Llamado2 {myStr}")
print("Este Es Mi Primer Programa Llamado3 {0}".format(myStr))
# Para saber los "metodos" que hay, la formacion. para poder afectar el String de las Variables.
print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
# Metodos Encadedados. una forma de definir metodos entro otros. "la Variable con un metodo y puedes agregar otro metodos."
print(myStr.replace('Hola', 'Adios').upper())
#cuantas letras "tiene mi valor"
print(myStr.count('o'))
#inica con "tal caracter True o false"
print(myStr.startswith('Ho'))
#termina con "tal caracter True o false"
print(myStr.endswith('ndo'))
#quiero separar "por tal cosa o caracter"
print(myStr.split('H'))
#Cual es el indice, posicion."del tal cosa o caracter"
print(myStr.find('d'))
#saber la longitud de los caracter "comienza desde 1"
print(len(myStr))
#
print(myStr.index('a'))
#
print(myStr.isnumeric())
print(myStr.isalpha())
#el indice o posicion del caracter
print(myStr[3])
print(myStr[-5])



