from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

def boton_aceptar():
    # Segunda ventana
    ventana2 = Tk()
    ventana2.geometry("320x320")
    ventana2.title("¿Edad actual que tienes?")
    ventana2.config(bg="Slategray2")
    ventana2.resizable(False, False)
    

    Label1v2 = Label(text="Selecciona tù rango de edad")

    Label1v2.config(fg="gray30", bg="cadetblue1", font=("Comic Sans MS",22))
    def edad_3_a_5_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 3 a 5 años")
        ventana3.config(bg="OrangeRed3")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para niños de 3 a 5 años--\n\n En esta edad pueden realiar los siquientes tipos de ejercicios:\n\n Baloncesto\n\nFutbol\n\n Baile\n\n")
        texto_niños.config(bg="OrangeRed3",fg="Black", font=("Comic Sans MS",22))
        texto_niños.place(x=50,y=5,width=900,height=500)
    def edad_6_a_11_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 6 a 11 años")
        ventana3.config(bg="OrangeRed3")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para niños de 5 a 11 años--\n\n En esta edad pueden realiar los siquientes tipos de ejercicios:\n\n Baloncesto\n\nFutbol\n\n Baile\n\n")
        texto_niños.config(bg="OrangeRed3",fg="Black", font=("Comic Sans MS",22))
        texto_niños.place(x=50,y=5,width=900,height=500)
    def edad_12_a_19_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 12 a 19 años")
        ventana3.config(bg="OrangeRed3")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para jovenes  de 12 a 19 años--\n\n En esta edad pueden realiar los siquientes tipos de ejercicios:\n\n Baloncesto\n\nFutbol\n\n Baile\n\n")
        texto_niños.config(bg="OrangeRed3",fg="Black", font=("Comic Sans MS",22))
        texto_niños.place(x=50,y=5,width=900,height=500)
    def edad_20_a_26_años():
        ventana3 = Tk()
        ventana3.geometry("1000x650")
        ventana3.title("Accediste a los ejercicios de la edad de 19 a 26 años")
        ventana3.config(bg="OrangeRed3")
        ventana3.resizable(0, 0)
        texto_niños= Label(ventana3, text= "\n--Ejercicios para personas adultos de 20 a 26 años--\n\n En esta edad pueden realiar los siquientes tipos de ejercicios:\n\n Baloncesto\n\nFutbol\n\n Baile\n\n")
        texto_niños.config(bg="OrangeRed3",fg="Black", font=("Comic Sans MS",22))
        texto_niños.place(x=50,y=5,width=900,height=500)
    # Imagen que aparece en la entrada de los botones
    img=PhotoImage(file="carlos.png")
    lb_img= Label(ventana2,image=img)
    lb_img.place(x=150,y=150) 
    
    # Imagen que aparece en la entrada de los botones
    
    
    


    # Botón para acceder a la edad de 3 a 5 años
    boton_niños3_5=Button(ventana2,text="3-5",command=edad_3_a_5_años) 
    # Ubicació para el botón para edades de 3 a 5 años

    boton_niños3_5.place(x=30,y=30, width=100,height=40)
    # Botón para acceder a la edad de 6 a 11 años
    boton_niños6_11=Button(ventana2,text="6-11",command=edad_6_a_11_años) 

    # Ubicació para el botón para edades de 6 a 11 años
    boton_niños6_11.place(x=30,y=90, width=100,height=40)

    # Botón para acceder a la edad de 12 a 19 años
    boton_niños6_11=Button(ventana2,text="12-19",command=edad_12_a_19_años) 
    # Ubicació para el botón para edades de 12 a 19 años
    boton_niños6_11.place(x=30,y=150, width=100,height=40)

    # Botón para acceder a la edad de 20 a 26 años
    boton_niños6_11=Button(ventana2,text="20-26",command=edad_20_a_26_años) 
    # Ubicació para el botón para edades de 20 a 26 años
    boton_niños6_11.place(x=30,y=210, width=100,height=40)
    

    



 
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