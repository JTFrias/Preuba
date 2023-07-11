import numpy as df
from datetime import datetime as dt
now = dt.now()
hoy=dt.today
apartamentos=[["a",1,2,5,4,5,6,7,8,9,10],["b",1,2,3,4,5,6,7,8,9,10],["c",1,2,3,4,5,6,7,8,9,10],["d",1,2,3,4,5,6,7,8,9,10]]
menu=True
ruts=[19592323,25324233,61345236]
compradores=[]
TipA=3800
TipB=3000
TipC=2800
TipD=3500
accum=0
accum2=0
accum3=0
accum4=0
nombres=[]
apellidos=[]
print("ingrese su nombre")
nombre=input()
nombres.append(nombre)
print("ingrese su apellido")
apellido=input()
apellidos.append(apellido)
print(nombres)
print("-----------Menu----------------") 
print("1)ver apartamentos disponibles")
print("2)comprar habitacion ")
print("3)lista de compradores")
print("4)Mostrar ganancias totales")
print("5)Salir")
ingresa=int(input())
if ingresa==1:
    for i in apartamentos:
      print(i)
elif ingresa==2:
    print("ingrese el tipo de piso de apartamento ejemplo A B C D")
    b=input()
    print(f"ingrese el piso del apartamento que quiere comprar")
    a=int(input())
    print("ahora ingrese su rut sin el digito verificador y sin puntos ni guion")
    rut=int(input())
    if rut > 1 and rut < 7:
        print("invalido")
    elif rut > 8 and rut <=9:
        print("guardado")
        ruts.append(rut)
        if a==1 and a==2 and a==3 and a==4 and a==5 and a==6 and a==7 and a==8 and a==9 and a==10 and b=="a":
           TipA+=accum
           apartamentos[0].pop(a)
           print(f"Tipo A 3800 UF: {accum} ")
        elif a==1 and a==2 and a==3 and a==4 and a==5 and a==6 and a==7 and a==8 and a==9 and a==10 and b=="b":
            TipB+=accum2
            apartamentos[1].pop(a)
        elif a==1 and a==2 and a==3 and a==4 and a==5 and a==6 and a==7 and a==8 and a==9 and a==10 and b=="c":
            TipC+=accum3
            apartamentos[2].pop(a)
        elif a==1 and a==2 and a==3 and a==4 and a==5 and a==6 and a==7 and a==8 and a==9 and a==10 and b=="d":
            TipD+=accum4
            apartamentos[3].pop(a)
        print(apartamentos)
        
elif ingresa==3:
      for i in ruts:
        print(ruts.sort())  
elif ingresa==4:
      aa=apartamentos.count("x")
      tacum=accum+accum2+accum3+accum4
      print("--------------------------")
      print(f"Tipo A 3800 UF: {aa} : {accum} ")
      print(f"Tipo B 3800 UF: {aa} : {accum2} ")
      print(f"Tipo C 3800 UF: {aa} : {accum3} ")
      print(f"Tipo D 3800 UF: {aa} : {accum4} ")
      print(f"total : ")
elif ingresa==5:
      print(nombres(1))
      print(apellidos(1))
      print(hoy)