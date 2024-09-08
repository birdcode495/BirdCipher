import hashlib
from virus_total_apis import PublicApi
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image


API_KEY = 'c101a53eeba361bc3ac3eda6b9d3818d62f482cc4b329b8cd00111f422c48c10'
api = PublicApi(API_KEY)
files = ''

root = tk.Tk()




def abrirFichero():

	global files

	files = filedialog.askopenfilename(title = 'Abrir')
	print(files)


booton = tk.Button(root, text = 'Abrir fichero', command = lambda:abrirFichero())
booton.pack()







root.mainloop()

with open(files, 'rb') as myFile:

	filehash = hashlib.sha256(myFile.read()).hexdigest()



response = api.get_file_report(filehash)


print(response)


