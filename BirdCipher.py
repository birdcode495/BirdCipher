


# --------------------------------------------------------------------- BIRDCIPHER -------------------------------------------------------------------------


#                BirdCipher (version 1) is a serious game developed by the Technical Team of the company BirdCode S.A.S., focused on the training 
#                of teachers and students of middle and high school for the construction of basic academic and work skills in software
#                programming using the Python programming language. The workflow and algorithms of the Classroom Research Project
#                contemplate the design, structuring and execution of a set of activities in which STEM conceptual and methodological
#                elements are presented, that integrate theoretical topics of basic development in Python and application practices of  
#                the contents seen, in order to develop the serious game, in which the end user or player must guess numerical data  
#                related to species of birdlife that have been sighted in the territories where the student developers (authors) of 
#                the Serious Game live.


# -------------------------------------------------------------------- BIBLIOGRAFÍA ----------------------------------------------------------------------


#                     * Gobernación de Cundinamarca. Colibríes de Cundinamarca. Bogotá. 2018

#                     * Global Biodiversity Information Facility, GBIF




# ---------------------------------------------------------------------------------------------------------------------------------------------------------




# --------------------------------------- Code development practice in Python using the BirdCode and STEM methodologies -----------------------------------


# --------------------------------------------------------------------- Libraries importing ----------------------------------------------------------------



import tkinter as tk
from tkinter import ttk

#from tkinter import *   # --- Graphical User Interface (GUI) Construction with the Tkinter library

import time  # --- Time functions

from playsound import playsound  # --- Audio reproduction in Python

import random  # --- Library to generate random numbers

from BirdCipher_Images import *

from BirdCipher_Info import BirdCipher_sci

from BirdCipher_Info import BirdCipher_Spanish

from BirdCipher_Info import BirdCipher_english

from BirdCipher_Info import BirdCipher_french

from BirdCipher_Info import BirdCipher_german

from BirdCipher_Info import BirdCipher_chinese

from BirdCipher_Info import BirdCipher_pinyin

from secret_messages import *

from cipher_prac1_caesar import *

from BirdCipher_db import *

import sqlite3

import hashlib

from hash import *

import pyperclip as clipboard




# ------------------------------------------------------ 


BirdCipher_list_k = BirdCipher_list

BirdCipher_sci_k = BirdCipher_sci

BirdCipher_Spanish_k = BirdCipher_Spanish

BirdCipher_english_k = BirdCipher_english

BirdCipher_french_k = BirdCipher_french

BirdCipher_german_k = BirdCipher_german

BirdCipher_chinese_k = BirdCipher_chinese

BirdCipher_pinyin_k = BirdCipher_pinyin

number_species_k = number_species

key_audios_k = key_audios
keys_k = keys
crypto_audios_k = crypto_audios

bird_songs_k = bird_songs




# ---------------------------------------------------------------- Welcome to BirdCode --------------------------------------------------------------------


# ----------------------------- Temas tratados: Función print(), función time.sleep(), función input() y reproducción de audio ----------------------------


playsound('Milvago_chimachima.wav')

match = False

prueba_list_present = [0, 1, 2, 34]


print()
print()
print()
print(" ---------------------------------------------------------------------------------------------------------------------------------------")
print()
print()

print("                                                              WELCOME TO BIRDCIPHER                                             ")
print()
print("                                                  Numerical data guessing of bird biodiversity                                  ")
print()
print()
print(" ---------------------------------------------------------------------------------------------------------------------------------------")


print()
print("  BIRDCIPHER - A SERIOUS GAME TO GUESS THE MAGICAL NUMBERS RELATED TO BIRDS WHICH HAVE BEEN SEEN IN SOME PLACES IN THE WORLD")

print()
playsound("C:/BirdCipher/Audios/VoiceAudios/welcome.mp3")
time.sleep(4)
playsound("C:/BirdCipher/Audios/VoiceAudios/enter_name.mp3")

print()
print()
print(" ----------------------------------------------- Enter your credentials ----------------------------------------------------------------")
print()
print()
print()

username = input("     * Please enter your name: ")
print()

nickname = input("     * Please insert your nickname: ")
print()

password = input("     * Please enter your password: ")
print()

print()
print()
print(" ---------------------------------------------------------------------------------------------------------------------------------------")

bdatos = bytes(password, 'utf-8')
h = hashlib.new(algoritmo, bdatos)
hash1 = HASH.generaHash(h)


def updatePlayer():

	global username
	global nickname
	global password

	if nickname != "":

		miConexion = sqlite3.connect("Players")

		miCursor = miConexion.cursor()

		sql = 'insert into players(name_player, nickname, password) values(?,?,?)'
		data = (username, nickname, hash1)

		miCursor.execute(sql, data)

		miConexion.commit()

		miConexion.close()


updatePlayer()


birdCipher = tk.Tk()

def copy_hash():

	clipboard.copy(hash1)
	playsound('C:/BirdCipher/Audios/VoiceAudios/hash_copied.mp3')

def confidentiality_audio():

	playsound('C:/BirdCipher/Audios/VoiceAudios/confidentiality.mp3')

def integrity_audio():

	playsound('C:/BirdCipher/Audios/VoiceAudios/integrity.mp3')



