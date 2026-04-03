temperatura = float(input("ingrese grados: "))
escala = input("Es fareheint(F) o celsius(C)?: "). lower ()
if escala ==  "f":
    celsius = (temperatura - 32) * 5/9
    print ("en grados celsius es: ", celsius )
elif escala == "c":
    fareheint = temperatura * 1.8 + 32
    print("es grados faraheit es: ", fareheint)
else:
    print("no hay escala que pueda converti")    
    

