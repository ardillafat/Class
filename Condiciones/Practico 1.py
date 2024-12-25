# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  1. Mayor o Menor Edad %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # def edad_mayor(Edad):
    #     if (Edad>=18):
    #         return True
    #     else:
    #         return False

    # X = int(input("Escribe tu edad: "))
    # R = edad_mayor(X)
    # if (R == True):
    #     print("Eres mayor")
    # else:
    #     print("Eres menor")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  2. Numero Positivo o Negativo %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # def Numero(numero):
    #     if (numero > 0):
    #         return 1
    #     else:
    #         if(numero == 0):
    #             return 2
    #         else:
    #             return 3
    # X = int(input("Escribe tu numero: "))
    # R = Numero(X)

    # if (R == 1):
    #     print("Es Positivo")
    # if (R == 2):
    #     print ("El cero es neutro")
    # if (R == 3):
    #     print("Es negativo")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  3. Par o Impar %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # def Par(Numero):
    #     if (Numero / 2 == 0):
    #         return True
    #     else:
    #         False
            

    # N = int(input("ingrese un numero: \n"))
    # R = Par(N)
    # if (R == True):
    #     print("Es par")
    # else: 
    #     print ("Es impar")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  4. Aprobado o Reprobado %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # def Media_ponderada (n1,p1,n2,p2,n3,p3):
    #     mp = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
    #     return mp

    # n1 = float (input ("Ingrese la nota 1 \n"))
    # p1 = float (input ("Ingrese la mp 1 \n"))
    # n2 = float (input ("Ingrese la nota 2 \n"))
    # p2 = float (input ("Ingrese la mp 2 \n"))
    # n3 = float (input ("Ingrese la nota 3 \n"))
    # p3 = float (input ("Ingrese la mp 3 \n"))

    # R = Media_ponderada(n1,p1,n2,p2,n3,p3)
    # if (R >= 51):
    #     print("Pasó con: ", R)
    # else:
    #     print("No pasó, se quedo con: ", R)




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  5. ¿Es divisible 5? %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # Numero = int(input("pon el numero deseado: \n" ))

    # if (Numero % 5 == 0):
    #     print ("El numero es divisibe entre 5, el resultado es: ", (Numero / 5))
    # else:
    #     print ("El numero No es divisble entre 5, el resultado es: ")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  6. Validar contraseña %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # PasswordMain = "admin123"

    # PutPassword = input("Ingrese la contraseña: ")

    # if (PasswordMain == PutPassword):
    #     print  ("Acceso concebido")
    # else:
    #     print ("Acceso denegado")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  7. Numero mayor a 100 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # def Mayor(numero):
    #     if (numero >= 100):
    #         return True
    #     else:
    #         return False

    # Numero = float(input("Ingrese el numero deseao: "))
    # R = Mayor(Numero)

    # if (R == True):
    #     print ("Es mayor")
    # else: 
    #     print ("Es menor ")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  8. Elegibilidad para votar %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # def Edad_Votar(Edad):
    #     if (Edad>=18):
    #         return True
    #     else:
    #         return False

    # X = int(input("Escribe tu edad: "))
    # R = Edad_Votar(X)
    # if (R == True):
    #     print("Puedes votar")
    # else:
    #     print("Puedes votar")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  9. Clima frio o caliente %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

#No se como usar valores de temperatura




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  10. Número dentro del rango %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # def Limite(Numero):
    #     if Numero in range (0, 50):
    #         print (Numero, "Esta dentro del rango")
    #     else: 
    #         print (Numero, "Esta fuera del rango")

    # numero = float(input("Elije el numero dentro del rango 0-50: "))
    # x = Limite(numero)
    # print (x)
#Me dio algo de flojera realzaiar el comadno (If Numero ion range (0, 50): [return true], else: [return false]) y seguir con el comando (if Numero == true (o false), return [un valor]) porque creia que era mejor y mas directo hacer como esta, ignorando la respuesta "none". Creo que si hacia  el paso que me salte, desaparece el "none" y sale el valor true, para despues decir que el valor true = (Valor dentro del rango). Pero igual prefiero obtar por el paso directo, ignorando totalemnte la respuesta "none" de la función.




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  11. ¿Es un multiplo de 3? %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # Numero = int (input ("Ingrese el valor deseado: "))

    # if (Numero % 3 == 0):
    #     print ("El numero es multiplo de 3, el resultado es: ", (Numero / 3))
    # else:
    #     print ("El numero No es multiplo de 3")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  12. Compra Minima %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