confidentiality_logo = tk.PhotoImage(file="Confidentiality-logo1.png")
integrity_logo = tk.PhotoImage(file="Integrity-logo1.png")
availability_logo = tk.PhotoImage(file="Availability-logo1.png")
no_repudio_logo = tk.PhotoImage(file="Non-repudiation-logo1.png")
bird_cipher_graphics_logo = tk.PhotoImage(file="Graphics-logo1.png")
games_rules = tk.PhotoImage(file="Game's rules-logo1.png")
close_window_image = tk.PhotoImage(file = "Close window-logo1.png")


birdCipher.title("BirdGuess: A serious game for secret numbers guessing")
birdCipher_frame = tk.Frame(birdCipher)
birdCipher_frame.pack()
birdCipher_image = tk.PhotoImage(file = "BirdCipher-logo1.png")
birdCipherLabel = tk.Label(birdCipher_frame, image = birdCipher_image)
birdCipherLabel.pack(padx = 50)
#birdCipherLabel.place(x = 20, y = 0)

birdCipher_audio = tk.Button(birdCipher_frame, image = games_rules, command = lambda:confidentiality_audio())
birdCipher_audio.place(x = 20, y = 120)
birdCipher_audio.config(fg = '#320fec')

confidentiality = tk.Button(birdCipher_frame, image = confidentiality_logo, command = lambda:confidentiality_audio())
confidentiality.place(x = 20, y = 220)
confidentiality.config(fg = '#320fec')

integrity = tk.Button(birdCipher_frame, image = integrity_logo, command = lambda:integrity_audio())
integrity.place(x = 20, y = 320)
integrity.config(fg = '#320fec')

availability = tk.Button(birdCipher_frame, image = availability_logo, command = lambda:_audio())
availability.place(x = 20, y = 420)
availability.config(fg = '#320fec')

no_repudio = tk.Button(birdCipher_frame, image = no_repudio_logo, command = lambda:no_repudio_audio())
no_repudio.place(x = 20, y = 520)
no_repudio.config(fg = '#320fec')

birdCipher_graphic = tk.Button(birdCipher_frame, image = bird_cipher_graphics_logo, command = lambda:bc_graphics())
birdCipher_graphic.place(x = 20, y = 20)
birdCipher_graphic.config(fg = '#320fec')

close_window = tk.Button(birdCipher_frame, image = close_window_image, command = lambda:birdCipher.destroy())
close_window.place(x = 20, y = 605)

name_player = tk.Label(birdCipher_frame, text = "Welcome to BirdCipher, {} ".format(nickname), font = ("Comic Sans MS", 13))
name_player.place(x = 530, y = 20)
name_player.config(fg = '#ec40e1', bg = '#050505')

hash_player = tk.Label(birdCipher_frame, text = hash1, font = ("Comic Sans MS", 11))
hash_player.config(bg = '#050505', fg = '#ec40e1')
hash_player.place(x = 180, y = 650)

hash_copy = tk.Button(birdCipher_frame, text = "Copy", font = ("Comic Sans MS", 11), command = lambda:copy_hash())
hash_copy.place(x = 760, y = 645)
hash_copy.config(fg = '#5f0659')

label_hash = tk.Label(birdCipher_frame, text ="Your password hash (SHA 256)", font = ("Comic Sans MS", 13))
label_hash.place(x = 180, y = 607)
label_hash.config(fg = '#5f0659')

birdCipher.mainloop()



print()

print("     Welcome to BirdCipher ", username,  "!!! Now, let us learn more about the groups of birds in the world, so that we can identify them easier.")

time.sleep(3)

playsound("C:/BirdCipher/Audios/VoiceAudios/species_info.mp3")

index = 890

def IndexCreation():

	global index

	#index = random.randint(0, len(BirdCipher_list_k) - 1)
	index = random.choice(prueba_list_present)
	

IndexCreation()


# ------------------------------------------------------------ Creation of graphical interfaces ------------------------------------------------------------


# -----------------------------------------Temas tratados: Creación inicial de interfaz gráfica y reproducción de audio con Python ----------------------

# ----- Recordar que se deben eliminar las funciones de reproduccion porque eso es parte del reto


# raiz_cundi = tk.Tk()

# def MapWindow():

# 	mapCundi = Toplevel(raiz_cundi)
# 	mapCundi.title("Map of Cundinamarca")
# 	mapCundi.geometry("1700x1700")

# 	mapLabel = Label(mapCundi, image = CundinamarcaImg)
# 	mapLabel.pack()
# 	mapLabel.image = CundinamarcaImg


# def MainChallenge():

# 	playsound("main_challenge.mp3")
# 	time.sleep(20)
# 	playsound("reto_principal.mp3")

	

# raiz_cundi.title("Cundinamarca")
# raiz_cundi.geometry("800x500")
# miFrame_cundi = Frame(raiz_cundi)
# miFrame_cundi.pack()
# mainChallenge = PhotoImage(file = "Main Challenge1.png")
# Label(miFrame_cundi, image = mainChallenge).pack()



# miFrame_MapWindow = Frame(raiz_cundi)
# miFrame_MapWindow.pack()
# CundinamarcaImg = PhotoImage(file = "Cundinamarca9.png")

