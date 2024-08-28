


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

from cryptography.fernet import Fernet

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


# ----------------------------- Temas tratados: Función print(""), función time.sleep(), función input() y reproducción de audio ----------------------------


#playsound('Milvago_chimachima.wav')



username_db = ''
nickname_db = ''
password_db = ''
target_person = ''
target_person_decrypt = ''
message_sent_decrypt = ''
key_sent_decrypt = ''



points = 0
coins = 0
feathers = 0
diamonds = 0
lifes = 3

login = tk.Tk()
login.title("BirdCipher welcome and login")
login.resizable(0, 0)
login.geometry('900x900')

username = tk.StringVar()
nickname = tk.StringVar()
password = tk.StringVar()

confirmPlyr = False

hash1 = ''
#hash2 = ''

def createPlayer():

	global points
	global coins
	global feathers
	global diamonds
	global lifes
	global username
	global nickname
	global password
	global username_db
	global nickname_db
	global password_db
	global confirmPlyr
	global hash1

	bdatos = bytes(password.get(), 'utf-8')
	h = hashlib.new(algoritmo, bdatos)
	hash1 = HASH.generaHash(h)

	miConexion = sqlite3.connect("BirdCipher_DB.db")

	miCursor = miConexion.cursor()

	#miCursor.execute("CREATE TABLE Players(id integer PRIMARY KEY ASC, username varchar(30), nickname varchar(30), password varchar(256), points integer NOT NULL DEFAULT 0, coins integer NOT NULL DEFAULT 0, feathers integer NOT NULL DEFAULT 0, diamonds integer NOT NULL DEFAULT 0)")

	#miCursor.execute("CREATE TABLE encryptedMessages(id integer PRIMARY KEY ASC, nickname varchar(30), password varchar(256), server varchar(30), actual_message varchar(256))")

	#miCursor.execute("ALTER TABLE encryptedMessages ADD COLUMN key_b varchar(100)")

	sql = 'insert into Players(username, nickname, password, points, coins, feathers, diamonds, lifes) values(?,?,?,?,?,?,?,?)'
	data = (username.get(), nickname.get(), hash1, 0, 0, 0, 0, 3)

	sql2 = 'insert into encryptedMessages(nickname, password) values(?,?)'
	data2 = (nickname.get(), hash1)

	sql3 = 'select * from Players where nickname = (?)'
	data3 = (nickname.get(),)

	miCursor.execute(sql3, data3)
	dt = miCursor.fetchall()

	if len(dt) == 0:

		miCursor.execute(sql, data)
		miCursor.execute(sql2, data2)
		miCursor.execute(sql3, data3)
		records = miCursor.fetchall()
		username_db = records[0][1]
		nickname_db = records[0][2]
		password_db = records[0][3]
		points = records[0][4]
		coins = records[0][5]
		feathers = records[0][6]
		diamonds = records[0][7]
		lifes = records[0][8]
		confirmPlyr = True

		#playsound('PlayerCreated.mp3')

	elif dt[0][8] > 0 and hash1 == dt[0][3]:

		username_db = dt[0][1]
		nickname_db = dt[0][2]
		password_db = dt[0][3]
		points = dt[0][4]
		coins = dt[0][5]
		feathers = dt[0][6]
		diamonds = dt[0][7]
		lifes = dt[0][8]
		confirmPlyr = True

		playsound('PlayerActivated.mp3')

	elif dt[0][8] > 0 and hash1 != dt[0][3]:

		playsound('IncorrectPassword.mp3')


	elif dt[0][8] <= 0:

		playsound('GameOver.mp3')


	miConexion.commit()

	miConexion.close()


def confirmPlayer():

	global confirmPlyr

	if confirmPlyr == True:

		#playsound('completedAuthentication.mp3')
		login.destroy()

	# else:

	# 	playsound('completeAuth.mp3')



birdCipher_image_login = tk.PhotoImage(file = "BirdCipher-logo1.png")
login_logo_image = tk.PhotoImage(file = "Login-logo1.png")
close_window_log = tk.PhotoImage(file = "Close-logo1.png")
birdCipherLabel_login = tk.Label(login, image = birdCipher_image_login)
birdCipherLabel_login.place(x = 50, y = 20)

label_username_login = tk.Label(login, text = "Enter your username", font = ("Comic Sans MS", 13))
label_username_login.config(fg = '#7e086c')
label_username_login.place(x = 40, y = 10)

login_username = tk.Entry(login, textvariable = username, font = ("Comic Sans MS", 13), justify = "center", width = 20)
login_username.config(bg = '#050005', fg = '#7e086c')
login_username.place(x = 20, y = 50)

label_nickname_login = tk.Label(login, text = "Enter your nickname", font = ("Comic Sans MS", 13))
label_nickname_login.config(fg = '#7e086c')
label_nickname_login.place(x = 40, y = 100)

login_nickname = tk.Entry(login, textvariable = nickname, font = ("Comic Sans MS", 13), justify = "center", width = 20)
login_nickname.config(bg = '#050005', fg = '#7e086c')
login_nickname.place(x = 20, y = 140)

label_password_login = tk.Label(login, text = "Enter your password", font = ("Comic Sans MS", 13))
label_password_login.config(fg = '#7e086c')
label_password_login.place(x = 40, y = 190)

login_password = tk.Entry(login, textvariable = password, font = ("Comic Sans MS", 13), justify = "center", width = 20)
login_password.config(bg = '#050005', fg = '#7e086c', show = '*')
login_password.place(x = 20, y = 230)

login_button = tk.Button(login, image = login_logo_image, command = lambda:createPlayer())
login_button.place(x = 90, y = 270)

