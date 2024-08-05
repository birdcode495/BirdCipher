


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




# ---------------------------------------------------------------- Welcome to BirdCode --------------------------------------------------------------------


# ----------------------------- Temas tratados: Función print(), función time.sleep(), función input() y reproducción de audio ----------------------------


playsound('Milvago_chimachima.wav')

match = False

birdCipher = tk.Tk()

birdCipher.title("BirdGuess: A serious game for secret numbers guessing")
birdCipher_frame = tk.Frame(birdCipher)
birdCipher_frame.pack()
birdCipher_image = tk.PhotoImage(file = "BirdCipher-logo.png")
birdCipherLabel = tk.Label(birdCipher_frame, image = birdCipher_image).pack()

birdCipher.mainloop()


print()
print()
print()
print(" -------------------------------------------------------------------------------------------------------------------------------")
print()
print()

print("                                                       WELCOME TO BIRDCIPHER                                                     ")
print()
print("                                           Numerical data guessing of bird biodiversity                                         ")
print()
print()
print(" -------------------------------------------------------------------------------------------------------------------------------")


print()
print("     BIRDCIPHER - A PROGRAM TO GUESS THE SIZES OF FALCONS AND HUMMINGBIRDS THAT HAVE BEEN SEEN IN BOGOTÁ - COLOMBIA")

print()
playsound("welcome.mp3")
playsound("enter_name.mp3")

username = input("     * Please enter your name: ")

nickname = input("     * Please insert your nickname: ")

password = input("     * Please enter your password: ")

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



print()

print("     Welcome to BirdCipher. ", username,  "!!! Now we are going to learn how to develop serious games with Python about colombian biodiversity")

print()

time.sleep(3)

playsound("species_info.mp3")

index = 890

def IndexCreation():

	global index

	index = random.randint(0, len(BirdCipher_list_k) - 1)
	

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

	raiz.title(BirdCipher_english_k[34])

	raiz.iconbitmap()

	miFrame = tk.Frame(raiz)

	miFrame.pack()

	miImagen = tk.PhotoImage(file = BirdCipher_list_k[34][0])
	bird_singing_logo = tk.PhotoImage(file="Singing-logo5.png")

	imageLabel = tk.Label(miFrame, image=miImagen)
	imageLabel.pack()
	

	Button = tk.Button(raiz, text = "Close Window", font = ("Comic Sans MS", 8), command = raiz.destroy)
	Button.config(fg = "#fa7704")
	Button.place(x = 20, y = 115)

	Button_song = tk.Button(raiz, image = bird_singing_logo, command = lambda:bird_singing())
	Button_song.place(x = 20, y = 20)

	change_image = tk.Button(raiz, text = 'Change', command = lambda:change_image_bird())
	change_image.place(x = 20, y = 250)


	def bird_singing():

		if match == False:

			playsound("ableHearSong.mp3")

		elif match == True:

			playsound("Singing_Rupornis_magnirostris.wav")

	def change_image_bird():

		global count
		global miImagen
		global index

		playsound('cartoon130.mp3')
		miImagen = tk.PhotoImage(file = BirdCipher_list_k[34][count + 1])
		imageLabel.config(image = miImagen)
		imageLabel.pack()
		count = count + 1

		if count == len(BirdCipher_list_k[34]) - 1:

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


# def caesarCipher():

# 	def CaesarExplanat():

# 		playsound("CaesarCipherExplanation0A.mp3")
		
	
# 	def CaesarExplanat2():

# 		playsound("CaesarCipherExplanation0B.mp3")

# 	def CaesarExplanat3():

# 		playsound("CaesarCipherExplanation1.mp3")

# 	def CaesarExplanat4():

# 		playsound("CaesarCipherExplanation2.mp3")

# 	def CaesarExplanat5():

# 		playsound("CaesarCipherExplanation3.mp3")

# 	def CaesarChallenge():

# 		playsound("CaesarChallenge.mp3")

		

# 	caesar_cipher = tk.Tk()
# 	caesar_cipher.title("Caesar Cipher")
# 	caesar_cipher_frame = Frame(caesar_cipher)
# 	caesar_cipher_frame.pack()
# 	caesar_cipher_image = PhotoImage(file = "ImplementTheCaesarCipherInPython.png")
# 	Label(caesar_cipher_frame, image = caesar_cipher_image).pack()

# 	CaesarExplanation = tk.Button(caesar_cipher, text = "Introduction", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat())
# 	CaesarExplanation.config(fg = "#a9a70a")
# 	CaesarExplanation.place(x = 1100, y = 50)

# 	CaesarExplanation2 = tk.Button(caesar_cipher, text = "Presentation", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat2())
# 	CaesarExplanation2.config(fg = "#a9a70a")
# 	CaesarExplanation2.place(x = 1100, y = 100)

# 	CaesarExplanation3 = tk.Button(caesar_cipher, text = "Justification", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat3())
# 	CaesarExplanation3.config(fg = "#a9a70a")
# 	CaesarExplanation3.place(x = 1100, y = 150)

# 	CaesarExplanation4 = tk.Button(caesar_cipher, text = "History and use", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat4())
# 	CaesarExplanation4.config(fg = "#a9a70a")
# 	CaesarExplanation4.place(x = 1090, y = 200)

# 	CaesarExplanation5 = tk.Button(caesar_cipher, text = "Applications", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat5())
# 	CaesarExplanation5.config(fg = "#a9a70a")
# 	CaesarExplanation5.place(x = 1100, y = 250)

