import customtkinter as ctk
from PIL import Image

GRID_SIZE = 11
my_image1 = ctk.CTkImage(light_image=Image.open("/Users/albert.dygov/Documents/PRIVAT/PRIVATEPROJEKTE/BilderFV/pentest.jpg"),size = (500,200))
my_image2 = ctk.CTkImage(light_image=Image.open("/Users/albert.dygov/Documents/PRIVAT/PRIVATEPROJEKTE/BilderFV/trouble.jpg"),size = (500,200))

#---------ROOT----------
root= ctk.CTk()
root.geometry("900x500")
root.title("Test Oberfläche")
root.resizable(True,True)


for i in range (GRID_SIZE):
    root.columnconfigure(i,weight=1)
    root.rowconfigure(i, weight=1)

#----------NAVBAR----------
nav_frame = ctk.CTkFrame(root,width= 50, height= 50, fg_color="darkred",corner_radius=0)
nav_frame.grid(row=0, column=0, columnspan = GRID_SIZE,sticky="nsew")
nav_frame.columnconfigure(1,weight=1)
nav_frame.columnconfigure(2,weight=1)
nav_frame.rowconfigure(1, weight=1)

#----------DRAG & DROP----------

drag = ctk.CTkFrame(root, width=50, height=50, fg_color="darkred")
drag.grid(row=6, column=8,rowspan=5, columnspan =3, sticky="nsew", padx= 10,pady=10)
drag.configure(corner_radius=10)

'''FONT'''
font1=('Courier New', 15)

'''LABEL'''
labelDrag = ctk.CTkLabel(drag, text="Drag file \nin here !",font=font1,text_color="white")
labelDrag.pack(expand =True)

#-----------FLASHDRIVE------------

flash = ctk.CTkFrame(root, width=50, height=50, fg_color="darkred")
flash.grid(row=1, column=8,rowspan=5, columnspan =3, sticky="nsew", padx= 10,pady=10)
flash.configure(corner_radius=10)

#-----------PENTESTTOOLL-------------
pen = ctk.CTkFrame(root,width=50, height=50, fg_color="darkgrey")
pen.grid(row=1, column=0,rowspan=5, columnspan =8, sticky="nsew", padx= 10,pady=10)
pen.configure(corner_radius=10)

pen.columnconfigure(1,weight=1)
pen.columnconfigure(2,weight=1)
pen.rowconfigure(1, weight=1)
pen.rowconfigure(2, weight=1)

image = ctk.CTkLabel(pen, image=my_image1, text="")
image.grid(row = 1,column =1, rowspan =2,columnspan = 2,padx=10,pady=10,sticky="nsw")

penBtn = ctk.CTkButton(pen,text = "test", fg_color="darkblue", corner_radius=0)
penBtn.grid(row = 2, column = 2,sticky="se",padx = 10,pady = 10)

#-----------TROUBLESHOOTINGTOOLL-------------
trouble = ctk.CTkFrame(root, width=50, height=50, fg_color="darkgrey")
trouble.grid(row=6, column=0,rowspan=5, columnspan =8, sticky="nsew", padx= 10,pady=10)
trouble.configure(corner_radius=10)

trouble.columnconfigure(1,weight=1)
trouble.columnconfigure(2,weight=1)
trouble.rowconfigure(1, weight=1)
trouble.rowconfigure(2, weight=1)

image = ctk.CTkLabel(trouble, image=my_image2, text="")
image.grid(row = 1,column =1, rowspan =2,columnspan = 2,padx=10,pady=10,sticky="nsw")

troBtn = ctk.CTkButton(trouble,text = "test", fg_color="darkblue",corner_radius=0)
troBtn.grid(row = 2, column = 2,sticky="se",padx = 10,pady = 10)

root.mainloop()
