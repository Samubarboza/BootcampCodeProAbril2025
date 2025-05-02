# Crea un programa que gestione las tareas de una persona. Debe usar un diccionario para almacenar las tareas con la siguiente estructura:

# tarea:nombredelatarea.
# estado:estado de la tarea(pendiente,enprogreso,completada).

print('¡Bienvenido a tu agenda de tareas!')
agenda_de_tareas = {}

# Funcion para agregar tarea al programa
def agregar_tarea():
    ingreso_tarea = input('Por favor agrega una nueva tarea: ')
    ingreso_estado = input('Por favor agrega un estado a la tarea: ')
    agenda_de_tareas[ingreso_tarea] = ingreso_estado
    print(f'¡Tarea agregada con exito!\nLas tareas son: {agenda_de_tareas}')
    


# Funcion para modificar el estado de la tarea del programa
def modificar_estado():
    ingreso_modificacion = input('Por favor ingresa el nombre de la tarea que desea modificar: ')
    ingreso_nuevo_estado = input('Por favor ingresa el nuevo estado de la tarea: ')
    if ingreso_modificacion in agenda_de_tareas:
        agenda_de_tareas[ingreso_modificacion] = ingreso_nuevo_estado
    else:
        print('Lo siento, no se encontro esa tarea.')
    print(f'¡Estado de tarea modificado con exito!\n {agenda_de_tareas}')


# Funcion para eliminar tarea
def eliminar_tarea():
    ingreso_para_eliminar = input('Por favor ingresa el nombre de la tarea que desea eliminar: ')
    if ingreso_para_eliminar in agenda_de_tareas:
        del agenda_de_tareas[ingreso_para_eliminar]
    print(f'¡Tarea eliminado con exito!\n {agenda_de_tareas}')


# Funcion para mostrar todas las tareas y su estado
def mostrar_tareas():
    if agenda_de_tareas == {}:
        print('No hay ninguna tarea en tu agenda')
    else:
        print(f'Estas son todas tus tareas\n {agenda_de_tareas}')

# Bucle infinito para el programa
while True:
    opciones_para_el_usuario = input('Por favor ingresa una opcion para continuar con el programa.\n1. Agregar una tarea\n2. Modificar el estado de una tarea\n3. Eliminar una tarea\n4. Mostrar todas las tareas\n5. Salir\n: ')  
    
    if opciones_para_el_usuario == '1':
        agregar_tarea()
    elif opciones_para_el_usuario == '2':
        modificar_estado()
    elif opciones_para_el_usuario == '3':
        eliminar_tarea()
    elif opciones_para_el_usuario == '4':
        mostrar_tareas()
    elif opciones_para_el_usuario == '5':
        print('Gracias por utilizar el programa\n¡Hasta la proxima!')
        break
    else:
        print('Opcion invalida, intentalo nuevamente.')

    
# Juego para adivinar numeros 
numero_secreto = 5
intentos = 3

while intentos > 0:
    try:
        ingreso_usuario = int(input('Ingresa el numero: '))
    except:
        print('No ingresaste un numero\nIngresa un numero valido por favor.')
    if ingreso_usuario == numero_secreto:
        print('¡Felicitaciones! Adivinaste')
        break
    elif ingreso_usuario > numero_secreto:
        print('El numero secreto es menor al numero ingresado.')
    elif ingreso_usuario < numero_secreto:
        print('El numero secreto es mayor al numero ingresado.')
    else:
        print('No ingresaste un numero.')
    
    intentos -= 1
    print(f'Te quedan {intentos} intentos.')
    if intentos == 0:
        print('¡Hasta la proxima!')



'''
Challenge 3: La Clase Animal
Crea una clase llamada Animal que tenga los atributos: ● Nombre
● edad
La clase debe tener un método llamado presentarse() que imprima algo como:

"¡Hola! Soy [nombre] y tengo [edad] años. Luego, crea instancias de un perro y un gato y haz que ambos se presenten.
'''


class Animal():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        return f'Hola, soy {self.nombre} y tengo {self.edad} años'
perro = Animal ('Facundo', '20')
gato = Animal ('Rogelio', '29')
lobo = Animal ('Tanos','250')
print(f'{perro.presentarse()}\n{gato.presentarse()}\n{lobo.presentarse()}')




'''
Challenge 4: Peluche
Crea una clase Peluche con los atributos:
● nombre
● tamaño
La clase debe tener un método abrazar() que imprima algo como: "¡Es hora de
abrazar a [nombre], el peluche de tamaño [tamaño]!" Luego, crea un peluche y haz que sea abrazado. Conceptos usados:
● Clases, Atributos, Métodos.'''

class Peluche():
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
    def abrazar(self):
        return f'Es hora de abrazar a {self.nombre} mi peluche de tamaño {self.tamaño}'
oso = Peluche ('Dinosauro', 'Grande')
print(oso.abrazar())


''' 
Challenge 5: Multiplicar una Lista de Números
Escribe una función llamada multiplicar_lista() que reciba una lista de números como parámetro y devuelva el resultado de multiplicar todos los elementos de la lista.
'''


def multiplicar_lista(lista_de_numeros):
    primer_resultado = lista_de_numeros[0] * lista_de_numeros [0]
    segundo_resultado = lista_de_numeros[1] * lista_de_numeros [1]
    print (f'{primer_resultado}, {segundo_resultado}')

multiplicar_lista([2,4])




'''
Challenge 6: Acumulador de Números
Escribe una función llamada acumulador() que reciba un número n como parámetro y devuelva la suma de todos los números desde 1 hasta n.'''

def acumulador(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
print(acumulador(5))