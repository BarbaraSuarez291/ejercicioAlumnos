#Pensar una manera mas eficiente de obtener alumnos en base a la matricula
# La matricula se debe poder ingresar por un input del programa pista: input()
# El usuario debe ingresar un numero de matricula, y una funciona tiene que responder
# con los datos de ese alumno
# Limitacion: No se puede usar for.
# Tiene que ser una funcion


#### Diccionario de diccionarios.
# La matricula(va a la key de cada diccionario). Esta se va completando de forma automatica cuando
# se ingresa un alumno nuevo al sistema.

#dic   key(matricula)                      value(datos de alumno)
#                     key :  value  ,     key  :    value   ,    key:  value
alumnos = { 1 :  { "nombre": "Lucas", "apellido": "Rodriguez", "edad": '23'}}
##cont=2



## Funcion para mostrar alumno segun su matricula
## Verifica que exista un alumno con la matricula que se busca
def mostrarAlumno(matricula, alumnos):
    if(alumnos.get(matricula)!= None):
        nom= alumnos[matricula].get('nombre', 'No hay registro')
        apell= alumnos[matricula].get('apellido', 'No hay registro')
        ed= alumnos[matricula].get('edad', 'No hay registro')
        print('---------------------------')
        print('Nº de matricula: ', matricula)
        print('Nombre: ',nom)
        print('Apellido: ',apell)
        print('Edad: ',ed)
        print('---------------------------')
    else:
        print('')
        print('La matricula ingresada no existe.')
        print('')
## Funcion para ingresar un alumno nuevo
def ingresarAlumnoNuevo():
    matricula = int(input('Nº de matricula: '))
    nombre = input('Nombre:')
    apellido = input('Apellido:')
    edad = input('Edad:')
    alumnos[matricula]= {"nombre": nombre, "apellido": apellido, "edad": edad}
    mostrarAlumno(matricula, alumnos)

##Con el while el usuario puede elegit opciones y asi, decidir cuando finalizar el programa.
i=0
while(i==0):

    print("  Seleccione la opcion deseada:")
    print(" -1 para ingresar un nuevo alumno")
    print(" -2 para buscar a un alumno alumno")
    print(" -3 para finalizar el programa")
    opcionElegida=input()

    if(opcionElegida=='1'):   ## Ingreso de alumno nuevo
        ingresarAlumnoNuevo()
        #print(alumnos)
        #cont+=1

    elif(opcionElegida=='2'): ## Busca alumno
        #print(alumnos)
        matricula=input('Ingrese el numero de matricula: ')
        mostrarAlumno(int(matricula), alumnos)

    elif(opcionElegida=='3'):## Finaliza el programa
        print('')
        print("Programa Finalizado.")
        print('')
        i+=1

    else:                   ## En caso de error
        print('')
        print("Error! Vuelva a intentarlo.")
        print('')