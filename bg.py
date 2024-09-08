import hashlib
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
#import pandas as pd
from io import StringIO
from docx import Document


root = tk.Tk()


files = ''

def abrirFichero():

    global files

    files = filedialog.askopenfilename(title = 'Abrir')
    print(files)


booton = tk.Button(root, text = 'Abrir fichero', command = lambda:abrirFichero())
booton.pack()

root.mainloop()
 
 
def get_checksum(filename, hash_function):
    """Generate checksum for file baed on hash function (MD5 or SHA256).
 
    Args:
        filename (str): Path to file that will have the checksum generated.
        hash_function (str):  Hash function name - supports MD5 or SHA256
 
    Returns:
        str`: Checksum based on Hash function of choice.
 
    Raises:
        Exception: Invalid hash function is entered.
 
    """
    hash_function = hash_function.lower()
 
    with open(filename, "rb") as f:
        byte = f.read()  # read file as bytes

        if hash_function == "md5":
            readable_hash = hashlib.md5(byte).hexdigest()
        elif hash_function == "sha256":
            readable_hash = hashlib.sha256(byte).hexdigest()
        else:
            Raise("{} is an invalid hash function. Please Enter MD5 or SHA256")
 
    return readable_hash


fer = get_checksum(files, 'sha256')




url = "https://www.virustotal.com/api/v3/files/" + fer

headers = {
    "accept": "application/json", "content-type": "multipart/form-data",
    "x-apikey": "c101a53eeba361bc3ac3eda6b9d3818d62f482cc4b329b8cd00111f422c48c10"
}

response = requests.get(url, headers=headers)

print(response.text)