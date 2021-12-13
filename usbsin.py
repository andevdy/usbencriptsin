from os import name #importacion de recursos de os
from sys import path #importacion de recursos de sys
import threading 
from cryptography.fernet import Fernet, InvalidToken #imoortacion de fernet
from tkinter import * #importacion de recursos de tkinter
from tkinter import ttk #importacion de recursos de tkinter
from tkinter import filedialog #importacion de recursos de tkinter
from tkinter import messagebox #importacion de recursos de tkinter
import os.path #importacion de os.path

key = b'' #variable clave
key_ = b'' #variable copia de clave
keyglobal = b'DRdTHLlm2x6jjgV064wvmFKDRjWoJFAL0i4Sd3o-g_A' #variable clave global
def ramdom_key(): #clase generar clave al azar
    global key_ #definimos copia de clave como global
    key_ = Fernet.generate_key() #generamos una clave al azar con la ayuda de fernet
    Key_Entry.delete(0,"end") #verificamos si la clave esta vacia
    Key_Entry.config(state=NORMAL) #definimos el estado
    Key_Entry.insert(0,key_[:len(key)-1]) #insertamos la clave
    
def Start_Decrypt(): #clase comenzar a desencriptar archivo
    global key #definimos clave como global
    if len(Key_Entry.get()) <= 42: #verificamos la cantidad de caracteres menor a 42
        messagebox.showerror(title="Pocos Caracteres",message="debe tener 44 caracteres (más se eliminarán)") #generamos mensaje si se cumple la condicion
    else: #caso contrario a la condicion ingresara por aqui
        if len(Key_Entry.get()) >= 43: #verificamos la cantidad de caracteres mayor a 43
                l = Key_Entry.get() #extraemos la clave
                Key_Entry.delete(0,"end") #verificamos si la clave esta vacia
                Key_Entry.insert(0,l[:43]) #insertamos la clave
                key = str.encode(Key_Entry.get()) #codificamos la clave
                
        if str(key) == "b''": #preguntamos si la clave es igual
            messagebox.showwarning(message="Se necesita una Clave",title="Clave no Definida") #generamos mensaje si se cumple la condicion
        else: #caso contrario a la condicion ingresara por aqui
            if str(key[len(key)-1:]) != "b'='": #verificamos si el tamaño de clave es la misma
                key = key + str.encode(("=")) #continuacion de la linea anterior
        
        hilo2 = threading.Thread(target=Decrypt_file,daemon=True) #llamamos a la clase de desencriptacion
        hilo2.start() #iniciamos la clase
    print(key) #impriminos la clave
    print('key') #imprimimos la palabra key

# Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
CAFE = (90,50,15)
AZUL = (0,0,255)
GRIS = (128,128,128)
VERDE = (0,128,0)
AMARILLO = (255,255,0)

def Decrypt_file(): #clase desencriptar archivo
    if root.filename != None: #vemos si no existe ningun file
        try: #condicion en caso de que falle algo
            global key #definimos key como variable global
            
                
            Mas = Fernet(key) #con la ayuda de fernet extraemos la clave
            f = open(root.filename.name,"rb") #iniciamos la operacion con el nombre del archivo
            data = f.read() #leemos el archivo
            data_un = Mas.decrypt(data) #desencriptamos el archivo
            f.close() #finalizamos la operacion
            done = True #definimos done como verdadero
            i = 0 #la variabke i comenzara en 0
            while done: #mientras la condicion sea verdadera
                name = "Archivo_Desencriptado.cry" #definimos el nombre del nuevo archivo
                if os.path.isfile(name): #comparamos si existe un archivo con el mismo nombre
                    name = "Archivo_Desincriptado.cry "+str(i) #si existe entonces le agregamos un valor extra numeral
                if not os.path.isfile(name): #creamos el nuevo archivo si no existe el mismo nombre
                    done = False #definimos done como falso
                else: #si existe el mismo nombre
                    i = i + 1 #aumentamos el valor i
            f = open(name,"wb") #iniciamos la operacion con el nombre del archivo
            f.write(data_un) #escribimos el nombre del archivo
            f.close() #finalizamos la operacion
        except InvalidToken: #si la clave no es valida
            messagebox.showerror(title="Clave Invalida",message="Ingrese la Clave Correcta por Favor") #generamos mensaje si se cumple la condicion
        except: #si ocurre un error en la desencriptacion
            messagebox.showerror(title="ERROR",message="Falla en Desincriptacion") #generamos mensaje si se cumple la condicion
        else: #si la desencriptacion se realizo con existo
            messagebox.showinfo(title="Exito de Desincriptacion",message="El archivo ha sido desencriptado con exito, solo falta cambiar la extension adecuada") #generamos mensaje si se cumple la condicion

