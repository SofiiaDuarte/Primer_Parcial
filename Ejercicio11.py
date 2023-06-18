"""Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
A. Si es número es par o impar.
B. Cuanto es la suma total de todos los números mostrados.
C. Cuanto es la suma total de todos los números pares mostrados.
D. Cuanto es la suma total de todos los números impares mostrados."""

#Numeros del 1 al 10

Numero1=1
Numero2=2
Numero3=3
Numero4=4
Numero5=5
Numero6=6
Numero7=7
Numero8=8
Numero9=9
Numero10=10

Numero=1
while Numero <=10:
    print(Numero)
    Numero= Numero+1
    
Numero=int(input("\n""Ingrese un numero: "))
if  Numero % 2==0:
 print("El numero ingresado: "+ str(Numero)+" es par")
else: 
 print("El numero ingresado es: "+str(Numero)+ " es impar")

#Suma de pares e impares

Suma_Numero_par= Numero2 + Numero4 + Numero6 + Numero8 + Numero10
Suma_Numero_impar= Numero1 + Numero3 + Numero5 + Numero7 + Numero9

#Suma total de numeros

Suma_Total= Suma_Numero_par + Suma_Numero_impar

#Numeros pares e impares

print(str(Numero1)+" Es un numero impar")
print(str(Numero2)+" Es un numero par")
print(str(Numero3)+" Es un numero impar")
print(str(Numero4)+" Es un numero par")
print(str(Numero5)+" Es un numero impar")
print(str(Numero6)+" Es un numero par")
print(str(Numero7)+" Es un numero impar")
print(str(Numero8)+" Es un numero par")
print(str(Numero9)+" Es un numero impar")
print(str(Numero10)+" Es un numero par")

#Resultados

print("El resultado de los numero pares son: "+ str(Suma_Numero_par))
print("El resutado de los numeros impares son: "+str(Suma_Numero_impar))