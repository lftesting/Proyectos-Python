#crear un programa que pida 2 numeros
#que obtenga como resultado cual de ellos es par o si ambos lo son

n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese otro numero: "))

if n1%2==0 and n2%2==0:
    print("Ambos numeros son pares")
elif n1%2==0 and n2%2!=0:
    print(f"{n1} es un numero par")
elif n1%2!=0 and n2%2==0:
    print(f"{n2} es un numero par")
else:
    print("Ambos numeros son impares")
    