def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

def start_encrypt(): #clase comenzar a encriptar archivo
    global key_ #definimos clave como global
    if root.filename != None: #verificamos si el archivo existe
        print(len(Key_Entry.get())) #ingresamos a la clave
        if len(Key_Entry.get()) <= 42: #verificamos la cantidad de caracteres menor a 42
            messagebox.showerror(title="Pocos Caracteres",message="debe tener 44 caracteres (más se eliminarán)") #generamos mensaje si se cumple la condicion
        else: #caso contrario a la condicion
            if len(Key_Entry.get()) > 43: #verificamos la cantidad de caracteres mayor a 43
                    l = Key_Entry.get() #extraemos la clave
                    Key_Entry.delete(0,"end") #verificamos si la clave esta vacia
                    Key_Entry.insert(0,l[:43]) #insertamos la clave
                    key_ = str.encode(Key_Entry.get()) #codificamos la clave
            if str(key_) == "b''": #verificacion si la clave es la misma
                if len(Key_Entry.get()) >= 43: #verificamos si la clave es mayor a 43
                    key_ = str.encode(Key_Entry.get() + "=") #codificamos la copia clave
                else: #si la clave es menor a 43
                    messagebox.showwarning(message="Se necesita una Clave",title="Clave no Definida")#generamos mensaje si se cumple la condicion
            else: #si la clave no es la misma
                if str(key_[len(key_)-1:]) != "b'='": #verificamos si tiene a misma clave
                    key_ = key_ + str.encode(("=")) #continuacion de la linea anterior
            hilo = threading.Thread(target=encrypt_file,daemon=True) #llamamos a la clase encriptar archivo
            hilo.start() #ejecutamos la clase
        print(len(Key_Entry.get())) #imprimimos la clave
        print(key_) #imprimimos la copia de la llave
        print('key_') #imprimimos la palabra key_

def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

def encrypt_file(): #clase encriptar archivo
    global key_ #definimos la copia de clave como global
    
    print(key_) #imprimimos la copia de la llave
    path = root.filename.name #verificamos la ruta del archivo
    f = open(path,"rb") #iniciamos la operacion con el nombre del archivo
    data = f.read() #leemos el archivo
    Mas = Fernet(key_) #con la ayuda de fernet extraemos la clave
    token = Mas.encrypt(data) #integramos la clave al archivo
    
    f.close() #finalizamos la operacion
    done = True #definimos done como verdadero
    i = 0 #la variabke i comenzara en 0
    while done: #mientras la condicion sea verdadera
        name = "Archivo_Encriptado" #definimos el nombre del nuevo archivo
        if os.path.isfile(name): #comparamos si existe un archivo con el mismo nombre
            name = "Archivo_Encriptado "+str(i) #si existe entonces le agregamos un valor extra numeral
        if not os.path.isfile(name): #creamos el nuevo archivo si no existe el mismo nombre
            done = False #definimos done como falso
        else: #si existe el mismo nombre
            i = i + 1 #aumentamos el valor i
    f = open(name,"wb") #iniciamos la operacion con el nombre del archivo
    f.write(token) #añadimos la clave
    f.close() #finalizamos la operacion

rc = 0
a = 0
if(rc == 1):
    color = NEGRO
if(rc == 2):
    color = ROJO
if(rc == 3):
    color = CAFE
if(rc == 4):
    color = AZUL
if(rc == 5):
    color = GRIS
if(rc == 6):
    color = VERDE
if(rc == 7):
    color = AMARILLO

def Savekey(): #clase guardar la clave
    file =  open("keys.cry","w") #iniciamos la operacion para extraer la clave
    file.write(Key_Entry.get()) #extraemos la clave
    file.close() #finalizamos la operacion
def Recuperarkey(): #iniciamos la operacion para extraer la clave
    file = open("keys.cry","r")  #extraemos la clave
    key1 = file.read()  #leemos el documento
    print(key1) #imprimos la clave
    Key_Entry.delete(0,"end") #verificamos si esta vacia
    Key_Entry.config(state=NORMAL) #definimos su estado
    Key_Entry.insert(0,key1[:len(key)+43]) #insertamos la clave
    file.close() #finalizamos la operacion