# mapButton = tk.Button(raiz_cundi, text = "Cundinamarca Map", font = ("Comic Sans MS", 13), command = lambda:MapWindow())
# mapButton.config(fg = "#320fec")
# mapButton.place(x = 30, y = 400)

# infoButton = tk.Button(raiz_cundi, text = "Main Challenge", font = ("Comic Sans MS", 13), command = lambda:MainChallenge())
# infoButton.config(fg = "#320fec")
# infoButton.place(x = 400, y = 400)

# raiz_cundi.mainloop()



# def Challenge2():

# 	def DevelopmentChallenge2():

# 		playsound("DevelopmentChallenge2.mp3")


# 	def Close():

# 		raiz_challng2.destroy()

	
# 	raiz_challng2 = tk.Tk()

# 	raiz_challng2.title("Challenge 2")

# 	raiz_challng2.geometry("600x400")

# 	raiz_challng2.iconbitmap()

# 	miFrame_challng2 = Frame(raiz_challng2)

# 	miFrame_challng2.pack()

# 	miImagen_challng2 = PhotoImage(file = "Challenge 2abcd.png")

# 	Label(miFrame_challng2, image = miImagen_challng2).pack()

# 	DevelopChallenge2 = tk.Button(raiz_challng2, text = "Bird Singing - Development Challenge", font = ("Comic Sans MS", 13), command = lambda:DevelopmentChallenge2())
# 	DevelopChallenge2.config(fg = "#fa7704")
# 	DevelopChallenge2.place(x = 80, y = 300)

# 	CloseWindow = tk.Button(raiz_challng2, text = "Close window", font = ("Comic Sans MS", 13), command = lambda:Close())
# 	CloseWindow.config(fg = "#fa7704")
# 	CloseWindow.place(x = 450, y = 300)
		
# 	raiz_challng2.mainloop()

count = 0

def GUI_Creation():

	global count

	global match

	global index

	raiz = tk.Tk()

	raiz.title(BirdCipher_english_k[index])

	raiz.iconbitmap()

	miFrame = tk.Frame(raiz)

	miFrame.pack()

	miImagen = tk.PhotoImage(file = BirdCipher_list_k[index][0])
	arrow = tk.PhotoImage(file = "arrow1.png")
	bird_singing_logo = tk.PhotoImage(file="Singing-logo5.png")

	imageLabel = tk.Label(miFrame, image=miImagen)
	imageLabel.pack()
	

	Button = tk.Button(raiz, text = "Close Window", font = ("Comic Sans MS", 8), command = raiz.destroy)
	Button.config(fg = "#fa7704")
	Button.place(x = 20, y = 200)

	Button_song = tk.Button(raiz, image = bird_singing_logo, command = lambda:bird_singing())
	Button_song.place(x = 20, y = 20)

	change_image = tk.Button(raiz, image = arrow, command = lambda:change_image_bird())
	change_image.place(x = 20, y = 115)


	def bird_singing():

		if match == False:

			playsound("C:/BirdCipher/Audios/VoiceAudios/ableHearSong.mp3")

		elif match == True:

			playsound(bird_songs_k[index])

	def change_image_bird():

		global count
		global miImagen
		global index

		playsound('cartoon130.mp3')
		miImagen = tk.PhotoImage(file = BirdCipher_list_k[index][count + 1])
		imageLabel.config(image = miImagen)
		imageLabel.pack()
		count = count + 1

		if count == len(BirdCipher_list_k[index]) - 1:

			count = -1

	

	raiz.mainloop()


# def Challenge3():

# 	def DevelopmentChallenge3():

# 		playsound("DevelopmentChallenge3.mp3")

# 	raiz_challng3 = tk.Tk()

# 	raiz_challng3.title("Challenge 3")

# 	raiz_challng3.geometry("600x400")

# 	raiz_challng3.iconbitmap()

# 	miFrame_challng3 = Frame(raiz_challng3)

# 	miFrame_challng3.pack()

# 	miImagen_challng3 = PhotoImage(file = "Challenge 3a.png")

# 	Label(miFrame_challng3, image = miImagen_challng3).pack()

# 	DevelopmentChallenge = tk.Button(raiz_challng3, text = "Development Challenge", font = ("Comic Sans MS", 13), command = lambda:DevelopmentChallenge3())
# 	DevelopmentChallenge.config(fg = "#a9a70a")
# 	DevelopmentChallenge.place(x = 50, y= 300)

# 	raiz_challng3.mainloop()


