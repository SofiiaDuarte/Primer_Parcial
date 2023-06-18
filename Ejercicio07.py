"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de horas. 
escribe un programa que calcule el descuento anual a realizarse, considerando: 
A. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
B. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
C. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1. d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual a descontarse y las horas trabajadas en todo el año."""

Horas_trabajadas=float(input(" Ingrese horas trabajadas: "))

# Definimos las variables

Horas= Horas_trabajadas * 12
Sueldo_Anual1= Horas_trabajadas * 1500
Sueldo_Anual2= Horas_trabajadas * 1300
Sueldo_Anual3= Horas_trabajadas * 1100

Bonificacion1= Sueldo_Anual1 * 0.18
Bonificacion2= Sueldo_Anual2 * 0.15
Bonificacion3= Sueldo_Anual3 * 0.13

Sueldoneto1= Sueldo_Anual1 + Bonificacion1
Sueldoneto2= Sueldo_Anual2 + Bonificacion2
Sueldoneto3= Sueldo_Anual3 + Bonificacion3 

Descuento1= Sueldo_Anual1 - 0.03
Descuento2= Sueldo_Anual2 - 0.05
Descuento3= Sueldo_Anual3 - 0.01

# Resultados

if Sueldo_Anual1 > 2000000:
    print("El sueldo anual bruto del empleado es: $", str(Sueldo_Anual1)+" La bonificacion: $", str(Bonificacion1), " Descuento anual: ", str(Descuento1), " Horas anuales trabajadas: ",str(Horas))
elif Sueldo_Anual2 >= 1000000 and Sueldo_Anual2 <= 2000000:
    print("El sueldo anual bruto del empleado es: $", str(Sueldo_Anual2) + " La bonificacion: $", str(Bonificacion2), " Descuento anual: $", str(Descuento2), " Horas anuales trabajas: ",str(Horas))
elif Sueldo_Anual3 < 1000000 and Sueldo_Anual3 >0:
    print("El sueldo anual bruto del empleado es: $", str(Sueldo_Anual3)+ " La bonificacion: $", str(Bonificacion3), " Descuento anual: $", str(Descuento3), " Horas anuales trabajadas: ",str(Horas))