#   ............. Forma sencilla ............

    # Gasto_realziado = float ( input ("Ingrese el monto de su compra: "))
    # if (Gasto_realziado >= 100):
    #     print("Haz ganado un cupon de descuento, gracias a tu compra que revaza los 100bs")
    # else: 
    #     print("Desea aumentar el costo de su compra? Puede llegar a ganar un cupon de descuento")


#   ............. Como Funcion ............
    # def Gasto (Monto):
    #     if (Monto >= 100):
    #         return True
    #     else:
    #         return False

    # Dinero = float (input ("Ingrese el gasto realizado: "))
    # Proceso = Gasto(Dinero)

    # if (Proceso == True):
    #     print ("Felicidades, Gracias a su Compra de más de 100bs ¡Ganó un cupon de descuento!")
    # else: 
    #     print ("Desea agrandar su compra? Por un monto superior a 100bs, puede ganar un Cupon de descuento")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  13. Es una vocal %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # Abecedario = ['A', 'E', 'I', 'O', 'U']

    # Letra = str ( input ("Ingrese la Letra que desee (EN MAYUSCULA): "))
    # if (Letra in Abecedario ):
    #     print ("Su Letra esta dentro del abecedario")
    # else: 
    #     print ("Su Letra esta fuera del abecedario")



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  14. Edad Para trabajar %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # print ("La edad minima para ingresar a trabajr denotr de nuestra empresa es de 17 años, ¿Cuantos años tiene usted?")
    # edad = int ( input ("Ingrese su edad: "))
    # if (edad >= 17): 
    #     print ("Uds esta dentro del rango para poder trabajar junto a nosotros")
    # else: 
    #     print ("usted es menor al requerimiento que pedimos para poder ingresar a trbajar dentro de la empresa")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  15. Numero mayor que otro %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # numero = input ("ingrese el primero numero que desee: ")

    # def Comparación (Numero):
    #     if (Numero >= numero):
    #         return True
    #     else:
    #         return False

    # N = input ("Ingrese el segundo numero que desee: ")
    # R = Comparación (N)
    # if (R == True):
    #     print((N),"es mayor que ", numero)
    # else:
    #     print((N),"es menor que ", numero)
    # #Ni idea como lo hice pero me funcionó jajajaja, y ni me pregunte del como es que da el resultado ese jajajaja




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  16. Cáculo de descuento %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    # Compra_realizada = float (input ("Gasto total de la compra: "))
    # Descuento_navideño = 10 / 100

    # print ("Aplicando descuento navideño del 10%, a la comrap realizada")
    # Descuento = Compra_realizada * Descuento_navideño
    # Descuento_total = Compra_realizada - Descuento

    # print ("El monto total, junto al descuento navideño es de: ", Descuento_total)
# La verdad no supe como hacerlo, entoces tuve que pedir ayuda a la AI




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  17. Validación de hora %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # print ("Evaluacion de hora limite dentro del formato de 24 horas")

    # Hora = int ( input ("ingrese la hora deseada: "))

    # if (Hora in range (0,24)):
    #     print ("La hora deseada está dentro del formato de 24/H")
    # else: 
    #     print ("La hora deseada no está dentro del formato de 24/H")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  18. Número igual a cero %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # Numero = int ( input ("Ingrese un numero cualqueira: "))

    # if (Numero == 0):
    #     print ("El numero puesto es igual a cero")
    # else:
    #     if (Numero >= 0):
    #         print ("Su numero rebaza a 0")
    #     else:
    #         print ("Su numero es menor a 0")





# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  19. Mayor que 1000 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # def Numero (Mayor):
    #     if (Mayor >= 1000):
    #         return True
    #     else: 
    #         return False

    # N = float ( input ("Ingrese un valor: "))
    # Comparación = Numero(N)

    # if (Comparación == True):
    #     print ("El numero ingresado es mayor a 1000")
    # else: 
    #     print ("El numero ingresado es menor a 1000")




# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  20. Año bisiesto %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # Año = int ( input (" Ingrese el año que desea chequear si es bisiesto:  "))

    # if (Año % 4 == 0):
    #     print ("El año elejido es bisiesto")
    # else: 
    #     print ("El año elejido no es bisiesto")