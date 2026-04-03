saldo = 1000
intetos = 0 

print("Cajero automatico")

while intetos < 3:
    pin = int(input("ingresa tu pin: "))
    if pin == 1234:
        print("Acceso concedido\n")
        break
    else:
        print("pin incorreto")
        intetos += 1
        
if intetos == 3:
    print("Trajeta bloqueda")
else:            
    while True:
        print("\n1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = int(input("selecione una opcion: "))
        
        if opcion == 1:
             print(f"Tu saldo es: $ {saldo}")
        elif opcion == 2:
            deposito = int(input("cantidad a depositar: "))
            
            if deposito > 0:
                saldo += deposito
                print(f"deposito existoso. Nuevo saldo: ${saldo}")
            else:
                print("cantidad invalida")
        elif opcion == 3:
            Retiro = int(input("Cuanto desea retirar: "))
            
            if Retiro <= 0:
                print("cantidad invalida")
            elif Retiro > saldo:
                print("Fondos insuficientes")
            else:
                saldo -= Retiro
                print(f"Retiro existoso. Nuevo saldo ${saldo}")
        elif opcion == 4:
            print("Gracias por usar el cajero")
            break
        else:
            print("Opcion no valida")            
            
                
            
                    
                    
   
        
            
    
    