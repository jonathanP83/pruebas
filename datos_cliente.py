import os
os.system('cls' if os.name == 'nt' else 'clear')# Limpiar la consola
'''
print ("===========================================================")
print ("|\t\t\t\t\t\t\t  |\n|\t\t    bievenido cliente\t\t\t  |\n| \ta continuación le solicitaremos algunos datos  \t  |")
print ("|\t\t\t\t\t\t\t  |\n===========================================================")
nombre_cliente = input("Ingreses su nombre?\n")
apellido_cliente = input("Ingrese su apellido?\n")
edad_cliente = int(input("Edad?\n"))
correo_electronico_cliente = input("Correo electronico?\n")
print ("====================================================================")
print ("|\t\t Muchas gracias por su información\t\t   |\n|\t      a continuación le mostraremos sus datos\t\t   |")
print ("====================================================================\n")
print ("Nombre:\t\t   " , nombre_cliente) 
print ("Apellido:\t   ", apellido_cliente) 
print ("Edad:\t\t   ", edad_cliente) 
print ("Correo electrónico:" , correo_electronico_cliente,"\n") 
print ("====================================================================")
'''

print ("\n=====================================================\n|\t\t\t\t\t\t    |\n|\t\tBievenido cliente\t\t    |\n|   a continuación le solicitaremos algunos datos   |\n|\t\t\t\t\t\t    |\n=====================================================\n")

#1_declaro variable
#2_solicito ingreso de datos al usuario
#3_Compruebo si el dato ingresado no esta vacio
#4_Si el dato ingresado esta vacio vuelvo a solicitar el ingreso de datos al usuario
#5_En caso de que el dato ingresado siga vacio se imprime un mensaje de error y se cierra el programa
#6_En caso de que el dato ingresado no este vacio continua el programa

nombre_cliente = input("Ingrese su Nombre?\n").strip()

if nombre_cliente == "":
    print ("ERROR - Nombre no puede estar vacío - Intente de Nuevo")
    input("Ingrese su Nombre?\n").strip()
    if nombre_cliente == "": 
        print ("ERROR - Programa Finalizado - Nombre no puede estar vacío")
        exit()


apellido_cliente = input("Ingrese su Apellido?\n").strip() 

if apellido_cliente == "":
    print ("ERROR - Apellido no puede estar vacío - Intente de Nuevo")
    input("Ingrese su Apellido?\n").strip()
    if apellido_cliente == "":
        print ("ERROR - Programa Finalizado - Apellido no puede estar vacío")
        exit()

edad_cliente = int(input("Edad? [solo valor numerico]\n".strip())) 

#compruebo si la edad es menor a 18 de ser asi no se permite el ingreso de datos

if edad_cliente < 18:
    print ("ERROR - Debe Tener Minimo 18 - Intente de Nuevo") 
    edad_cliente = int(input("Edad? [solo valor numerico]\n".strip())) 
    if edad_cliente < 18:
        print ("ERROR - Programa Finalizado - Debe Tener Minimo 18") 
        exit()

correo_electronico_cliente = input("Cual es su correo electronico?\n").strip()
if correo_electronico_cliente == "" :
    print ("ERROR - El correo electronico no puede estar vacío - Intente de Nuevo")
    input("Cual es su correo electronico?\n").strip()
    if correo_electronico_cliente == "" :
        print ("ERROR - Programa Finalizado - El correo electronico no puede estar vacío")
        exit()

print ("=================================================================\n|\t\tMuchas gracias por su información\t\t|\n|\t     a continuación le mostraremos sus datos\t\t|\n""=================================================================\n","Nombre:\t     ", nombre_cliente, "\n Apellido:\t     ", apellido_cliente, "\n Edad:\t\t     ",   edad_cliente, "\n Correo electrónico: ", correo_electronico_cliente ,"\n=================================================================\n")


''' 


print("\n=====================================================\n|\t\t\t\t\t\t    |\n|\t\tBienvenido cliente\t\t    |\n|   A continuación le solicitaremos algunos datos   |\n|\t\t\t\t\t\t    |\n=====================================================\n")

# Validar nombre
while True:
    nombre_cliente = input("Ingrese su Nombre?\n")
    if nombre_cliente.strip() == "":
        print("ERROR - nombre no puede estar vacío")
    else:
        break

# Validar apellido
while True:
    apellido_cliente = input("Ingrese su Apellido?\n")
    if apellido_cliente.strip() == "":
        print("ERROR - apellido no puede estar vacío")
    else:
        break

# Validar edad
while True:
    try:
        edad_cliente = int(input("Edad? [solo valor numerico]\n"))
        if edad_cliente < 18:
            print("ERROR - debe ser mayor o igual a 18")
        else:
            break
    except ValueError:
        print("ERROR - Por favor ingrese un número válido.")

# Validar correo electrónico
while True:
    correo_electronico_cliente = input("Cual es su correo electrónico?\n")
    if "@" not in correo_electronico_cliente:
        print("ERROR - El correo electrónico debe contener '@'")
    else:
        break

# Mostrar datos ingresados
print("\n=================================================================")
print("|\t\tMuchas gracias por su información\t\t|")
print("|\t     A continuación le mostraremos sus datos\t\t|")
print("=================================================================")
print(f"Nombre:\t\t     {nombre_cliente}")
print(f"Apellido:\t     {apellido_cliente}")
print(f"Edad:\t\t     {edad_cliente}")
print(f"Correo electrónico: {correo_electronico_cliente}")
print("=================================================================")

'''