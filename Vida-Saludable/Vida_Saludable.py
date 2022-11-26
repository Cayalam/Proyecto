from tkinter import *
from tkinter import messagebox

def boton_aceptar():
    # Segunda ventana
    ventana2 = Tk()
    ventana2.geometry("650x570")
    ventana2.title("Vida Saludable")
    ventana2.config(bg="cadetblue1")
    ventana2.resizable(False, False)

    Label1v2 = Label(text="Seleccione su rango de edad")
    Label1v2.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
    Label1v2(ventana2)
 
# Ventana principal
root = Tk()
root.geometry("650x490")
root.title("Vida Saludable")
root.config(bg="cadetblue1")
root.resizable(False, False)

# Texto indicativo en forma de Label
Label1 = Label(text="Digite sus datos para continuar")
Label2 = Label(text="Nombre")
Label3 = Label(text="Peso(kilogramos)")
Label4 = Label(text="Altura(centímetros)")

#Configuración de los Label; tipo, tamaño y color de letra
Label1.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
Label2.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
Label3.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
Label4.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))

# Ubicación de los Label
Label1.place(x=100, y=40)
Label2.place(x=40, y=150)
Label3.place(x=40, y=230)
Label4.place(x=40, y=310)

# Entradas de texto
entrada1 = Entry() #"Nombre"
entrada2 = Entry() #"Peso(kilogramos)"
entrada3 = Entry() #"Altura(centímetros)"

#Foco de digitar texto en los entry
entrada1.focus_set()

#Configuración de las entradas; tipo, tamaño y color de letra
entrada1.config(bg="turquoise1", fg="steel blue", font=("Comic Sans MS",22))
entrada2.config(bg="turquoise1", fg="steel blue", font=("Comic Sans MS",22))
entrada3.config(bg="turquoise1", fg="steel blue", font=("Comic Sans MS",22))

# Ubicación de las entradas de texto y ajustes de tamaños de las mismas
entrada1.place(x=350, y=150, width=260,height=40)
entrada2.place(x=350, y=230, width=260,height=40)
entrada3.place(x=350, y=310, width=260,height=40)


# Botón de aceptar
boton_aceptar = Button(text="Aceptar",command=boton_aceptar)

# Ubicación del Botón aceptar
boton_aceptar.place(x=275,y=410, width=100,height=40)



root.mainloop()