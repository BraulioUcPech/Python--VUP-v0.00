print("El Inicio")

# Variables
cursor = 'Este es un valor de la Variable, -el nombre de la variable-'
print (cursor)

# Contantes
ESTO_ES_UNA_CONTANTE = 'El valor de una Contante, siempre es en Mayuscula. Dicho por la Comunidad de Python'
print (ESTO_ES_UNA_CONTANTE)

# Tipos
#Strings
titulo_de_algo = 'Bienvenido/a'
print (titulo_de_algo)

nombre_completo = "Braulio Uc Pech"
print(nombre_completo)

abertencia = """Este es un articulo peligroso,
                no abrir,
                no leer,
                no comprimir.
                es peligroso!"""
print(abertencia)

#Int
un_numero = 10
print(un_numero)

numero_operadores = 10 + 10, 10 - 10, 10 * 10, 10 / 10, 10 // 10 # es lo mismo, en una sola variable
print(numero_operadores)

numero_operadores = 10 - 10
print(numero_operadores)
numero_operadores = 10 * 10
print(numero_operadores)
numero_operadores = 10 / 10
print(numero_operadores)
numero_operadores = 10 // 10 # Para mostrar en la divicion, si te sale en decimal es resultado, colocando // se imprime el valor en entero.
print(numero_operadores)

#Float
#los flotantes hacen lo mismo que los enteros, pueden usar los operadores
un_decimal = 20.1416
print(un_decimal)

un_decimal = -20.1343
print(un_decimal)

#Bool
valor = True
print(valor)

valor1 = False
print(valor1)

#Tipado Dinamico
#Manejar diferentes tipos de datos en diferentes tipos de tiempos.
valor = "Jose"
print(valor)
valor = 10
print(valor)
valor = 18.10
print(valor)
valor = True
print(valor)
valor = "Valor!"
print(valor)

#Relaciones
#Comparar tipos de datos de un "int" o "float"
numero_uno = 10
numero_dos = 20
#Operador relacional
"""
    >
    <
    >=
    <=
    ==
    !=
"""

resultado = numero_uno > numero_dos
print(resultado)

#Logicos
# and, or y not
resultado_final = True and True and True
print(resultado_final)

resultado_final = True and True and 10 > 20
print(resultado_final)

resultado_final = True or True or 10 < 20
print(resultado_final)

resultado_final = True and (False or 10 > 20)
print(resultado_final)

negar_el_valor = not True
print(negar_el_valor)
negar_el_valor = not False
print(negar_el_valor)

#Tipado
valorTip = "jose"
print(type(valorTip))

valorTip = 17
print(type(valorTip))

valorTip = 18.15
print(type(valorTip))

valorTip = True
tipo = (type(valorTip))
print(tipo)

#Entradas
nombre_completo = input("Teclee Sus Nombres:")

edad = int(input("Teclee su edad:"))

altura = input("Teclee su altura:")
altura = float(altura)

confirmacion = input("¿Acepta todo esto?: (si/no)") == "si"

autorizacion = input("¿Aprueda estos datos?: (si/no)")
autorizacion = autorizacion == "si"

print(f"Tu Nombre:{nombre_completo} Tu Edad:{edad} Tu Altura:{altura} Tu Confirmacion:{confirmacion} Tu Autorizacion:{autorizacion}")

#Multiples
nombre, apellido, titulo = "braulio", "uc pech", "Doc."
print(nombre)
print(apellido)
print(titulo)

#Listas
lista = ["String", 10, 29.20, True]  #list()
print(lista)

lista_string = ["Eduardo", "Rodrigo", "Mario"]
lista_enteros = [10, 20, 30, 500]
lista_flotantes = [10.20, 30.21, 70, 17]
lista_booleanos = [True, False, (2<10), (4>3 and 10 != 11)]