# 	CaesarExplanation6 = tk.Button(caesar_cipher, text = "Challenges", font = ("Comic Sans MS", 13), command = lambda:CaesarChallenge())
# 	CaesarExplanation6.config(fg = "#a9a70a")
# 	CaesarExplanation6.place(x = 1100, y = 300)

# 	caesar_cipher.mainloop()


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

	print()
	print("-------------------------- BIRD INFORMATION -----------------------------------")
	print()
	playsound("idea-1.mp3")
	print("     * The scientific name of this bird is: ", BirdCipher_sci_k[34])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The english name of this bird is: ", BirdCipher_english_k[34])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The spanish name of this bird is: ", BirdCipher_Spanish_k[34])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The french name of this bird is: ", BirdCipher_french_k[34])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The german name of this bird is: ", BirdCipher_german_k[34])
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The chinese name of this bird is: ", BirdCipher_chinese_k[34]) 
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The pinyin (chinese phonetic transcription system) is: ", BirdCipher_pinyin_k[34]) 
	print()
	time.sleep(1)
	playsound("idea-1.mp3")
	print("     * The secret message about this species is: ")
	print()
	print("       ", secret_messages[10])
	time.sleep(3)
	
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

secretNumber = number_species_k[34]


print()
print("---------------------- BIRDGUESS - BIRD BIODIVERSITY SECRET NUMBERS GUESSING. LETS PLAY NOW!!! ---------------------")
print()
time.sleep(3)


playsound("WelcomeSecretNumbers.mp3")
playsound("try_guess.mp3")

print("   Guess the number of species of the group: ", BirdCipher_english_k[34])  # --- Trabaje en el RETO 2

print()

guess = float(input("   Enter the number of species: "))
print()

attempts = 1

lives = 4

End = False

points = 0

coins = 0

win_challenge2_info = 0


while End == False or lives > 0:

	#if win_challenge2_info == 0:

		#Challenge_2()
		#win_challenge2_info = 1

	if guess != secretNumber and attempts == 7 and lives > 1:

		print()
		print("------------------------------------- RESULTS ----------------------------------------------------")
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
		print("------------------- BIRDGUESS - DATA GUESSING OF BIRD BIODIVERSITY. LETS PLAY NOW!!!----------------------")
		print()
		print("   Guess the number of species corresponding to the group: ", BirdCipher_english_k[34])
		print()
		playsound("try_guess.mp3")
		guess = float(input("   Enter the number of species: "))
		print()
		attempts = attempts + 1

	elif guess != secretNumber and attempts == 7 and lives == 1:

		print()
		print("------------------------------------------- RESULTS ------------------------------------------------------")
		print()
		print("   Now you have no lives. Game over")
		lives = lives - 1
		break
		

	elif guess < secretNumber:

		playsound("larger.mp3")
		guess = float(input("    * There are more species in this group (order) of birds. Try again: "))
		print()
		attempts = attempts + 1
		

	elif guess > secretNumber:

		playsound("smaller.mp3")
		guess = float(input("    * There are fewer species in this group (order) of birds. Try again: "))
		print()
		attempts = attempts + 1
		

	elif guess == secretNumber and attempts <= 7 and len(BirdCipher_list_k) > 1:

		points = points + 10
		print()
		print("-------------------------------------------- RESULTS ----------------------------------------------------")
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
		print("------------------------ DECIPHER THE SECRET MESSAGE ABOUT THIS BIRD!!!! -------------------------------")
		print()
		print()
		playsound("radar-ufo.mp3")
		playsound("sonar-radar.mp3")
		time.sleep(3)
		caesarCipher()
		playsound("DecipherMessage.mp3")
		print("       ", secret_messages[10])
		message = getMessage()
		print()
		playsound('MessageClueObtained.mp3')
		playsound('SecretClue.mp3')
		playsound('WriteTheClue.mp3')
		key = getKey()
		if key == 13:

			match = True
			playsound("rightDecrypt.mp3")
			playsound("GoldCoin.mp3")
			time.sleep(2)
			playsound("seePictureAgain.mp3")
			GUI_Creation()

		else:

			playsound("wrongPassword.mp3")

		print()
		playsound("secretMessageSpecies.mp3")
		time.sleep(2)
		print('        Your translated text is: ')
		print()
		print("       ", getTranslatedMessage(message, key))
		
		time.sleep(70)

		
		print()
		
		match = False
		del BirdCipher_list_k[index]
		del BirdCipher_sci_k[index]
		del BirdCipher_Spanish_k[index]
		del BirdCipher_english_k[index]
		del BirdCipher_french_k[index]
		del BirdCipher_german_k[index]
		del BirdCipher_chinese_k[index]
		del BirdCipher_pinyin_k[index]
		IndexCreation()
		secretNumber = number_species_k[index]
		
		Challenge3()
		GUI_Creation()
		info_display()
		print()
		print()
		print("----------------------- BIRDGUESS - DATA GUESSING OF BIRD BIODIVERSITY. LETS PLAY NOW!!! ---------------------")
		print()
		print("   Guess the size in centimeters of: ", BirdCipher_english_k[index])
		attempts = 0
		print()
		playsound("try_guess.mp3")
		guess = float(input("   Enter the size of the bird: "))
		print()
		attempts = attempts + 1

	elif guess == secretNumber and attempts <= 7 and len(BirdCipher_list_k) == 1:

		
		print("-------------------------------------------- RESULTS ----------------------------------------------------")
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
		End = True
		break









# -------------------------------------------------------------------- END OF THE GAME --------------------------------------------------------------------


# ------------------------------------------------------------ Now, let's run this program!!! -------------------------------------------------------------





