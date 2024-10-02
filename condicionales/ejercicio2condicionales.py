#crear un programa que pida 3 numeros y determine cual es el mayor

n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese otro numero: "))
n3=int(input("Ingrese otro numero: "))

if n1>=n2 and n1>=n3:
    print(f"{n1} es el numero mas grande")
elif n2>=n1 and n2>=n3:
    print(f"{n2} es el numero mas grande")
elif n3>=n1 and n3>=n2:
    print(f"{n3} es el numero mas grande")

