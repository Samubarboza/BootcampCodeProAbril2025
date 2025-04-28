'''
Evaluar desempeño académico
Descripción:
Crea una función llamada evaluar_estudiante que reciba los siguientes parámetros:

nombre (Nombre del estudiante)
nota1, nota2, nota3 (Notas del estudiante)
La función debe:

Calcular el promedio de las notas.
Devolver un mensaje como:
"Felicitaciones <nombre>, aprobaste con un promedio de <promedio>!" si el promedio es mayor o igual a 6.
"Lo siento <nombre>, reprobaste con un promedio de <promedio>." si es menor a 6.

'''
def evaluar_estudiante(nombre, nota1, nota2, nota3):
    promedio_estudiante = nota1 + nota2 + nota3
    if promedio_estudiante >= 6:
        print(f'Felicitaciones {nombre}, pasaste con un promedio de {promedio_estudiante}!')
    else:
        print(f'Lo siento {nombre}, reprobaste con un promedio de {promedio_estudiante}')
evaluar_estudiante('Samuel',2,3,4)



# Hacé una función que reciba 3 números como parámetros y devuelva la suma.

def suma(numero1, numero2, numero3):
    resultado = numero1 + numero2 +numero3
    return resultado
print(1,2,3)

# Función que reciba dos notas y retorne el promedio.
def pasa_o_no_estudiante():
    nombre = input('Hola, ingresa tu nombre por favor: ')
    matematica = int(input('Ingresa tu nota en matematica: '))
    ingles = int(input('Ingresa tu nota en ingles: '))
    fisica = int(input('Ingresa tu nota en fisica: '))
    promedio_del_estudiante = (matematica + ingles + fisica) / 3
    promedio = 6
    if promedio_del_estudiante >= promedio:
        print(f'Felicitaciones {nombre}, aprobaste con un promedio de {promedio_del_estudiante}!')
    else:
        print(f'Lo siento {nombre}, reprobaste con un promedio de {promedio_del_estudiante}')
pasa_o_no_estudiante()

'''Calcular el área de un rectángulo
Función que reciba base y altura, y retorne el área'''

def area_del_rectangulo():
    base = float(input('Por favor ingresa el base del rectangulo: '))
    altura = float(input('Ahora ingresa la altura del rectangulo: '))
    area = base * altura
    print(f'El area del rectangulo es: {area}')
    return area
area_del_rectangulo()

variable = area_del_rectangulo() / 2
print(variable)

# Convertir Celsius a Fahrenheit
def convertir():
    temperatura = float(input('Por favor ingresa la temperatura: '))
    f = (temperatura * 9/8) + 32
    print(f'La temperatura de celcius a Fahrenheit es de: {f}')
convertir()

''' Mostrar nombre completo
Función que reciba nombre y apellido y retorne una sola cadena con el nombre completo.'''
def nombre_completo():
    primer_nombre = input('Por favor ingresa tu nombre: ')
    segundo_nombre = input('Por favor ingresa tu segundo nombre: ')
    apellido = input('Aca podes ingresar tus dos apellidos: ')
    print(f'Tu nombre completo es {primer_nombre} {segundo_nombre} {apellido}. Mucho gusto.')
nombre_completo()

# Crea una función nombre_mas_largo que reciba una lista de nombres y devuelva el nombre que tenga más letras.
def nombre_mas_largo():
    nombre_1 = input('Por favor ingresa un nombre: ')
    nombre_2 = input('Por favor ingresa otro nombre: ')
    nombre_3 = input('Por favor ingresa un nombre mas: ')
    lista = nombre_1, nombre_2, nombre_3
    nombre_con_mas_letra = max(lista, key=len)
    print([nombre_con_mas_letra])
nombre_mas_largo()

''' Crea un programa que pida al usuario que ingrese un número para elegir una opción del menú. Según el número que el usuario escriba, el programa debe:

Si elige 1, mostrar: "Elegiste Hamburguesa",
Si elige 2, mostrar: "Elegiste Pizza",
Si elige 3, mostrar: "Elegiste Ensalada",
Si escribe cualquier otro número, mostrar: "Opción no válida". '''

print('Bienvenido al lugar de las mejores comidas del mundo.\nA continuacion elige una de las opciones del menu.')
print('- Opcion 1 = Hamburguesa.\n- Opcion 2 = Pizza. \n- Opcion 3 = Ensalada.')
comida = int(input(' '))
if comida == 1:
    print('Elegiste hamburguesa.')
elif comida == 2:
    print('Elegiste Pizza')
elif comida == 3:
    print('Elegiste ensalada.')
else:
    print('Opcion no valida.')
    
    
#  Eliminar elemento de una lista
# Crea una función llamada eliminar_elemento que reciba una lista de números y un número específico para eliminarlo de la lista.
def eliminar_elemento(n1,n2,n3,n4):
    lista_de_numeros = [n1, n2, n3, n4]
    lista_de_numeros.remove(n2)
    print(lista_de_numeros)
eliminar_elemento(1,2,3,4)

'''
🔁 Imprimir números hasta N con while
Descripción:
Escribe un programa que pida al usuario un número y luego imprima los números del 1 hasta ese número (inclusive) utilizando un bucle while.
'''

def pedir_numero():
    numero = int(input('Ingresa un numero: '))
    numero_ = 1
    while numero_ <= numero:
        print(numero_)
        numero_ += 1
pedir_numero()

# Escribe un programa que reciba una lista de números y utilice un bucle for para mostrar solo los números que sean mayores a 10.

primer_numero_que_ingresa_el_usuario = int(input('Ingresa un numero: '))
segundo_numero_que_ingresa_el_usuario_ = int(input('Ingresa un numero: '))
tercer_numero_que_ingresa_el_usuario = int(input('Ingresa un numero: '))
lista_de_numero = [primer_numero_que_ingresa_el_usuario, segundo_numero_que_ingresa_el_usuario_, tercer_numero_que_ingresa_el_usuario]
for i in lista_de_numero:
    if i > 10:
        print(i)
    else:
        print('El numero es menor.')

    
