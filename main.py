from tkinter import *

import tkinter.messagebox



#fonction des differentes glisieres 
def Slider(value):
#variable r stocke red_scale
    r = red_Scale.get()
#variable g stocke geen_scale
    g = green_Scale.get()
#variable b stocke blue_scale
    b = blue_Scale.get()
#variable rgb stocke les élement d'échelle rgb 
    rgb = f'{r}, {g}, {b}'
#définition de l'échelle initiale
    code = "#%02x%02x%02x" % (r,g,b)
#le champ colorlabel aura pour background l'élement code précedement crée
    colorLabel.config(bg=code)
#l'entrée rdb de fin 
    rgb_entry.delete(0, END)
#l'éntrée rgb d'insertion
    rgb_entry.insert(0, rgb)



#creation de la fonction clique copy
def onClick():
#envoie ce message si la fonction onclick est appelé 
    tkinter.messagebox.showinfo("copy to clipboard", "votre couleur rgb code("+rgb_entry.get()+") est copier")
#crée une fenetre
    clip = Tk()
#retire la fenetre
    clip.withdraw()
#nettoyer la fenetre
    clip.clipboard_clear()
#ajoute a la fenetre la donnée rgb_entry 
    clip.clipboard_append(rgb_entry.get())
#fin de la fenetre
    clip.destroy()




#crée une fenetre 
root = Tk()

#donne le titre a cette fenetre
root.title("Master Lipakumu Color Piker")

#donne une taille a cette fenetre
root.geometry("360x380+100+100")

#crée un espace appelée colorlabel dans la fenetre nomée root avec un background noir etc...
colorLabel = Label(root, bg="black", width=50, height=10, bd=1, relief=None)
#positionnement de color label par rapport a root
colorLabel.pack(pady=5)



frame = Frame(root, bd=1, relief=None)
#positionnement de frame par rapport a root
frame.pack(pady=5)


#crée un espace appelée red_label dans la fenetre nomée frame avec un font-color rouge etc...
red_label= Label(frame, text="Red", fg="red", font=("Time new Roma", 12, "bold"))
#positionnement de red_label par rapport a frame
red_label.grid(row=0, column=0)


#crée une glissiere appelée red_scale dans la fenetre nomée frame avec un font-color rouge etc...
red_Scale = Scale(frame, to = 255, from_ = 0, length = 210, fg="red", orient = HORIZONTAL, command = Slider)
#positionnement de red_label par rapport a frame
red_Scale.grid(row=0, column=1)


#crée un espace appelée green_label dans la fenetre nomée frame avec un font-color vert etc...
green_label = Label(frame, text="Green", fg="green", font=("Time New Roman", 12, "bold"))
#positionnement de green_label par rapport a frame
green_label.grid(row=1, column=0)

green_Scale = Scale(frame, from_=0, to=255, length=210, fg="green", orient=HORIZONTAL, command=Slider)
green_Scale.grid(row=1, column=1)

blue_label = Label(frame, text="Blue", fg="blue", font=("Time New Roman", 12, "bold"))
blue_label.grid(row=2, column=0)

blue_Scale = Scale(frame, to = 255, from_ = 0, length=210, fg="blue", orient=HORIZONTAL, command=Slider)
blue_Scale.grid(row=2, column=1)


#crée une seconde fenetre appelé frame2 
frame2 = Frame(root, relief=None, bd=1)
#positionnement de frame 2 par rapport a root
frame2.pack(pady=5)

#affiche RGB CODE :
rgb_label = Label(frame2, text='RGB CODE  :', font=("Time New Roman", 12, "bold"))
rgb_label.grid(row=2, column=0)


# crée une entrée nommée rgb dans la fenetre frame2
rgb_entry = Entry(frame2, width=12, font=("Time New Roman", 12))
#positionnement
rgb_entry.grid(row=2, column=1, padx=5)
#insert la donée d'entreé de l'echelle final
rgb_entry.insert(END, '')



#crée un boutton nomée copy qui va faire appel a la fonction onclick
Copy = Button(frame2, text="COPY", font=("Time New Roman", 12, "bold"), command=onClick)
#positionnement
Copy.grid(row=3, columnspan=2, pady=7)




#lance la fenetre root
root.mainloop()

#MasterLipakumu Color Piker

