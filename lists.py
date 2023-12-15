#una lista puede almacenar todos los Tipo De Datos "un int, un float, un bool o que tenga otra lista dentro."
emo_list = [1 , "string", 1.19, True, [1, "otro string", 1.20, False]]
colors = ['red', 'blue', 'yellow' , 'yellow']

# Tupla usarlo para que los numeros no sean string si no enteros o flotantes. "tupla dentro de la list con una variable"
numero_lista = list((1, 2, 3, 4, 5))
print(numero_lista)

# Renge saber el rango obtener el rango. haciendo una variable y la list con el Renge y dentro del Renge los numeros.
R = list(range(1, 11))
print(R)

#Saber el tipo de dato que es de una variable's.
#Usando el "dir" para saber imformacion de un tipo de dato. ¿que es lo que puedo hacer con este tipo de dato para la variable?
print(dir(colors))
print(len(colors))#saber la longitud de los variables "cuantas valores tiene mis variables"
print(colors[2])# saber si esta el valor en mis variables.
print("blue" in colors)# saber si esta un valor dentro de mis variables en mi lista "en este caso da si = True"
print('green' in colors)# saber si esta un valor dentro de mis variables en mi lista "en este caso no = False"

#A qui lo que hacer es cambiar un valor por otro
print(colors)
colors[1] = 'green'
print(colors)

#el ".append" es para agregar un valor a mi lista "list" a mis variables.
#colors.append('violet')
#no puede poner mas valores a una variable, lo que tiene que hacer es agregar una Tupla que hace que se convierta en un valor, en un solo elemento.
#colors.append(('violet', 'marrom')) #pero al momento de de imprimirlo en pantalla es una lista dentro de un Tupla, ose aque es una tupla no un valor dentro de la misma variable. hay que hacer que estos dos valores que queremos agregar se convierta un solo elemento de la variable. ¿como lo hacermos?

colors.extend(['violet', 'marrom']) #Es .extend es para agregar de forma de lista lo agrega de un solo elemento, hace que los valores se unan con los otros valores que hay en la variable, ya no es una tupla o lista "extiendemo estos valores a esta variable para agregar mas valores."
colors.extend(['pink', 'black'])

# El .insert es para agregar mas elemento a la lista pero con posicion de la longitud de la variable, ya sea adente o tras o en medio.
colors.insert(9 , 'oro1')
colors.insert(1, 'plata2')
colors.insert(len(colors), 'diamont3')
# El .pop es para elminar un elemento uno por uno, "el ultimo" cuanto mas pongas la "variable.pop()" se eliminara el ultimo.
colors.pop(1)
colors.pop()
# El .remove es para remover un valor de las variables.
colors.remove('green')
#colors.clear()#Limpia todo lo que esta en la lista.
# El .sort es para hacer que los valores de las variables se ordenen de forma alfabetica y numerica. si agregamos un "reverse = True" hace que el ordenen alfabetico retroseda.
colors.sort(reverse = True)
print(colors)
print(colors.index('yellow'))# Saber el indece de de los valores de las variables
print(colors.count('yellow'))# Saber cuantos veces de repite la el valor o el dato o elemento que hay en las variables

