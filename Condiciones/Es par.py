#Realizar un programa que verifique que un numero es par o impar
# N = int(input("ingrese un numero: "))
# if (N % 2 == 0):
#     print ("Es par")
# else: 
#     print ("es impar")
    
def par(Numero):
    if (Numero % 2 == 0):
        return True
    else:
        return False

N = int(input("ingrese un numero"))
R = par(N)
if (R == True):
    print("Es par")
else: 
    print ("Es impar")
