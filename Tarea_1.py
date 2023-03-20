ARG=203.35
MXN=18.49
COL=4849.99

def convertir_dolar(valor,region):
    cantidad_dolar = int(input("Ingrese la cantidad en Dolares : "))
    conversion=cantidad_dolar*valor
    print(f" El valor es {conversion} pesos {region}")

nombre = input("cual es su nombre: ")
print (f"Hola {nombre},bienvenidos al conversor de monedas ")
print ("Seleccione una conversion: ")
print ("1.- Pesos Argentinos")
print ("2.- Pesos Colombianos")
print ("3.- Pesos Mexicanos")
opcion = int(input("Seleccione la opcion "))

if opcion == 1 :
    convertir_dolar(ARG,"Argentinos")
else:
    if opcion == 2 :
      convertir_dolar(COL, "Colombianos")
    else:
       if opcion == 3 :
        convertir_dolar(MXN, "Mexicanos")
       else:
           print("Ingrese un valor valido")