close_window_login = tk.Button(login, image = close_window_log, command = lambda:confirmPlayer())
close_window_login.place(x = 90, y = 380)

#login.protocol("WM_DELETE_WINDOW", lambda: None)

login.mainloop()


def updatePlayer_points():

	conexion2 = sqlite3.connect("BirdCipher_DB.db")
	cursor2 = conexion2.cursor()

	sql4 = "update Players set (points) = (?) where nickname = (?)"
	datsActs = (points, nickname_db)

	cursor2.execute(sql4, datsActs)
	conexion2.commit()
	conexion2.close()


def updatePlayer_coins():

	conexion3 = sqlite3.connect("BirdCipher_DB.db")
	cursor3 = conexion3.cursor()

	sql5 = "update Players set (coins) = (?) where nickname = (?)"
	datsActs2 = (coins, nickname_db)

	cursor3.execute(sql5, datsActs2)
	conexion3.commit()
	conexion3.close()




match = False

prueba_list_present = [0, 1, 2, 34]

#fg = input("ws: ")


print()
print()
print()
print(" ---------------------------------------------------------------------------------------------------------------------------------------")
print()
print("              ****************************************************************************************************************  ")
print()
print("                                                              WELCOME TO BIRDCIPHER                                             ")
print()
print("                                   A cryptographic serious game for Numerical data guessing of bird biodiversity                ")
print()
print("              ****************************************************************************************************************  ")
print()
print(" ---------------------------------------------------------------------------------------------------------------------------------------")


time.sleep(5)
#playsound("C:/BirdCipher/Audios/VoiceAudios/welcome.mp3")
time.sleep(4)
#playsound("C:/BirdCipher/Audios/VoiceAudios/enter_name.mp3")

print()
print("       BIRDCIPHER - A SERIOUS GAME TO GUESS THE MAGICAL NUMBERS RELATED TO BIRDS WHICH HAVE BEEN SEEN IN SOME PLACES IN THE WORLD")

print()


# print()
# print()
# print(" ----------------------------------------------- Enter your credentials ----------------------------------------------------------------")
# print()
# print()
# print()

# username = input("     * Please enter your name: ")
# print()

# nickname = input("     * Please insert your nickname: ")
# print()

# password = input("     * Please enter your password: ")
# print()

# print()
# print()
# print(" ---------------------------------------------------------------------------------------------------------------------------------------")






birdCipher = tk.Tk()

def copy_hash():

	global hash1

	clipboard.copy(hash1)
	#playsound('C:/BirdCipher/Audios/VoiceAudios/hash_copied.mp3')

#def confidentiality_audio():

	#playsound('C:/BirdCipher/Audios/VoiceAudios/confidentiality.mp3')

#def integrity_audio():

	#playsound('C:/BirdCipher/Audios/VoiceAudios/integrity.mp3')



confidentiality_logo = tk.PhotoImage(file="Confidentiality-logo1.png")
integrity_logo = tk.PhotoImage(file="Integrity-logo1.png")
availability_logo = tk.PhotoImage(file="Availability-logo1.png")
no_repudio_logo = tk.PhotoImage(file="Non-repudiation-logo1.png")
bird_cipher_graphics_logo = tk.PhotoImage(file="Graphics-logo1.png")
games_rules = tk.PhotoImage(file="Game's rules-logo1.png")
close_window_image = tk.PhotoImage(file = "Close window-logo1.png")


birdCipher.title("BirdGuess: A serious game for secret numbers guessing")
birdCipher_frame = tk.Frame(birdCipher)
birdCipher.resizable(0, 0)
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

name_player = tk.Label(birdCipher_frame, text = "Welcome to BirdCipher, {} ".format(nickname_db), font = ("Comic Sans MS", 13))
name_player.place(x = 530, y = 20)
name_player.config(fg = '#ec40e1', bg = '#050505')

hash_player = tk.Label(birdCipher_frame, text = password_db, font = ("Comic Sans MS", 11))
hash_player.config(bg = '#050505', fg = '#ec40e1')
hash_player.place(x = 180, y = 650)

hash_copy = tk.Button(birdCipher_frame, text = "Copy", font = ("Comic Sans MS", 11), command = lambda:copy_hash())
hash_copy.place(x = 760, y = 645)
hash_copy.config(fg = '#5f0659')

label_hash = tk.Label(birdCipher_frame, text ="Your password hash (SHA 256)", font = ("Comic Sans MS", 13))
label_hash.place(x = 180, y = 607)
label_hash.config(fg = '#5f0659')

birdCipher.protocol("WM_DELETE_WINDOW", lambda: None)

birdCipher.mainloop()



print()

print("     Welcome to BirdCipher ", username_db,  "!!! Now, let us learn more about the groups of birds in the world, so that we can identify them easier.")

time.sleep(3)

#playsound("C:/BirdCipher/Audios/VoiceAudios/species_info.mp3")

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

	raiz.resizable(0, 0)

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


	#def bird_singing():

		#if match == False:

			#playsound("C:/BirdCipher/Audios/VoiceAudios/ableHearSong.mp3")

		#elif match == True:

			#playsound(bird_songs_k[index])

	def change_image_bird():

		global count
		global miImagen
		global index

		#playsound('cartoon130.mp3')
		miImagen = tk.PhotoImage(file = BirdCipher_list_k[index][count + 1])
		imageLabel.config(image = miImagen)
		imageLabel.pack()
		count = count + 1

		if count == len(BirdCipher_list_k[index]) - 1:

			count = -1

	raiz.protocol("WM_DELETE_WINDOW", lambda: None)	

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

# 	def CaesarExplanat():

# 		#playsound("CaesarCipherExplanation0A.mp3")
		
	
# 	def CaesarExplanat2():

