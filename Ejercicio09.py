"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad. 
de una cantidad de personas ingresada por el usuario."""

Personas= int(input("cantidad de personas que quiere ingresar: "))
while(Personas>=1):
 nombre = input("Ingrese el nombre: ")
 apellido = input("Ingrese el apellido: ")
 edad = input("Ingrese la edad: ")
 print("Nombre: ",(nombre))
 print("Apellido: ",(apellido))
 print("Edad: ",(edad))
 Personas=Personas-1
 print("Su nombre es: ",nombre)
 print("Su apellido es: ",apellido)
 print("Su edad es: ",edad)
else:
 print("Finalizo el programa")