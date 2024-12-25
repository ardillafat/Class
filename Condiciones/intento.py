def Si (Ganar):
    if (Ganar>= 100):
        return (True)
    else:
        return (False)

X = int(input("Ingrese_profit: "))
R = Si (X)
if (R == True):
    print ("profit")
else:
    print ("no hubo profit")    
    