# 		#playsound("CaesarCipherExplanation0B.mp3")

# 	def CaesarExplanat3():

# 		#playsound("CaesarCipherExplanation1.mp3")

# 	def CaesarExplanat4():

# 		#playsound("CaesarCipherExplanation2.mp3")

# 	def CaesarExplanat5():

# 		#playsound("CaesarCipherExplanation3.mp3")

# 	def CaesarChallenge():

# 		#playsound("CaesarChallenge.mp3")

		

	caesar_cipher = tk.Tk()
	caesar_cipher.title("Caesar Cipher")
	caesar_cipher.resizable(0, 0)

	notebk_caesar = ttk.Notebook(caesar_cipher)
	notebk_caesar.pack(expand=True)

	vr = ttk.Frame(notebk_caesar, width = 1300, height=900)
	vr.pack(fill='both', expand=True)
	notebk_caesar.add(vr, text = "      Caesar Cipher Implementation")

	vr2 = ttk.Frame(notebk_caesar, width = 1300, height=900)
	vr2.pack(fill='both', expand=True)
	notebk_caesar.add(vr2, text = "      Fernet Cipher Implementation")

	caesar_cipher_image = tk.PhotoImage(file = "ImplementTheCaesarCipherInPython.png")
	fernet_cipher_image = tk.PhotoImage(file = "fernet.png")
	labelCaesarPhoto = tk.Label(vr, image = caesar_cipher_image)
	labelCaesarPhoto.pack()

	CaesarExplanation = tk.Button(vr, text = "Introduction", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat())
	CaesarExplanation.config(fg = "#a9a70a")
	CaesarExplanation.place(x = 1100, y = 50)

	CaesarExplanation2 = tk.Button(vr, text = "Presentation", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat2())
	CaesarExplanation2.config(fg = "#a9a70a")
	CaesarExplanation2.place(x = 1100, y = 100)

	CaesarExplanation3 = tk.Button(vr, text = "Justification", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat3())
	CaesarExplanation3.config(fg = "#a9a70a")
	CaesarExplanation3.place(x = 1100, y = 150)

	CaesarExplanation4 = tk.Button(vr, text = "History and use", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat4())
	CaesarExplanation4.config(fg = "#a9a70a")
	CaesarExplanation4.place(x = 1090, y = 200)

	CaesarExplanation5 = tk.Button(vr, text = "Applications", font = ("Comic Sans MS", 13), command = lambda:CaesarExplanat5())
	CaesarExplanation5.config(fg = "#a9a70a")
	CaesarExplanation5.place(x = 1100, y = 250)

	CaesarExplanation6 = tk.Button(vr, text = "Challenges", font = ("Comic Sans MS", 13), command = lambda:CaesarChallenge())
	CaesarExplanation6.config(fg = "#a9a70a")
	CaesarExplanation6.place(x = 1100, y = 300)

	labelFernetPhoto = tk.Label(vr2, image = fernet_cipher_image)
	labelFernetPhoto.pack()


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

	#playsound("C:/BirdCipher/Audios/VoiceAudios/vernacularNames.mp3")
	time.sleep(4)

	print()
	print("-------------------------------------------------- BIRDS INFORMATION --------------------------------------------------------------")
	print()
	print()
	#playsound("idea-1.mp3")
	print("     * The scientific name of this order of birds is: ", BirdCipher_sci_k[index])
	print()
	time.sleep(1)
	#playsound("idea-1.mp3")
	print("     * The english name of this order of birds is: ", BirdCipher_english_k[index])
	print()
	time.sleep(1)
	#playsound("idea-1.mp3")
	print("     * The spanish name of this order of birds is: ", BirdCipher_Spanish_k[index])
	print()
	time.sleep(1)
	#playsound("idea-1.mp3")
	print("     * The french name of this order of birds is: ", BirdCipher_french_k[index])
	print()
	time.sleep(1)
	#playsound("idea-1.mp3")
	print("     * The german name of this order of birds is: ", BirdCipher_german_k[index])
	print()
	time.sleep(1)
	#playsound("idea-1.mp3")
	print("     * The chinese name of this order of birds is: ", BirdCipher_chinese_k[index]) 
	print()
	time.sleep(1)
	#playsound("idea-1.mp3")
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
print("---------------------- BIRDCIPHER - BIRD BIODIVERSITY SECRET NUMBERS GUESSING. LET US PLAY NOW!!! ---------------------------------------")
print()
#time.sleep(3)


