"""Escribe un programa que calcule el promedio general de una clase."""

Estudiantes= int(input("Ingrese la cantidad de estudiantes: "))
Suma_Notas=0
contador=0

while contador < Estudiantes:
 Notas = float(input("Ingrese Nota del alumno: "))
 Suma_Notas += Notas
 contador +=1

promedio = Suma_Notas / Estudiantes
print("El promedio general de la clase es: ",(promedio))