def caesarCipher():

	def CaesarExplanat():

		playsound("CaesarCipherExplanation0A.mp3")
		
	
	def CaesarExplanat2():

		playsound("CaesarCipherExplanation0B.mp3")

	def CaesarExplanat3():

		playsound("CaesarCipherExplanation1.mp3")

	def CaesarExplanat4():

		playsound("CaesarCipherExplanation2.mp3")

	def CaesarExplanat5():

		playsound("CaesarCipherExplanation3.mp3")

	def CaesarChallenge():

		playsound("CaesarChallenge.mp3")

		

	caesar_cipher = tk.Tk()
	caesar_cipher.title("Caesar Cipher")
	caesar_cipher_frame = tk.Frame(caesar_cipher)
	caesar_cipher_frame.pack()
	caesar_cipher_image = tk.PhotoImage(file = "ImplementTheCaesarCipherInPython.png")
	labelCaesarPhoto = tk.Label(caesar_cipher_frame, image = caesar_cipher_image)
	labelCaesarPhoto.pack()

	CaesarExplanation = tk.Button(caesar_cipher, text = "Introduction", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat())
	CaesarExplanation.config(fg = "#a9a70a")
	CaesarExplanation.place(x = 1100, y = 50)

	CaesarExplanation2 = tk.Button(caesar_cipher, text = "Presentation", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat2())
	CaesarExplanation2.config(fg = "#a9a70a")
	CaesarExplanation2.place(x = 1100, y = 100)

	CaesarExplanation3 = tk.Button(caesar_cipher, text = "Justification", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat3())
	CaesarExplanation3.config(fg = "#a9a70a")
	CaesarExplanation3.place(x = 1100, y = 150)

	CaesarExplanation4 = tk.Button(caesar_cipher, text = "History and use", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat4())
	CaesarExplanation4.config(fg = "#a9a70a")
	CaesarExplanation4.place(x = 1090, y = 200)

	CaesarExplanation5 = tk.Button(caesar_cipher, text = "Applications", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat5())
	CaesarExplanation5.config(fg = "#a9a70a")
	CaesarExplanation5.place(x = 1100, y = 250)

	CaesarExplanation6 = tk.Button(caesar_cipher, text = "Challenges", font = ("Comic Sans MS", 13), command = lambda:CaesarChallenge())
	CaesarExplanation6.config(fg = "#a9a70a")
	CaesarExplanation6.place(x = 1100, y = 300)

	caesar_cipher.mainloop()


# def Challenge_1():

# 	def DataPrint():

# 		playsound("DataPrintChallenge1.mp3")


# 	def DevelopmentChallenge1():

# 		playsound("DevelopmentChallenge1.mp3")

# 	def TrilingualismChallenge1():

# 		playsound("TrilingualismChallenge1.mp3")


# 	def Close():

# 		raiz_challng1.destroy()


# 	raiz_challng1 = tk.Tk()

# 	raiz_challng1.title("Challenge 1")

# 	raiz_challng1.geometry("500x450")

# 	raiz_challng1.iconbitmap()

# 	miFrame_challng1 = Frame(raiz_challng1)

# 	miFrame_challng1.pack()

# 	miImagen_challng1 = PhotoImage(file = "Challenge 1a.png")

# 	Label(miFrame_challng1, image = miImagen_challng1).pack()


# 	DataPrintChallenge = tk.Button(raiz_challng1, text = "Data Print Challenge", font = ("Comic Sans MS", 13), command = lambda:DataPrint())
# 	DataPrintChallenge.config(fg = "#228a08")
# 	DataPrintChallenge.place(x = 40, y = 330)

# 	DevelopmentChallenge = tk.Button(raiz_challng1, text = "Development Challenge", font = ("Comic Sans MS", 13), command = lambda:DevelopmentChallenge1())
# 	DevelopmentChallenge.config(fg = "#228a08")
# 	DevelopmentChallenge.place(x = 40, y= 380)

# 	TrilingualismChallenge = tk.Button(raiz_challng1, text = "Trilingualism Challenge", font = ("Comic Sans MS", 13), command = lambda:TrilingualismChallenge1())
# 	TrilingualismChallenge.config(fg = "#228a08")
# 	TrilingualismChallenge.place(x = 280, y = 330)
	
# 	CloseButton = tk.Button(raiz_challng1, text = "Close window", font = ("Comic Sans MS", 13), command = lambda:Close())
# 	CloseButton.config(fg = "#228a08")
# 	CloseButton.place(x = 280, y = 380)


# 	raiz_challng1.mainloop()


# def Challenge345():

# 	raiz_challng2 = tk.Tk()

# 	raiz_challng2.title("Challenge 2")

# 	raiz_challng2.iconbitmap()

# 	miFrame_challng2 = Frame(raiz_challng2)

# 	miFrame_challng2.pack()

# 	miImagen_challng2 = PhotoImage(file = "Challenge 2a.png")

# 	Label(miFrame_challng2, image = miImagen_challng2).pack()

# 	raiz_challng2.mainloop()


GUI_Creation()

#Challenge2()



# ---------------------------------------------------------------- Declaration of variables ---------------------------------------------------------------


# -------------------------- Temas tratados: Declaración de variables en Python, tipos de datos y operadores aritméticos y de asignación ------------------


'''

scientific_name = "Eriocnemis cupreoventris"

family = "Trochilidae"

bird_name = "Coppery-bellied Puffleg"

spanish_name = "Calzadito cobrizo"

french_name = "Érione à ventre cuivré"

german_name = "Kupferbauch-Schneehöschen"

chinese_bird_name = "铜腹毛腿蜂鸟"

pinyin = "Tóng fù máo tuǐ fēngniǎo"

size = 9.7

feeding = "nectar"

habitat = "high Andean forest and paramo"

distribution = "almost endemic"

min_altitude_msnm = 1950

max_altitude_msnm = 3200

mean_altitude_msnm = (max_altitude_msnm + min_altitude_msnm) / 2

length_beak_mm = 18

conservacion = "Near Threatened" 

migration = False

'''