def openfile(): #clase abrir un archivo
    root.filename = filedialog.askopenfile(initialdir="/Users",title="Seleccionar Archivo",filetypes = (("all files",""),("all files","*.*"))) #ejecutamos el Explorador de Archivos
    if root.filename != None: #vemos si existe el archivo
        print(root.filename.name) #imprimimos el archivo
        i = 0 #la variable i comenzara en 0
        path = "" #la variable path estara vacio
        for c in root.filename.name: #ejecutamos la cantidad de archivos
            
            if i > 36: #vemos si i es mayo a 36
                path = path + "..." #agregamos la variable path
                break #finalizamos
            path = path+c #agragamos a la variable path
            i=i+1 #aumentamos la variable i
        
        Path_Varible.set("File:  "+path) #verificamos los archivos
        Decrypt_buton.config(state=NORMAL) #definimos el boton para la clase Desencriptar
        Encrypt_buton.config(state=NORMAL) #definimos el boton para la clase Encriptar
        
    else: #caso contrario a la condicion
        Path_Varible.set("File: ") #verificamos los archivos
        Decrypt_buton.config(state=DISABLED) #definimos el boton para la clase Desencriptar
        Encrypt_buton.config(state=DISABLED) #definimos el boton para la clase Encriptar



root = Tk() #generamos un ventana
root.title("Encriptador y Desencriptador SIN-811") #titulo de la ventana
Path_Varible = StringVar() #Definimos una variable
Path_Varible2 = StringVar() #Definimos una variable
Path_Varible3 = StringVar() #Definimos una variable
Path_Varible4 = StringVar() #Definimos una variable
root.resizable(width=False, height=False) #definimos el ancho y la altura
root.geometry("400x300") #dimension de la ventana

File_Path_Label = ttk.Label(root,textvariable=Path_Varible2) #usamos una variable
File_Path_Label.place(x=100,y=3) #ubicacion del label
Path_Varible2.set("Integrantes: ") #escritura en el label

File_Path_Label = ttk.Label(root,textvariable=Path_Varible3) #usamos una variable
File_Path_Label.place(x=120,y=23) #ubicacion del label
Path_Varible3.set("Quinta Lipe Deyvis") #escritura en el label

File_Path_Label = ttk.Label(root,textvariable=Path_Varible4) #usamos una variable
File_Path_Label.place(x=120,y=43) #ubicacion del label
Path_Varible4.set("Quiñajo Macias Jhonatan Jemio") #escritura en el label

File_Path_Label = ttk.Label(root,textvariable=Path_Varible) #usamos una variable
File_Path_Label.place(x=110,y=83) #ubicacion del label
Path_Varible.set("Ruta del Archivo: ") #escritura en el label

Open_File = ttk.Button(root,text="Abrir",command=openfile) #usamos un boton con el nombre de abrir y su operacion
Open_File.place(x=30,y=80) #ubicacion del boton

Encrypt_buton = ttk.Button(root,text="Encriptar",command=start_encrypt,state=DISABLED) #usamos un boton con el nombre de encriptar y su operacion
Encrypt_buton.place(x=30,y=140,width=160) #ubicacion del boton

Decrypt_buton = ttk.Button(root,text="Desencriptar",command=Start_Decrypt,state=DISABLED) #usamos un boton con el nombre de desencriptar y su operacion
Decrypt_buton.place(x=200,y=140,width=160) #ubicacion del boton

Ramdon_key_buton = ttk.Button(root,text="Clave al Azar",command=ramdom_key) #usamos un boton con el nombre de clave al azar y su operacion
Ramdon_key_buton.place(x=30,y=200) #ubicacion del boton

Key_Entry = ttk.Entry(root) #caja de texto
Key_Entry.place(x=120,y=201,width=240,height=23) #ubicacion de la caja de texto

warn = ttk.Label(text="Si pierde la clave, es posible que el archivo no se recupere") #usamos una variable
warn.place(x=30,y=280) #ubicacion del label

Save_buton = ttk.Button(root,text="Guardar clave, en local",command=Savekey) #usamos un boton con el nombre de Guardar clave, en local y su operacion
Save_buton.place(x=30,y=170,width=160) #ubicacion del boton

Recu_buton = ttk.Button(root,text="Recuperar clave Local",command=Recuperarkey) #usamos un boton con el nombre de Recuperar clave local y su operacion
Recu_buton.place(x=200,y=170,width=160) #ubicacion del boton
root.mainloop() #iniciar la ventana
