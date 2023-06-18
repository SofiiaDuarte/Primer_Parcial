"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no 
hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas."""

Edades= int(input("Ingrese la cantidad de edades a calcular: "))
Suma_edades = 0
contador = 0

while contador < Edades:
 Edad = int(input("Ingrese edad: "))
 Suma_edades += Edad
 contador += 1

Promedio = Suma_edades / Edades
Total=Edades
print("El promedio de las edades ingresadas son: ",str(Promedio))
print("El total de las edades ingresadas son: ",(Total))
