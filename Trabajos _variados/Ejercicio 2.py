# n1 = int(input("Ingrese la nota 1: "))
# p1 = int(input("Ingrese la ponderacion 1: "))
# n2 = int(input("Ingrese la nota 2: "))
# p2 = int(input("Ingrese la ponderacion 2: "))
# n3 = int(input("Ingrese la nota 3: " ))
# p3 = int(input("Ingrese la ponderacion 3: "))
# mp = ((n1*p1)+(n2*p3)+(n3+p3)) / (p1+p2+p3)
# print(mp)


def media_ponderada(n1,p1,n2,p2,n3,p3):
    mp= ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
    return  mp
# n1 = int(input("Ingrese la nota 1: "))
# p1 = int(input("Ingrese la ponderacion 1: "))
# n2 = int(input("Ingrese la nota 2: "))
# p2 = int(input("Ingrese la ponderacion 2: "))
# n3 = int(input("Ingrese la nota 3: " ))
# p3 = int(input("Ingrese la ponderacion 3: "))
# print (media_ponderada(n1,p1,n2,p2,n3,p3))


print (media_ponderada(int(input("Ingrese nota 1: ")),int(input("Ingrese ponderación 1: ")),int(input("Ingrese nota 2:")),int(input("Ingrese ponderación 2: ")),int(input("Ingrese nota 3:")),int(input("Ingrese ponderación 2: "))))