# -------------------------------------------------------- Bird Species Information Printing --------------------------------------------------------------


# ---------------------- Temas tratados: Potencialidad de la función print(), función time.sleep(), concatenación de cadenas de caracteres-----------------


# -------------------------------------------------------- CHALLENGE 1: Printing species data via console ---------------------------------------------

#                        Student groups must research each species of bird in the Accipitridae and Trochilidae families
#                        in the GBIF portal and other sources and create new prints of the information consulted by declaring
#                        the corresponding variables within the data list  of species built in the BirdGuess_information.py 
#                        module with the aim of enriching the  final player's experience (public) and offer training to them
#                        on the topic of biodiversity of birds present in the territory where the students reside, which is the
#                        geographical context of the educational community of the school that is implementing this BirdGuess 
#                        Project and that can become a tourism-friendly school and receive visitors from Colombia and the world.

#                        The information initially included in the BirdGuess_data list created in the BirdGuess_information.py 
#                        Module comprises the trilingualism component with the common names of each species integrated into the
#                        BirdGuess_list of the Image Module in Spanish, English, French, German and Mandarin Chinese. The additional
#                        data that each group of developer students may be related to food, ecology, habitat, maximum, minimum and 
#                        average altitude, geographical distribution, anatomy, state of conservation, etc. ..........

#                        Note: The order of creation of each item within the BirdGuess_data lists must match the order of the list
#                        images of the list of species integrated into the BirdGuess_Images.py Module
#                        

# ---------------------------------------------------------------------------------------------------------------------------------------------------------




def info_display():

	playsound("C:/BirdCipher/Audios/VoiceAudios/vernacularNames.mp3")
	time.sleep(4)

	print()
	print("-------------------------------------------------- BIRDS INFORMATION --------------------------------------------------------------")
	print()
	print()
	playsound("idea-1.mp3")
	print("     * The scientific name of this order of birds is: ", BirdCipher_sci_k[index])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The english name of this order of birds is: ", BirdCipher_english_k[index])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The spanish name of this order of birds is: ", BirdCipher_Spanish_k[index])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The french name of this order of birds is: ", BirdCipher_french_k[index])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The german name of this order of birds is: ", BirdCipher_german_k[index])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The chinese name of this order of birds is: ", BirdCipher_chinese_k[index]) 
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The pinyin (chinese phonetic transcription system) is: ", BirdCipher_pinyin_k[index]) 
	print()
	time.sleep(1)
	# playsound("idea-1.mp3")
	# print("     * The secret message about this species is: ")
	# print()
	# print("     ", secret_messages[index])
	# time.sleep(3)
	
info_display()

#Challenge_1()

'''

time.sleep(5)
print("This birds habitat is: ", habitat)
print()
time.sleep(5)
print("The distribution of this hummingbird is: ", distribution)
print()
time.sleep(5)
print("The minimun altitude where we can find this bird is: ", min_altitude_msnm, " msnm")
print()
time.sleep(5)
print("The maximun altitude where we can find this bird is: ", max_altitude_msnm, " msnm")
print()
time.sleep(5)
print("The mean altitude where this bird dwells is: ", mean_altitude_msnm, " msnm")
print()
time.sleep(5)
print("The birds beak length is: ", length_beak_mm, " mm")
print()
time.sleep(5)
print("The conservation state of this bird according to the IUCN is: ", conservacion)
print()
time.sleep(5)
print("The ", bird_name, " is an emblematic species of Colombia. Migration: ", migration)
print()
time.sleep(5)
print("The type of the object 'bird_name' is: ", type(bird_name))
print()
time.sleep(5)
print("The type of the object 'max_altitude_msnm' is: ", type(max_altitude_msnm))
print()
time.sleep(5)
print("The type of the object 'mean_altitude_msnm' is: ", type(mean_altitude_msnm))
print()
time.sleep(5)
print("The type of the object 'migration' is: ", type(migration))
time.sleep(5)
print()
print()

'''

# -------------------------------------------- BirdGuess Game development "Guess the size of the bird in centimeters" ------------------------------------


# -------------------------------------- Temas tratados: Función input() o entrada de datos por consola, Condicionales y bucles --------------------------


# ------------------------------------------------ DINÁMICA DE DESARROLLO DEL JUEGO DE ADIVINANZAS DE TAMAÑOS DE AVES ------------------------------------

#                      El estudiante debe pensar como crear las pantallas en las que el jugador debe adivinar el tamaño del ave dentro del elenco de especies
#                      construido. Cada vez que el jugador adivine el tamaño de una especie el juego debe continuar, eliminando dentro de la lista la especie
#                      cuyo tamaño ha sido adivinada y ofreciendo al jugador una pantalla siguiente para adivinar el tamaño de otra especie 
#                      dentro de la lista restante. 

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------- RETO 2 ---------------------------------------------------------------------------

#                      Ampliar el reto para el jugador de modo que adivine otros datos numéricos de cada especie dentro de cada pantalla
#                      y ofrecer un estímulo a éste por medio de obtención de puntos, monedas, diamantes, etc. que defina el progreso
#                      o fracaso del jugador y lo invite a pasar los retos de conocimiento sobre biodiversidad que definirán el avance
#                      del usuario dentro del juego.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------- RETO 3 ---------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------------------------------------------------------