#playsound("WelcomeSecretNumbers.mp3")
#playsound("try_guess.mp3")

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

			#playsound('integerNumber.mp3')
			print("   * You must enter an integer number. Try again.")
			


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
	global coins
	global feathers
	global diamonds
	global lives
	global nickname_db
	global hash1
	global target_person
	global target_person_decrypt
	global message_sent_decrypt
	global key_sent_decrypt
	

	key_encryption = ""
	token = ""

	def comd_decrypt():

		global key
		global keys
		global message
		global chances_decrypt
		global match
		global coins

		message = secret_messages[index]
		key = player_answer_decrypt.get()
		

		if chances_decrypt <= 3 and key == keys[index]:

			#playsound('C:/BirdCipher/Audios/VoiceAudios/CorrectKey.mp3')
			time.sleep(2)
			cipher_text.config(text = getTranslatedMessage(message, key), font = ("Comic Sans MS", 10))
			cipher_text.config(bg = '#050005', fg = '#7e086c')
			coins = coins + 1
			#playsound("rightDecrypt.mp3")
			#playsound("GoldCoin.mp3")
			labelCoins.config(text = coins)
			match = True
			

		elif chances_decrypt <= 3 and key!= keys[index]:

			#playsound('C:/BirdCipher/Audios/VoiceAudios/WrongKey.mp3')
			cipher_text.config(text = getTranslatedMessage(message, key), font = ("Comic Sans MS", 10))
			cipher_text.config(bg = '#050005', fg = '#FFFFFF')
			chances_decrypt = chances_decrypt + 1

		# elif chances_decrypt > 3:

		# 	playsound('C:/BirdCipher/Audios/VoiceAudios/chances_decrypt.mp3')


	def fernet_key_gen():

		global key_encryption

		# message_to_encrypt = cipher_text2.get("1.0", "end-1c")
		# message_to_encrypt = message_to_encrypt.encode()
		key_encryption = Fernet.generate_key()
		#f = Fernet(key)
		key_fernet_text.config(text = key_encryption.decode())
		clipboard.copy(key_encryption)


	def fernet_encryption_function():

		global key_encryption
		global token

		message_to_encrypt = cipher_text2.get("1.0", "end-1c")
		message_to_encrypt = message_to_encrypt.encode()
		f = Fernet(key_encryption)
		token = f.encrypt(message_to_encrypt)
		token = token.decode()
		cipher_text2_encrp.config(text = token, justify = "left", wraplength = 600)
		clipboard.copy(token)


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


	

	def person1_actv():

		global target_person

		person1_activated = True
		person2_activated = False
		person3_activated = False
		person4_activated = False
		target_person = person1_var.get()
		#playsound()

	def person2_actv():

		global target_person

		person1_activated = False
		person2_activated = True
		person3_activated = False
		person4_activated = False
		target_person = person2_var.get()
		#playsound()

	def person3_actv():

		global target_person

		person1_activated = False
		person2_activated = False
		person3_activated = True
		person4_activated = False
		target_person = person3_var.get()
		#playsound()

	def person4_actv():

		global target_person

		person1_activated = False
		person2_activated = False
		person3_activated = False
		person4_activated = True
		target_person = person4_var.get()
		#playsound()

	

	def person1c_actv():

		global target_person_decrypt

		person1c_activated = True
		person2c_activated = False
		person3c_activated = False
		person4c_activated = False
		target_person_decrypt = person1c_var.get()
		#playsound()

	def person2c_actv():

		global target_person_decrypt

		person1c_activated = False
		person2c_activated = True
		person3c_activated = False
		person4c_activated = False
		target_person_decrypt = person2c_var.get()
		#playsound()

	def person3c_actv():

		global target_person_decrypt

		person1c_activated = False
		person2c_activated = False
		person3c_activated = True
		person4c_activated = False
		target_person_decrypt = person3c_var.get()
		#playsound()

	def person4c_actv():

		global target_person_decrypt

		person1c_activated = False
		person2c_activated = False
		person3c_activated = False
		person4c_activated = True
		target_person_decrypt = person4c_var.get()
		#playsound()

	
	decrypt = tk.Tk()

	decrypt.title("BirdCipher Cryptographic Machine")
	decrypt.geometry('1050x540')
	decrypt.resizable(0, 0)

	player_answer_decrypt = tk.IntVar()
	player_message_encrypt = tk.StringVar()
	passw_em = tk.StringVar()
	password_for_decrypt = tk.StringVar()

	person1_var = tk.StringVar()
	person2_var = tk.StringVar()
	person3_var = tk.StringVar()
	person4_var = tk.StringVar()

	person1c_var = tk.StringVar()
	person2c_var = tk.StringVar()
	person3c_var = tk.StringVar()
	person4c_var = tk.StringVar()
	

	person1_activated = False
	person2_activated = False
	person3_activated = False
	person4_activated = False
	

	person1c_activated = False
	person2c_activated = False
	person3c_activated = False
	person4c_activated = False


	#miImagen = tk.PhotoImage(file = BirdCipher_list_k[2][0])
	#bird_singing_logo = tk.PhotoImage(file="Singing-logo5.png")

	decrypt_buttonImg = tk.PhotoImage(file = "Decrypt Message-logo1.png")
	listen_buttonImg = tk.PhotoImage(file = "Listen to the message-logo1.png")

	notebk = ttk.Notebook(decrypt)
	notebk.pack(expand=True)
		
	fr = ttk.Frame(notebk, width = 1050, height=540)
	fr.configure(style = "BW.TLabel")
	fr.pack(fill='both', expand=True)
	notebk.add(fr, text = "      BirdCipher Decrypt Machine")

	fr2 = ttk.Frame(notebk, width = 1150, height=540)
	fr2.pack(fill='both', expand=True)
	notebk.add(fr2, text = "      BirdCipher Personal Encryption Machine")

	fr3 = ttk.Frame(notebk, width = 1050, height=540)
	fr3.pack(fill='both', expand=True)
	notebk.add(fr3, text = "      BirdCipher Personal Decryption Machine")

	#imageLabel = tk.Label(miFrame, image=miImagen)
	#imageLabel.pack()

	cipher_text = tk.Label(fr, text = secret_messages[index], font = ("Comic Sans MS", 10), justify = 'center')
	#cipher_text.place(x = 30, y = 30)
	#cipher_text.pack(pady = 30)
	cipher_text.config(bg = '#050005', fg = '#FFFFFF', padx = 30)
	cipher_text.place(x = 60, y = 40)


	nicknameCuad = tk.Entry(fr, textvariable=player_answer_decrypt, font = ("Comic Sans MS", 13), justify = "center")
	#nicknameCuad.config(bg="black", fg="green")
	#nicknameCuad.place(x=50, y=55)
	#nicknameCuad.pack(padx = 30, pady = 30)
	nicknameCuad.config(bg = '#050005', fg = '#7e086c')
	nicknameCuad.place(x = 790, y = 100)
	

	decrypt_button = tk.Button(fr, image = decrypt_buttonImg, font = ("Comic Sans MS", 8), command = lambda:comd_decrypt())
	decrypt_button.config(fg = '#1af017')
	decrypt_button.place(x = 800, y = 150)
	
	#decrypt_button.pack()

	decrypt_listen = tk.Button(fr, image = listen_buttonImg, font = ("Comic Sans MS", 8), command = lambda:listen_decrypt_text())
	decrypt_listen.config(fg = '#1af017')
	decrypt_listen.place(x = 900, y = 150)
	
	#decrypt_listen.pack()


	imagen_caesar_cipher = tk.PhotoImage(file = 'Imagen_caesar.png')
	imagePoints = tk.PhotoImage(file = "Points-logo1.png")
	imageCoins = tk.PhotoImage(file = "Gold Coins-logo1.png")
	imageFeathers = tk.PhotoImage(file = "Feather-logo1.png")
	imageDiamonds = tk.PhotoImage(file = "Diamond-logo1.png")
	imageLives = tk.PhotoImage(file = "Lives-logo1.png")
	cryptoMachineImage = tk.PhotoImage(file = "Cryptographic Machine-logo1.png")

	imagen_caesar_cipher_lab = tk.Label(fr, image = imagen_caesar_cipher)
	#imagen_caesar_cipher_lab.config(bg = '#FFFFFF')
	imagen_caesar_cipher_lab.place(x = 30, y = 300)

	titleBirdCipherMachine = tk.Label(fr, text = "BirdCipher message about {} encrypted with the Caesar Cipher algorithm".format(BirdCipher_sci_k[index]), font = ("Comic Sans MS", 12))
	titleBirdCipherMachine.config(fg = "#7e086c")
	titleBirdCipherMachine.place(x = 70, y = 8)

	buttonPoints = tk.Button(fr, image = imagePoints, command = lambda:pointsAudio())
	buttonPoints.place(x = 210, y = 300)

	buttonCoins = tk.Button(fr, image = imageCoins, command = lambda:coinsAudio())
	buttonCoins.place(x = 300, y = 300)

	buttonFeathers = tk.Button(fr, image =imageFeathers, command = lambda:feathersAudio())
	buttonFeathers.place(x = 400, y = 300)

	buttonDiamonds = tk.Button(fr, image = imageDiamonds, command = lambda:diamondsAudio())
	buttonDiamonds.place(x= 500, y = 300)

	buttonLives = tk.Button(fr, image = imageLives, command = lambda:livesAudio())
	buttonLives.place(x = 615, y = 300)

	labelPoints = tk.Label(fr, text = points, font = ("Comic Sans MS", 13), justify = "center", width = 6)
	labelPoints.config(bg = "#050005", fg = "#7e086c")
	labelPoints.place(x = 212, y = 410)

	labelCoins = tk.Label(fr, text = coins, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	labelCoins.config(bg = "#050005", fg = "#7e086c")
	labelCoins.place(x = 300, y = 410)

	labelFeathers = tk.Label(fr, text = feathers, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	labelFeathers.config(bg = "#050005", fg = "#7e086c")
	labelFeathers.place(x = 400, y = 410)

	labelDiamonds = tk.Label(fr, text = diamonds, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	labelDiamonds.config(bg = "#050005", fg = "#7e086c")
	labelDiamonds.place(x = 500, y = 410)

	labelLives = tk.Label(fr, text = lifes, font = ("Comic Sans MS", 13), justify = "center", width = 7)
	labelLives.config(bg = "#050005", fg = "#7e086c")
	labelLives.place(x = 617, y = 410)

	labelQuestionKey = tk.Label(fr, text = "Enter the secret key", font = ("Comic Sans MS", 13))
	labelQuestionKey.config(fg = "#7e086c")
	labelQuestionKey.place(x = 805, y = 60)

	labelPlayerBCM = tk.Label(fr, text = "Welcome, {} ".format(nickname_db), font = ("Comic Sans MS", 11))
	labelPlayerBCM.config(fg = "#7e086c", bg = "#050005")
	labelPlayerBCM.place(x = 830, y = 20)

	imageCryptographicMachine = tk.Label(fr, image = cryptoMachineImage)
	imageCryptographicMachine.place(x = 750, y = 260)

	closeMachineButton = tk.Button(fr, text = "Close the BirdCipher Cryptographic Machine", font = ("Comic Sans MS", 12), command = lambda:closeMachine())
	closeMachineButton.place(x = 250, y = 460)
	closeMachineButton.config(fg = "#7e086c")


	# ---------------

	


	encryption_machine_logo = tk.PhotoImage(file = "Send Encrypted Message-logo.png")
	generate_key_image = tk.PhotoImage(file = "Generate Key-logo.png")
	encrypt_message_image = tk.PhotoImage(file = "Encrypt Message-logo1.png")

	cipher_text2 = tk.Text(fr2, font = ("Comic Sans MS", 10), width = 80)
	cipher_text2.config(bg = '#050005', fg = '#FFFFFF')
	cipher_text2.place(x = 60, y = 40, height = 70)

	key_fernet_label = tk.Label(fr2, text = "Key for Fernet algorithm")
	key_fernet_label.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
	key_fernet_label.place(x = 65, y = 120)

	key_fernet_text = tk.Label(fr2, text = "", font = ("Comic Sans MS", 10), width = 80)
	key_fernet_text.config(bg = "#050005", fg = "#FFFFFF")
	key_fernet_text.place(x = 60, y = 150)

	encrypted_label = tk.Label(fr2, text = "Your encrypted message is: ")
	encrypted_label.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
	encrypted_label.place(x = 65, y = 180)
	
	cipher_text2_encrp = tk.Label(fr2, text = "", font = ("Comic Sans MS", 10), width = 80)
	cipher_text2_encrp.config(bg = '#050005', fg = '#FFFFFF')
	cipher_text2_encrp.place(x = 60, y = 210, height = 80)

	nicknameCuad2 = tk.Entry(fr2, textvariable = passw_em, font = ("Comic Sans MS", 13), justify = "center")
	nicknameCuad2.config(bg = '#050005', fg = '#7e086c')
	nicknameCuad2.place(x = 790, y = 100)
	

	fernet_key_button = tk.Button(fr2, image = generate_key_image, font = ("Comic Sans MS", 8), command = lambda:fernet_key_gen())
	fernet_key_button.config(fg = '#7e086c')
	fernet_key_button.place(x = 800, y = 150)
	
	#decrypt_button.pack()

	fernet_encryption_message = tk.Button(fr2, image = encrypt_message_image, font = ("Comic Sans MS", 8), command = lambda:fernet_encryption_function())
	fernet_encryption_message.config(fg = '#1af017')
	fernet_encryption_message.place(x = 900, y = 150)

	imagen_caesar_cipher_lab2 = tk.Label(fr2, image = imagen_caesar_cipher)
	imagen_caesar_cipher_lab2.place(x = 30, y = 300)

	titleBirdCipherMachine2 = tk.Label(fr2, text = "BirdCipher Encryption Machine: a tool to guarantee the confidentiality of your messages", font = ("Comic Sans MS", 12))
	titleBirdCipherMachine2.config(fg = "#7e086c")
	titleBirdCipherMachine2.place(x = 70, y = 8)

	buttonPoints2 = tk.Button(fr2, image = imagePoints, command = lambda:pointsAudio())
	buttonPoints2.place(x = 210, y = 300)

	buttonCoins2 = tk.Button(fr2, image = imageCoins, command = lambda:person1_actv())
	buttonCoins2.place(x = 300, y = 300)

	buttonFeathers2 = tk.Button(fr2, image =imageFeathers, command = lambda:person2_actv())
	buttonFeathers2.place(x = 400, y = 300)

	buttonDiamonds2 = tk.Button(fr2, image = imageDiamonds, command = lambda:person3_actv())
	buttonDiamonds2.place(x= 500, y = 300)

	buttonLives2 = tk.Button(fr2, image = imageLives, command = lambda:person4_actv())
	buttonLives2.place(x = 615, y = 300)

	labelPoints2 = tk.Label(fr2, text = points, font = ("Comic Sans MS", 13), justify = "center", width = 6)
	labelPoints2.config(bg = "#050005", fg = "#7e086c")
	labelPoints2.place(x = 212, y = 410)

	person1 = tk.Entry(fr2, textvariable = person1_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	person1.config(bg = "#050005", fg = "#7e086c")
	person1.place(x = 300, y = 410)

	person2 = tk.Entry(fr2, textvariable = person2_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	person2.config(bg = "#050005", fg = "#7e086c")
	person2.place(x = 400, y = 410)

	person3 = tk.Entry(fr2, textvariable = person3_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	person3.config(bg = "#050005", fg = "#7e086c")
	person3.place(x = 500, y = 410)

	person4 = tk.Entry(fr2, textvariable = person4_var, font = ("Comic Sans MS", 13), justify = "center", width = 7)
	person4.config(bg = "#050005", fg = "#7e086c")
	person4.place(x = 617, y = 410)

	labelQuestionKey2 = tk.Label(fr2, text = "Enter the secret key", font = ("Comic Sans MS", 13))
	labelQuestionKey2.config(fg = "#7e086c")
	labelQuestionKey2.place(x = 805, y = 60)

	labelPlayerBCM2 = tk.Label(fr2, text = "Welcome, {} ".format(nickname_db), font = ("Comic Sans MS", 11))
	labelPlayerBCM2.config(fg = "#7e086c", bg = "#050005")
	labelPlayerBCM2.place(x = 830, y = 20)

	imageCryptographicMachine2 = tk.Button(fr2, image = encryption_machine_logo, command = lambda:send_message())
	imageCryptographicMachine2.place(x = 760, y = 290)
	imageCryptographicMachine2.config(bg = "#3f0322")

	closeMachineButton2 = tk.Button(fr2, text = "Close the BirdCipher Cryptographic Machine", font = ("Comic Sans MS", 12), command = lambda:closeMachine())
	closeMachineButton2.place(x = 250, y = 460)
	closeMachineButton2.config(fg = "#7e086c")

	# --------------


	cipher_text3 = tk.Label(fr3, font = ("Comic Sans MS", 10), justify = 'center', width = 72, height = 4)
	cipher_text3.config(bg = '#050005', fg = '#FFFFFF', padx = 30)
	cipher_text3.place(x = 60, y = 40)



	nicknameCuad3 = tk.Entry(fr3, textvariable=password_for_decrypt, font = ("Comic Sans MS", 13), justify = "center")
	nicknameCuad3.config(bg = '#050005', fg = '#7e086c')
	nicknameCuad3.place(x = 790, y = 100)

	decrypt_button3 = tk.Button(fr3, image = decrypt_buttonImg, font = ("Comic Sans MS", 8), command = lambda:displayCiphertext())
	decrypt_button3.config(fg = '#1af017')
	decrypt_button3.place(x = 800, y = 150)
	
	#decrypt_button.pack()

	decrypt_listen3 = tk.Button(fr3, image = listen_buttonImg, font = ("Comic Sans MS", 8), command = lambda:listen_decrypt_text())
	decrypt_listen3.config(fg = '#1af017')
	decrypt_listen3.place(x = 900, y = 150)

	imagen_caesar_cipher_lab3 = tk.Label(fr3, image = imagen_caesar_cipher)
	#imagen_caesar_cipher_lab.config(bg = '#FFFFFF')
	imagen_caesar_cipher_lab3.place(x = 30, y = 300)

	titleBirdCipherMachine3 = tk.Label(fr3, text = "BirdCipher Decryption Machine", font = ("Comic Sans MS", 12))
	titleBirdCipherMachine3.config(fg = "#7e086c")
	titleBirdCipherMachine3.place(x = 70, y = 8)

	key_fernet_label2 = tk.Label(fr3, text = "Key for Fernet algorithm")
	key_fernet_label2.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
	key_fernet_label2.place(x = 65, y = 120)

	key_fernet_text2 = tk.Label(fr3, text = "", font = ("Comic Sans MS", 10), width = 80)
	key_fernet_text2.config(bg = "#050005", fg = "#FFFFFF")
	key_fernet_text2.place(x = 60, y = 150)

	encrypted_label2 = tk.Label(fr3, text = "Your decrypted message is: ")
	encrypted_label2.config(font = ("Comic Sans MS", 12), fg = "#7e086c")
	encrypted_label2.place(x = 65, y = 180)
	
	cipher_text2_encrp2 = tk.Label(fr3, text = "", font = ("Comic Sans MS", 10), width = 80)
	cipher_text2_encrp2.config(bg = '#050005', fg = '#FFFFFF')
	cipher_text2_encrp2.place(x = 60, y = 210, height = 80)



	buttonPoints3 = tk.Button(fr3, image = imagePoints, command = lambda:pointsAudio())
	buttonPoints3.place(x = 210, y = 300)

	buttonCoins3 = tk.Button(fr3, image = imageCoins, command = lambda:person1c_actv())
	buttonCoins3.place(x = 300, y = 300)

	buttonFeathers3 = tk.Button(fr3, image =imageFeathers, command = lambda:person2c_actv())
	buttonFeathers3.place(x = 400, y = 300)

	buttonDiamonds3 = tk.Button(fr3, image = imageDiamonds, command = lambda:person3c_actv())
	buttonDiamonds3.place(x= 500, y = 300)

	buttonLives3 = tk.Button(fr3, image = imageLives, command = lambda:person4c_actv())
	buttonLives3.place(x = 615, y = 300)

	labelPoints3 = tk.Label(fr3, text = points, font = ("Comic Sans MS", 13), justify = "center", width = 6)
	labelPoints3.config(bg = "#050005", fg = "#7e086c")
	labelPoints3.place(x = 212, y = 410)

	person1_c = tk.Entry(fr3, text = person1c_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	person1_c.config(bg = "#050005", fg = "#7e086c")
	person1_c.place(x = 300, y = 410)

	person2_c = tk.Entry(fr3, text = person2c_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	person2_c.config(bg = "#050005", fg = "#7e086c")
	person2_c.place(x = 400, y = 410)

	person3_c = tk.Entry(fr3, text = person3c_var, font = ("Comic Sans MS", 13), justify = "center", width = 8)
	person3_c.config(bg = "#050005", fg = "#7e086c")
	person3_c.place(x = 500, y = 410)

	person4_c = tk.Entry(fr3, text = person4c_var, font = ("Comic Sans MS", 13), justify = "center", width = 7)
	person4_c.config(bg = "#050005", fg = "#7e086c")
	person4_c.place(x = 617, y = 410)

	labelQuestionKey3 = tk.Label(fr3, text = "Enter the secret key", font = ("Comic Sans MS", 13))
	labelQuestionKey3.config(fg = "#7e086c")
	labelQuestionKey3.place(x = 805, y = 60)

	labelPlayerBCM3 = tk.Label(fr3, text = "Welcome, {} ".format(nickname_db), font = ("Comic Sans MS", 11))
	labelPlayerBCM3.config(fg = "#7e086c", bg = "#050005")
	labelPlayerBCM3.place(x = 830, y = 20)

	imageCryptographicMachine3 = tk.Button(fr3, image = cryptoMachineImage, command = lambda:bc_decription_machine())
	imageCryptographicMachine3.place(x = 730, y = 260)

	closeMachineButton3 = tk.Button(fr3, text = "Close the BirdCipher Cryptographic Machine", font = ("Comic Sans MS", 12), command = lambda:closeMachine())
	closeMachineButton3.place(x = 250, y = 460)
	closeMachineButton3.config(fg = "#7e086c")

	def send_message():

		global nickname_db
		global key_encryption
		global token
		global target_person



		bdatos = bytes(passw_em.get(), 'utf-8')
		h = hashlib.new(algoritmo, bdatos)
		hash2 = HASH.generaHash(h)

		miConexion2 = sqlite3.connect("BirdCipher_DB.db")
		miCursor2 = miConexion2.cursor()

		sql110 = 'insert into encryptedMessages(nickname, password, server, actual_message, key_b) values(?,?,?,?,?)'
		datos_sql110 = (nickname_db, hash2, target_person, token, key_encryption)

		sql_verf_hash = 'select * from Players where nickname = (?)'
		sql_verf_hash_data = (nickname_db,)

		sql_verf_server = 'select * from encryptedMessages where server = (?)'
		sql_verf_server_data = (target_person,)

		sql111 = 'update encryptedMessages set (nickname, password, server, actual_message, key_b) = (?,?,?,?,?) where server = (?)'
		datasql111 = (nickname_db, hash2, target_person, token, key_encryption, target_person)

		miCursor2.execute(sql_verf_hash, sql_verf_hash_data)
		dlt5 = miCursor2.fetchall()

		if dlt5[0][5] > 10 and hash2 == dlt5[0][3]:

			miCursor2.execute(sql_verf_server, sql_verf_server_data)
			df1 = miCursor2.fetchall()

			if len(df1) == 0:

				miCursor2.execute(sql110, datos_sql110)

			elif len(df1) > 0:

				miCursor2.execute(sql111, datasql111)


		miConexion2.commit()
		miConexion2.close()

	
	def displayCiphertext():

		global nickname_db
		global key_encryption
		global token
		global target_person
		global message_sent_decrypt
		global key_sent_decrypt
	

		cdatos = bytes(password_for_decrypt.get(), 'utf-8')
		g = hashlib.new(algoritmo, cdatos)
		hash3 = HASH.generaHash(g)

		miConexion3 = sqlite3.connect("BirdCipher_DB.db")
		miCursor3 = miConexion3.cursor()

		sql33 = 'select * from Players where nickname = (?)'
		datasql33 = (nickname_db,)

		sql330 = 'select * from encryptedMessages where server = (?) and nickname = (?)'
		datasql330 = (nickname_db, target_person_decrypt)

		miCursor3.execute(sql33, datasql33)
		dlt6 = miCursor3.fetchall()

		if hash3 == dlt6[0][3]:

			miCursor3.execute(sql330, datasql330)
			dlt7 = miCursor3.fetchall()

			if len(dlt7) > 0:

				message_sent_decrypt = dlt7[0][4]
				key_sent_decrypt = dlt7[0][6]

				cipher_text3.config(text = dlt7[0][4], justify = "left", wraplength = 600, font = ("Comic Sans MS", 10))
				
				key_fernet_text2.config(text = dlt7[0][6])


		miConexion3.commit()
		miConexion3.close()


	def bc_decription_machine():

		global message_sent_decrypt
		global key_sent_decrypt

		#message_sent_decrypt = message_sent_decrypt.encode()
		k = Fernet(key_sent_decrypt)
		token2 = k.decrypt(message_sent_decrypt)
		#token2 = token2.decode()
		cipher_text2_encrp2.config(text = token2, justify = "left", wraplength = 600)



	decrypt.protocol("WM_DELETE_WINDOW", lambda: None)

	decrypt.mainloop()


attempts = 1

lives = 4

End = False



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
		#playsound("Lost_a_life.mp3")
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
		print("-------------------------- BIRDCIPHER - DATA GUESSING OF BIRDS BIODIVERSITY. LET US PLAY NOW!!!----------------------")
		print()
		print("   Guess the number of species corresponding to the group: ", BirdCipher_english_k[index])
		print()
		#playsound("try_guess.mp3")
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

		#playsound("larger.mp3")
		print("   * There are more species in this group (order) of birds. Try again.")
		question()
		attempts = attempts + 1
		

	elif guess > secretNumber:

		#playsound("smaller.mp3")
		print("   * There are fewer species in this group (order) of birds. Try again: ")
		question()
		attempts = attempts + 1
		

	elif guess == secretNumber and attempts <= 7 and len(BirdCipher_list_k) > 1:

		points = points + 10
		updatePlayer_points()
		print()
		print("---------------------------------------------------- RESULTS -----------------------------------------------------")
		print()
		print("   Congratulations!!! You guessed the total number of species of this group. You have earned 10 points!!!")
		print()
		print("   Now you have: ", points, " points.")
		#hit = True
		#playsound("Congratulations.mp3")
		time.sleep(8)
		print()
		print()
		print()
		print("---------------------------------- DECRYPT THE SECRET MESSAGE ABOUT THIS GROUP OF BIRDS!!!! -----------------------------")
		print()
		print()
		time.sleep(3)
		print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		#playsound("radar-ufo.mp3")
		#playsound("sonar-radar.mp3")
		time.sleep(3)
		caesarCipher()
		#playsound("DecipherMessage.mp3")
		print()
		print("                                                     ", BirdCipher_sci_k[index], "                                      ")
		print()
		time.sleep(3)
		print("                                               ", BirdCipher_english_k[index], "                                        ")
		print()
		time.sleep(3)
		print("                                                 Caesar Cipher Algorithm                                                ")
		time.sleep(3)
		print()
		print("                                                 Simmetrycal cryptography                                                ")
		time.sleep(3)
		print()
		print("                                    Here comes the BirdCipher Cryptographic Machine                                    ")
		print()
		print()
		print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

		#playsound('MessageClueObtained.mp3')
		#playsound(key_audios_k[index])
		time.sleep(2)
		#playsound('WriteTheClue.mp3')
		# here comes the GUI_BirdCipher Machine
		#key = getKey()

		GUI_BirdCipher_Machine()

		#print("Prueba GUI BirdCipher Machine")

		# if isinstance(key, str):

		# 	print("        Incorrect data type")

		if key == keys_k[index]:

			updatePlayer_coins()
			#playsound("rightDecrypt.mp3")
			#playsound("GoldCoin.mp3")
			time.sleep(2)
			#playsound("seePictureAgain.mp3")

			count = 0
			
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
		#playsound("try_guess.mp3")
		question()
		print()
		attempts = attempts + 1

	elif guess == secretNumber and attempts <= 7 and len(BirdCipher_list_k) == 1:

		
		print("--------------------------------------------------- RESULTS -----------------------------------------------------------")
		print()
		print()
		print("   Congratulations!!! You guessed the size of the bird I was thinking of. You have earned 10 points!!!")
		#playsound("Congratulations.mp3")
		time.sleep(3)
		#playsound("End.mp3")
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





