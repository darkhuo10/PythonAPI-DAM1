import requests
from tkinter import *

def obtener_datos(name):
    try:
        c = 1
        while c<16:
            url = "https://rickandmortyapi.com/api/character/{}".format(c)
            c+=1
            response = requests.get(url)
            personaje=response.json()
            nombre_json=personaje["name"]

            if(name==nombre_json):
                print("Nombre: ", personaje["name"])
                print("Estado: ", personaje["status"])
                print("Especie: ", personaje["species"])
                print("Género: ", personaje["gender"])

                name = personaje["name"]
                status = personaje["status"]
                species = personaje["species"]
                gender = personaje["gender"]

                nombre["text"] = "Nombre: {}".format(name)
                estado["text"] = "Estado: {}".format(status)
                especie["text"] = "Especie: {}".format(species)
                genero["text"] = "Género: {}".format(gender)

    except:
        print("Error")


ventana=Tk()
ventana.geometry("400x500")
ventana.title("Rick y Morty")
ventana.configure(bg="#06FAE2")

texto_intro=Label(ventana, text="Introduce el nombre del personaje:", font=("Arial",15,"bold"), justify="center", bg="#06FAE2",fg="#005166")
texto_intro.pack(padx=10,pady=10)

nombre_personaje=Entry(ventana,font=("Arial",20,"normal"), justify="center", bg="#03CDB9",fg="#005166")
nombre_personaje.pack(padx=30, pady=30)

boton_info=Button(ventana,text="Mostrar información", font=("Arial",15,"bold"), bg="#ACFF5E", fg="#6806AC", command=lambda:obtener_datos(nombre_personaje.get()))
boton_info.pack(padx=20, pady=10)

nombre=Label(ventana, font=("Arial",15,"bold"), bg="#06FAE2",fg="#005166")
nombre.pack(padx=10, pady=10)

estado=Label(ventana, font=("Arial",15,"bold"), bg="#06FAE2",fg="#005166")
estado.pack(padx=10, pady=10)

especie=Label(ventana, font=("Arial",15,"bold"), bg="#06FAE2",fg="#005166")
especie.pack(padx=10, pady=10)

genero=Label(ventana, font=("Arial",15,"bold"), bg="#06FAE2",fg="#005166")
genero.pack(padx=10, pady=10)

ventana.mainloop()