secretNumber = number_species_k[index]


print()
print("---------------------- BIRDCIPHER - BIRD BIODIVERSITY SECRET NUMBERS GUESSING. LETS PLAY NOW!!! ---------------------------------------")
print()
#time.sleep(3)


playsound("WelcomeSecretNumbers.mp3")
playsound("try_guess.mp3")

print("   Guess the number of species of the group: ", BirdCipher_english_k[index])  # --- Trabaje en el RETO 2

guess = 0

def question():

	global guess

	while True:

		try:
			print()
			guess = input("   * Enter the number of species: ")
			guess = int(guess)
			break

		except ValueError:

			print("   * You must enter a valid value. Try again.")
			


chances_decrypt = 0

def GUI_BirdCipher_Machine():

	global key
	global message
	global keys
	global chances_decrypt
	global crypto_audios_k
	global points
	global nickname
	global BirdCipher_sci_k
	global match

	def comd_decrypt():

		global key
		global keys
		global message
		global chances_decrypt
		global match

		message = secret_messages[index]
		key = player_answer_decrypt.get()
		

		if chances_decrypt <= 3 and key == keys[index]:

			playsound('C:/BirdCipher/Audios/VoiceAudios/CorrectKey.mp3')
			cipher_text.config(text = getTranslatedMessage(message, key), font = ("Comic Sans MS", 10))
			cipher_text.config(bg = '#050005', fg = '#7e086c')
			match = True
			

		elif chances_decrypt <= 3 and key!= keys[index]:

			playsound('C:/BirdCipher/Audios/VoiceAudios/WrongKey.mp3')
			cipher_text.config(text = getTranslatedMessage(message, key), font = ("Comic Sans MS", 10))
			cipher_text.config(bg = '#050005', fg = '#FFFFFF')
			chances_decrypt = chances_decrypt + 1

		elif chances_decrypt > 3:

			playsound('C:/BirdCipher/Audios/VoiceAudios/chances_decrypt.mp3')


	def listen_decrypt_text():

		global key
		global keys
		global chances_decrypt
		global crypto_audios_k
		global match

		key = player_answer_decrypt.get()

		if match == True and chances_decrypt <= 3:

			playsound(crypto_audios_k[index])

		elif match == False and chances_decrypt <= 3:
			
			playsound('C:/BirdCipher/Audios/VoiceAudios/WrongKey.mp3')

		elif chances_decrypt > 3:

			playsound('C:/BirdCipher/Audios/VoiceAudios/chances_decrypt.mp3')

	def audioPoints():

		playsound()

	def coinsAudio():

		playsound()

	def feathersAudio():

		playsound()

	def diamondsAudio():

		playsound()

	def closeMachine():

		global chances_decrypt
		global match

		chances_decrypt = 0
		
		decrypt.destroy()
		


	decrypt = tk.Tk()

	decrypt.title("BirdCipher Cryptographic Machine")
	decrypt.geometry('1050x520')

	#raiz.iconbitmap()

	#decrypt_frame = tk.Frame(decrypt)

	#decrypt_frame.pack()

	player_answer_decrypt = tk.IntVar()

	#miImagen = tk.PhotoImage(file = BirdCipher_list_k[2][0])
	#bird_singing_logo = tk.PhotoImage(file="Singing-logo5.png")

	decrypt_buttonImg = tk.PhotoImage(file = "Decrypt Message-logo1.png")
	listen_buttonImg = tk.PhotoImage(file = "Listen to the message-logo1.png")

	#imageLabel = tk.Label(miFrame, image=miImagen)
	#imageLabel.pack()

	cipher_text = tk.Label(decrypt, text = secret_messages[index], font = ("Comic Sans MS", 10), justify = 'center')
	#cipher_text.place(x = 30, y = 30)
	#cipher_text.pack(pady = 30)
	cipher_text.config(bg = '#050005', fg = '#FFFFFF', padx = 30)
	cipher_text.place(x = 60, y = 40)


	nicknameCuad = tk.Entry(decrypt, textvariable=player_answer_decrypt, font = ("Comic Sans MS", 13), justify = "center")
	#nicknameCuad.config(bg="black", fg="green")
	#nicknameCuad.place(x=50, y=55)
	#nicknameCuad.pack(padx = 30, pady = 30)
	nicknameCuad.config(bg = '#050005', fg = '#7e086c')
	nicknameCuad.place(x = 790, y = 100)
	

	decrypt_button = tk.Button(decrypt, image = decrypt_buttonImg, font = ("Comic Sans MS", 8), command = lambda:comd_decrypt())
	decrypt_button.config(fg = '#1af017')
	decrypt_button.place(x = 800, y = 150)
	
	#decrypt_button.pack()

	decrypt_listen = tk.Button(decrypt, image = listen_buttonImg, font = ("Comic Sans MS", 8), command = lambda:listen_decrypt_text())
	decrypt_listen.config(fg = '#1af017')
	decrypt_listen.place(x = 900, y = 150)
	
	#decrypt_listen.pack()


	imagen_caesar_cipher = tk.PhotoImage(file = 'Imagen_caesar.png')
	imagePoints = tk.PhotoImage(file = "Points-logo1.png")
	imageCoins = tk.PhotoImage(file = "Gold Coins-logo1.png")
	imageFeathers = tk.PhotoImage(file = "Feather-logo1.png")
	imageDiamonds = tk.PhotoImage(file = "Diamond-logo1.png")
	cryptoMachineImage = tk.PhotoImage(file = "Cryptographic Machine-logo1.png")

	imagen_caesar_cipher_lab = tk.Label(decrypt, image = imagen_caesar_cipher)
	#imagen_caesar_cipher_lab.config(bg = '#FFFFFF')
	imagen_caesar_cipher_lab.place(x = 30, y = 300)

	titleBirdCipherMachine = tk.Label(decrypt, text = "BirdCipher message about {} encrypted with the Caesar Cipher algorithm".format(BirdCipher_sci_k[index]), font = ("Comic Sans MS", 12))
	titleBirdCipherMachine.config(fg = "#7e086c")
	titleBirdCipherMachine.place(x = 70, y = 8)

	buttonPoints = tk.Button(decrypt, image = imagePoints, command = lambda:pointsAudio())
	buttonPoints.place(x = 210, y = 300)

	buttonCoins = tk.Button(decrypt, image = imageCoins, command = lambda:coinsAudio())
	buttonCoins.place(x = 300, y = 300)

	buttonFeathers = tk.Button(decrypt, image =imageFeathers, command = lambda:feathersAudio())
	buttonFeathers.place(x = 400, y = 300)

	buttonDiamonds = tk.Button(decrypt, image = imageDiamonds, command = lambda:diamondsAudio())
	buttonDiamonds.place(x= 500, y = 300)

	labelPoints = tk.Label(decrypt, text = points, font = ("Comic Sans MS", 13), justify = "center", width = 6)
	labelPoints.config(bg = "#050005", fg = "#7e086c")
	labelPoints.place(x = 210, y = 410)

	labelCoins = tk.Label(decrypt, text = "", font = ("Comic Sans MS", 13), justify = "center")
	labelCoins.config(bg = "#7e086c")
	labelCoins.place(x = 300, y = 410)

	labelFeathers = tk.Label(decrypt, text = "", font = ("Comic Sans MS", 13), justify = "center")
	labelFeathers.config(bg = "#7e086c")
	labelFeathers.place(x = 400, y = 410)


	labelDiamonds = tk.Label(decrypt, text = "", font = ("Comic Sans MS", 13), justify = "center")
	labelDiamonds.config(bg = "#7e086c")
	labelDiamonds.place(x = 500, y = 410)

	labelQuestionKey = tk.Label(decrypt, text = "Enter the secret key", font = ("Comic Sans MS", 13))
	labelQuestionKey.config(fg = "#7e086c")
	labelQuestionKey.place(x = 805, y = 60)

	labelPlayerBCM = tk.Label(decrypt, text = "Welcome, {} ".format(nickname), font = ("Comic Sans MS", 11))
	labelPlayerBCM.config(fg = "#7e086c", bg = "#050005")
	labelPlayerBCM.place(x = 830, y = 20)

	imageCryptographicMachine = tk.Label(decrypt, image = cryptoMachineImage)
	imageCryptographicMachine.place(x = 750, y = 260)

	closeMachineButton = tk.Button(decrypt, text = "Close the BirdCipher Cryptographic Machine", font = ("Comic Sans MS", 12), command = lambda:closeMachine())
	closeMachineButton.place(x = 250, y = 460)
	closeMachineButton.config(fg = "#7e086c")

	decrypt.protocol("WM_DELETE_WINDOW", lambda: None)


	decrypt.mainloop()


