"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre por pantalla el resultado, considerando lo siguiente:
A. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
B. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
C. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100."""


Horas_trabajadas= float(input("Ingrese la cantidad de horas que trabajo al mes: "))

#Definimos las variables

Sueldo_N1= Horas_trabajadas *1500 
Sueldo_N2= Horas_trabajadas *1300
Sueldo_N3= Horas_trabajadas *1100

#Resultado

if Horas_trabajadas >120:
    print("El sueldo del empleado es: $", str(Sueldo_N1))
elif Horas_trabajadas >= 80 and Horas_trabajadas <= 120:
    print("El sueldo del empleado es: $", str(Sueldo_N2))
elif Horas_trabajadas < 80 and Horas_trabajadas >0:
    print("El sueldo del empleado es: $", str(Sueldo_N3))