#Realizar un programa que calcule si una edad ingresada por teclado representa meyoria de edad

# Edad = int(input("Ingrese Una Edad: "))
# if (Edad >= 18):
#     print ("mayor de edad")
# else:
#     print("menor de edad")

def edad_mayor(edad):
    if (edad>=18):
        return (True)
    else:
        return (False)
#Como consumirlo 
X = int(input( "ingrese una edad: "))
R = edad_mayor(X)
if (R == True):
    print("es mayor de edad")
else:
    print("es menor de edad")