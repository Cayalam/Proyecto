from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

def boton_aceptar():
    # Segunda ventana
    ventana2 = Tk()
    ventana2.geometry("320x320")
    ventana2.title("¿Edad actual que tienes?")
    ventana2.config(bg="Slategray2")
    ventana2.resizable(0, 0)
    

    Label1v2 = Label(text="Selecciona tù rango de edad")

    Label1v2.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
    def edad_3_a_5_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 3 a 5 años")
        ventana3.config(bg="SkyBlue2")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para niños de 3 a 5 años--\n\n En esta edad pueden realiar los siquientes tipos de ejercicios:\n\n Baloncesto\n\nFutbol\n\n Baile\n\n")
        texto_niños.config(bg="SkyBlue2",fg="Black", font=("Comic Sans MS",20))
        texto_niños.place(x=50,y=5,width=900,height=500)
    def edad_6_a_11_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 6 a 11 años")
        ventana3.config(bg="SkyBlue2")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para niños de 6 a 11 años--\n\n En esta edad pueden realiar los siquientes tipos de ejercicios:\n\nAtletismo\n\n Baloncesto\n\nFutbol\n\nTae Kwon Do o Judo\n\n")
        texto_niños.config(bg="SkyBlue2",fg="Black", font=("Comic Sans MS",20))
        texto_niños.place(x=50,y=5,width=900,height=500)
    def edad_12_a_19_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 12 a 19 años")
        ventana3.config(bg="SkyBlue2")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para jovenes  de 12 a 19 años--\n\n se empieza con el calentamiento:Salto de tijera, estiramiento de brazo,\ntrotar,Saltos con cuerda.\n\n Ya cuando se ha calentado el cuerpo sequimos con:\n Flexiones con inclinaciòn(12 Repeticiones)\n Flexiones con brazos abiertos(8 R ) Flexiones con apoyo de rodilla(12 R)\n Crunch Abdominales(10 R),Twits Ruso(7 R),Elevaciones de piernas(12 R)\n\nPara terminar con la rutina diaria: \nEstiramiento de cobra(60 s), Estiramiento\n de pecho(80 s).\n\n Ademas otros ejercicios podria ser el:\n Atletismo, Ciclismo,Futbol,Nataciòn\n\n")
        texto_niños.config(bg="SkyBlue2",fg="Black", font=("Comic Sans MS",19))
        texto_niños.place(x=50,y=5,width=900,height=500)
    def edad_20_a_26_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 19 a 26 años")
        ventana3.config(bg="SkyBlue2")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para personas adultos de 20 a 26 años--\n\n En esta edad pueden realiar los siquientes tipos de ejercicios:\n\n Iniciamos con el calentamiento:\n Salto de tijera(40 s),Trotar(60 s),Saltar Laso(120 s),Rotaciones \nde Brazo(20 R) \n\nDespues de haber calentado:\nAbdominales(30 R), Cruch de bicicleta(24 R),Butt britge(18 R)\n Abdominales en V(18 R),Burpees(12 R), Flexiones en Diamante(16 R)\nFlexiones con Inclinacion(20 R)\n\nPara concluir con la rutina:Estiramiento de Hombros(30 s)\n Estiramiento de cobra(30 s), Estiramiento de pecho(30 s)")
        texto_niños.config(bg="SkyBlue2",fg="Black", font=("Comic Sans MS",20))
        texto_niños.place(x=0,y=5,width=1000,height=650)
    # Imagen que aparece en la entrada de los botones
  
    
    # Imagen que aparece en la entrada de los botones
    
    
    


    # Botón para acceder a la edad de 3 a 5 años
    boton_niños3_5=Button(ventana2,text="3-5",command=edad_3_a_5_años) 
    # Ubicació para el botón para edades de 3 a 5 años
    boton_niños3_5.pack(pady=15)
    boton_niños3_5.config(width=14,height=2)

    # Botón para acceder a la edad de 6 a 11 años
    boton_niños6_11=Button(ventana2,text="6-11",command=edad_6_a_11_años) 

    # Ubicació para el botón para edades de 6 a 11 años
    boton_niños6_11.pack(pady=15)
    boton_niños6_11.config(width=14,height=2)


    # Botón para acceder a la edad de 12 a 19 años
    boton_niños12_19=Button(ventana2,text="12-19",command=edad_12_a_19_años) 
    # Ubicació para el botón para edades de 12 a 19 años
    boton_niños12_19.pack(pady=15)
    boton_niños12_19.config(width=14,height=2)

    # Botón para acceder a la edad de 20 a 26 años
    boton_niños20_26=Button(ventana2,text="20-26",command=edad_20_a_26_años) 
    # Ubicació para el botón para edades de 20 a 26 años
    boton_niños20_26.pack(pady=15)
    boton_niños20_26.config(width=14,height=2)
    

    



 
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