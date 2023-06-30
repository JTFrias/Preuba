import numpy as np
import random
kkk=True
menu=True
mylist=[1000,2000,3000,4000,5000]
dineros=np.random.choice(mylist)
r=[]
nombres=[]
apellidos=[]
carreras=[]
asignaturas=[]
promedios=[]
cosa=[]
fechadenacimiento=[]
print(f"porfavor ingrese su nombre")
nombre=input()
nombres.append(nombre)
print(f"porfavor ingrese su apellido")
apellido=input()
apellidos.append(apellido)
print(f"porfavor ingrese su rut")
rut=input()
if len(rut) > 10:
    print("invalido")
elif len(rut) == 10:
    cosa.append(rut)
elif len(rut) < 10:
    print("no")
print(f"ingrese su fecha de nacimiento asi xx/xx/xxxx ")
fechadenaci=input()
fechadenacimiento.append(fechadenaci)
print(f"porfavor ingrese su carrera")
carrera=input()
carreras.append(carrera)
print(f"porfavor ingrese cantidad de asignaturas")
cantiasi=int(input())
for i in range(1,cantiasi+1):
   print("ingrese asignatura numero ",i)
   asi=input()
   asignaturas.append(asi)  
   print("ahora ingrese su promedio")
   promedio=float(input())
   if promedio < 1.0 and promedio > 8.0:
      print("invaldio prueba otro dia")
   elif promedio > 1.0 and promedio < 8.0:
      promedios.append(promedio)
if menu:
 print("1)ingresar rut para buscar")
 print("2)ingrese su rut para generar su pago")
 print("3)salir")
uno=int(input())
print("ingrese su rut")
ingrut=input()
if ingrut == cosa[1]:
 if uno < 1 and uno > 3:
   if uno==1:
     print(f"nombre {nombres(1)}")
     print(f"apellido {apellidos(1)}")
     print(f"rut {cosa(1)} ")
     print(f"fecha de nacimiento{fechadenacimiento(1)}")
     print(f"carrera {carreras(1)}")
     print(f"asignaturas {asignaturas}")
     print(f"notas {promedios}")
   else:
     print("intentelo denuevo mas tarde")
   if uno==2:
     print("1)alumno regular")
     print("2)alumno de notas")
     print("3)alumno de matricula")
     dd=input()
     if dd==1:
      print("Alumno regular")
      print(f"nombre {nombres(1)}")
      print(f"apellido {apellidos(1)}")
      print(f"rut {cosa(1)} ")
      print(f"carrera {carreras(1)}")
      print(f"Valor{dineros}")
     if dd==2:
      print("Alumno De notas")
      print(f"nombre {nombres(1)}")
      print(f"apellido {apellidos(1)}")
      print(f"rut {cosa(1)} ")
      print(f"carrera {carreras(1)}")
      print(f"asignaturas {asignaturas}")
      print(f"notas {promedios}")
      print(f"Valor{dineros}")
     if dd==3:
      print("Alumno De promedio")
      print(f"nombre {nombres(1)}")
      print(f"apellido {apellidos(1)}")
      print(f"rut {cosa(1)} ")
      print(f"carrera {carreras(1)}")
      print(f"asignaturas {asignaturas}")
      print(f"notas {promedios}")
      print(f"Valor{dineros}")
   if uno==3:
      print("adios")

     
     