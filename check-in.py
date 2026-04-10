import datetime

def check_in():
    nombre = input("Ingrese su nombre: ")
    hora = datetime.datetime.now()
    registro = f"{nombre} - {hora}\n"
    with open("checkin.txt", "a") as archivo:
        archivo.write(registro)
    print("Check-in registrado exitosamente.")
    
def ver_registros():
    try:
        with open("checkin.txt", "r") as archivo:
            registros = archivo.readlines()
            if registros:
                print("Registros de Check-in:")
                for registro in registros:
                    print(registro.strip())
            else:
                print("No hay registros de check-in.")
    except FileNotFoundError:
        print("No se han registrado check-ins aún.")
while True:
    print("\n1. Realizar Check-in")
    print("2. Ver Registros de Check-in")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        check_in()
    elif opcion == "2":
        ver_registros()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")        
            
    