from tkinter import *
from tkinter import messagebox 
import sqlite3

def conexionBBDD():
    miConexion= sqlite3.connect("Toys")
    micursor=miConexion.cursor()
    try:
        micursor.execute('''Create Table Toy(ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50),MARCA VARCHAR(50),Serie VARCHAR(50))''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
        messagebox.showwarning("¡ATENCION!","La base de datos ya existe")
def salir():
    valor=messagebox.showwarning("¡ATENCION!","¿Deseas salir?")
    if valor=="yes":
        root.destroy()
def limpiarcampos():
    miID.set("")
    miNombre.set("")
    miMarca.set("")
    miSerie.set("")

def eliminar():
    try:
        miConexion=sqlite3.connect("Toys")
        micursor=miConexion.cursor()
        micursor.execute("Delete From Toy where ID=?",(miID.get()))
        miConexion.commit()
        messagebox.showinfo("BBDD","Registro Eliminado")
    except:
        messagebox.showinfo("BBDD","Algo a fallado")


def leer():
    miConexion = sqlite3.connect("Toys")
    micursor = miConexion.cursor()
    micursor.execute("Select * FROM Toy where ID=" + miID.get())
    eljuguete = micursor.fetchall()
    for juguete in eljuguete:
        miID.set(juguete[0])
        miNombre.set(juguete[1])
        miMarca.set(juguete[2])
        miSerie.set(juguete[3])
        miConexion.commit()

def insertar():
    try:
        miConexion=sqlite3.connect("Toys")
        micursor=miConexion.cursor()
        micursor.execute("INSERT INTO Toy values(Null,?,?,?)",(
        miNombre.get(),miMarca.get(),miSerie.get()))
        miConexion.commit()
        messagebox.showinfo("BBDD","Registro insertado con exito")
    except:
        pass
        #messagebox.showinfo("BBDD","Algo a fallado")
def actualizar():
    try:
        miConexion=sqlite3.connect("Toys")
        micursor=miConexion.cursor()
        micursor.execute("Update Toy set Nombre=?,Marca=?,Serie=? where ID=?",
                           (miNombre.get(), miMarca.get(),miSerie.get(),miID.get()))
        miConexion.commit()  
        messagebox.showinfo("BBDD","Registro Actualizado")                           
    except:
        messagebox.showwarning("BBDD","Algo a fallado")
root=Tk()
barramenu=Menu(root)  
root.config(menu=barramenu,width=300,height=300)    
bbddmenu=Menu(barramenu,tearoff=0)
bbddmenu.add_command(label="Conectar",command=conexionBBDD)
bbddmenu.add_command(label="Salir",command=salir)

borrarmenu=Menu(barramenu,tearoff=0)
borrarmenu.add_command(label="Borrar campos",command=limpiarcampos)

crudMenu=Menu(barramenu,tearoff=0)
crudMenu.add_command(label="Crear",command=insertar)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Eliminar",command=eliminar)

barramenu.add_cascade(label="BBDD",menu=bbddmenu)
barramenu.add_cascade(label="Borrar",menu=borrarmenu)
barramenu.add_cascade(label="CRUD",menu=crudMenu)
miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miMarca=StringVar()
miSerie=StringVar()

CuadroID=Entry(miFrame,textvariable=miID)
CuadroID.grid(row=0,column=1,padx=10,pady=10)

CuadroNombre=Entry(miFrame,textvariable=miNombre)
CuadroNombre.grid(row=1,column=1,padx=10,pady=10)
#CuadroNombre.config(fg="red",justify="right")

CuadroMarca=Entry(miFrame,textvariable=miMarca)
CuadroMarca.grid(row=2,column=1,padx=10,pady=10)

CuadroSerie=Entry(miFrame,textvariable=miSerie)
CuadroSerie.grid(row=3,column=1,padx=10,pady=10)
#Label
idlabel=Label(miFrame,text="ID:")
idlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombrelabel=Label(miFrame,text="Nombre:")
nombrelabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

marcalabel=Label(miFrame,text="Marca:")
marcalabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

serielabel=Label(miFrame,text="Serie:")
serielabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)
#Botones
miFrame2=Frame(root)
miFrame2.pack()
botonCrear=Button(miFrame2,text="Crear",command=insertar)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Update",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonEliminar=Button(miFrame2,text="Delete",command=eliminar)
botonEliminar.grid(row=1,column=3,sticky="e",padx=10,pady=10)
root.mainloop()  