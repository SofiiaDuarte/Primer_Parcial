"""Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales.indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6)."""

# Calculamos el promedio de las notas

Nota1=float(input("Ingrese su primer Nota: "))
Nota2=float(input("Ingrese su segundo Nota: "))
Nota3=float(input("Ingrese su tercer Nota: "))
Promedio= (Nota1 + Nota2 + Nota3) /3
if (Promedio>=6):
 print("Su promedio es: ",Promedio," Usted aprobó la materia")
else:
 print("Su promedio es: ",Promedio,"Usted no aprobo, debe recursar la materia")