import os
os.system('cls' if os.name == 'nt' else 'clear')# Limpiar la consola

print ("\n"+"="*53+"\n|\t\t\t\t\t\t    |\n|\t\tBievenido cliente\t\t    |\n|   a continuación le solicitaremos algunos datos   |\n|\t\t\t\t\t\t    |\n"+"="*53+"\n")

#declaro variables

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: [solo caracteres numericos] "))
correo_electronico = input("Ingrese su correo electronico: ")

#compruebo si el dato ingresado no esta vacio
#si el dato ingresado esta vacio print error

if nombre == "" or apellido == "" or correo_electronico == "" or edad <= 18:
    print("ERROR")
else :
    print ("\n"+"="*49+"\n|\tMuchas gracias por su información\t|\n|     a continuación le mostraremos sus datos\t|\n"+"="*49+"\n","Nombre:\t     ", nombre, "\n Apellido:\t     ", apellido, "\n Edad:\t\t     ",   edad, "\n Correo electrónico: ", correo_electronico ,"\n"+"="*49+"\n") 
