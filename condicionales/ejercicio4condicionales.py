# crear un programa que simule un cajero automatico 
# la cuenta de cliente tiene saldo inicial de $2000
# el ATM tiene el siguiente menu
# 1 = ingreso de dinero
# 2 = retirar dinero
# 3 = mostrar dinero disponible
# 4 = salir

saldo=2000
print("1. Ingreso de dinero")
print("2. Retiro de dinero")
print("3. Mostrar dinero disponible")
print("4. Salir")

seleccion=int(input("Ingrese la opción deseada: "))

if seleccion ==1:
    ingreso= float(input("Ingrese el importe deseado: "))
    saldo+=ingreso
    print(f"Nuevo saldo: {saldo}")
elif seleccion ==2:
    retiro=float(input("Dinero a retirar: "))
    if retiro > saldo:
        print("Fondos insuficientes")
    else:
        saldo-=retiro
        print("Obtenga su dinero")
        print(f"Nuevo saldo: {saldo}")
elif seleccion==3:
    print(f"El saldo disponible es {saldo}")
elif seleccion==4:
    print("Muchas gracias. Retire su tarjeta")
else:
    print("Opcion invalida")



    