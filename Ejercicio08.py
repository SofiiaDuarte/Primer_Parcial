"""Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas."""

#Datos ingresados por el usuario

Contador= 1

while Contador <=6:
 Nombre=input("Ingrese su nombre: ")
 Apellido=input("Ingrese su apellido: ")
 Edad=int(input("Ingrese su edad: "))
 print(Nombre , " " , Apellido , " " , str(Edad))
 Contador +=1