print()

attempts = 1

lives = 4

End = False

points = 0

coins = 0

win_challenge2_info = 0

question()


while End == False or lives > 0:

	#if win_challenge2_info == 0:

		#Challenge_2()
		#win_challenge2_info = 1

	if guess != secretNumber and attempts == 7 and lives > 1:

		print()
		print("------------------------------------------------- RESULTS --------------------------------------------------------")
		print()
		playsound("Lost_a_life.mp3")
		print("   You have tried 7 times and have not been able to guess the size of this bird. You lost a life.")
		print()
		lives = lives - 1
		print("   Now you have: ", lives, " lives")
		IndexCreation()
		secretNumber = number_species_k[index]
		attempts = 0
		print()
		print()
		time.sleep(3)
		GUI_Creation()
		info_display()
		print()
		print("-------------------------- BIRDGUESS - DATA GUESSING OF BIRD BIODIVERSITY. LETS PLAY NOW!!!----------------------")
		print()
		print("   Guess the number of species corresponding to the group: ", BirdCipher_english_k[index])
		print()
		playsound("try_guess.mp3")
		#guess = float(input("   Enter the number of species: "))
		question()
		print()
		attempts = attempts + 1

	elif guess != secretNumber and attempts == 7 and lives == 1:

		print()
		print("-------------------------------------------------- RESULTS ------------------------------------------------------")
		print()
		print("   Now you have no lives. Game over")
		lives = lives - 1
		break
		

	elif guess < secretNumber:

		playsound("larger.mp3")
		print("   * There are more species in this group (order) of birds. Try again.")
		question()
		print()
		attempts = attempts + 1
		

	elif guess > secretNumber:

		playsound("smaller.mp3")
		print("   * There are fewer species in this group (order) of birds. Try again: ")
		question()
		print()
		attempts = attempts + 1
		

	elif guess == secretNumber and attempts <= 7 and len(BirdCipher_list_k) > 1:

		points = points + 10
		print()
		print("---------------------------------------------------- RESULTS -----------------------------------------------------")
		print()
		print("   Congratulations!!! You guessed the total number of species of this group. You have earned 10 points!!!")
		print()
		print("   Now you have: ", points, " points.")
		#hit = True
		playsound("Congratulations.mp3")
		time.sleep(8)
		print()
		print()
		print()
		print("---------------------------------- DECRYPT THE SECRET MESSAGE ABOUT THIS GROUP OF BIRDS!!!! -----------------------------")
		print()
		print()
		time.sleep(3)
		print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		playsound("radar-ufo.mp3")
		playsound("sonar-radar.mp3")
		time.sleep(3)
		caesarCipher()
		playsound("DecipherMessage.mp3")
		print()
		print("                                                 ", BirdCipher_sci_k[index], "                                          ")
		print()
		time.sleep(3)
		print("                                             ", BirdCipher_english_k[index], "                                          ")
		print()
		time.sleep(3)
		print("                                                 Caesar Cipher Algorithm                                                ")
		time.sleep(3)
		print()
		print("                                                 Simetrical cryptography                                                ")
		time.sleep(3)
		print()
		print("                                      Here comes the BirdCipher Cryptographic Machine                                    ")
		print()
		print()
		print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

		playsound('MessageClueObtained.mp3')
		playsound(key_audios_k[index])
		time.sleep(2)
		playsound('WriteTheClue.mp3')
		# here comes the GUI_BirdCipher Machine
		#key = getKey()

		GUI_BirdCipher_Machine()

		#print("Prueba GUI BirdCipher Machine")

		# if isinstance(key, str):

		# 	print("        Incorrect data type")

		if key == keys_k[index]:

			playsound("rightDecrypt.mp3")
			playsound("GoldCoin.mp3")
			time.sleep(2)
			playsound("seePictureAgain.mp3")
			
			GUI_Creation()

			

		# 	match = True
			
		# 	print()
		# 	playsound("secretMessageSpecies.mp3")
		# 	time.sleep(2)
		# 	print('        Your translated text is: ')
		# 	print()
		# 	print("       ", getTranslatedMessage(message, key))
		# 	time.sleep(5)
		# 	playsound(crypto_audios_k[2])
		# 	time.sleep(40)
		# 	print()

		# elif key != keys_k[2] and key >= 1 and key <= 26:

		# 	playsound("wrongPassword.mp3")
		# 	print()
		# 	#playsound("secretMessageSpecies.mp3")
		# 	time.sleep(2)
		# 	print('        Your translated text is: ')
		# 	print()
		# 	print("       ", getTranslatedMessage(message, key))
		# 	time.sleep(5)
		# 	#playsound(crypto_audios_k[2])
		# 	time.sleep(20)
		# 	print()

		# elif key < 1 or key > 26:

		# 	print("        Incorrect value")

				
		
		
		# del BirdCipher_list_k[index]
		# del BirdCipher_sci_k[index]
		# del BirdCipher_Spanish_k[index]
		# del BirdCipher_english_k[index]
		# del BirdCipher_french_k[index]
		# del BirdCipher_german_k[index]
		# del BirdCipher_chinese_k[index]
		# del BirdCipher_pinyin_k[index]
		prueba_list_present.remove(index)
		
		IndexCreation()
		secretNumber = number_species_k[index]
		match = False
		
		#Challenge3()
		GUI_Creation()
		info_display()
		print()
		print()
		print("--------------------- BIRDCIPHER - NUMERICAL DATA GUESSING OF BIRD BIODIVERSITY. LETS PLAY NOW!!! ---------------------")
		print()
		print("   Guess the size in centimeters of: ", BirdCipher_english_k[index])
		attempts = 0
		print()
		playsound("try_guess.mp3")
		question()
		print()
		attempts = attempts + 1

	elif guess == secretNumber and attempts <= 7 and len(BirdCipher_list_k) == 1:

		
		print("--------------------------------------------------- RESULTS -----------------------------------------------------------")
		print()
		print()
		print("   Congratulations!!! You guessed the size of the bird I was thinking of. You have earned 10 points!!!")
		playsound("Congratulations.mp3")
		time.sleep(3)
		playsound("End.mp3")
		points = points + 10
		print()
		print("Now you have: ", points, " points.")
		del BirdCipher_list_k[0]
		print()
		print("Congratulations!!! You have guessed all the sizes of the birds on the list. End of the game.")
		print()
		print()
		print(" -------------------------------------------------------------------------------------------------------------------")
		End = True
		break









# -------------------------------------------------------------------- END OF THE GAME --------------------------------------------------------------------


# ------------------------------------------------------------ Now, let's run this program!!! -------------------------------------------------------------





