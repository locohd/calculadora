import tkinter as tk
import datetime

def check_in():
    nombre = entrada.get()
    hora = datetime.datetime.now()
    
    with open("checkin.txt", "a") as archivo:
        archivo.write(f"{nombre} - {hora}\n")
    
    resultado.config(text="Registrado correctamente")

ventana = tk.Tk()
ventana.title("Sistema Check-In")

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Check-In", command=check_in)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()