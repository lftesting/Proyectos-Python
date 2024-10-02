# crear un programa que compare dos nombres 
# debe verificar si ambos nombres comienzan con la misma letra o terminan con la misma letra

nombre1=input("Escriba un nombre: ")
nombre2=input("Escriba otro nombre: ")

if nombre1 [0] == nombre2 [0] or nombre1 [-1] == nombre2 [-1]:
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

# el 0 usado entre [] identifica la primera letra
# el -1 usado entre [] identifica la ultima letra
