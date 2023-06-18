""" Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto 
(bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13."""

Horas_Trabajadas=float(input("Ingrese sus horas trabajadas: "))

#Definimos las variables

Bonificacion_18=Horas_Trabajadas * 18
Bonificacion_15=Horas_Trabajadas * 15
Sueldo_Neto_18=1500 + Bonificacion_18
Sueldo_Neto_15=1300 + Bonificacion_15

#Resultado

if Horas_Trabajadas>=120:
    total=Horas_Trabajadas*1500
    print("Sus horas trabajadas son: ",str(Horas_Trabajadas),"Le corresponde el pago de: $1500"," Mas la bonificacion: $",str(Bonificacion_18)," Y su sueldo neto es: $",str(Sueldo_Neto_18))
else:
    print("Sus horas trabajadas son: ", "Le corresponde el pago de: $1300"," Mas la bonificacion: $",str(Bonificacion_15)," Y su sueldo neto es: $",str(Sueldo_Neto_15))