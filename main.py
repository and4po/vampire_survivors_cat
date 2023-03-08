# Aquest sistema agafa els enllaços, posats de la següent manera,
# (nom)[enllaç] i fa un botó de l'enllaç i posa el text pla.

from webbrowser import open_new
import tkinter as tk

patro = "((.*?))"

root = tk.Tk()
root.geometry("400x200")

# Treure una cadena des d'uns separadors
def substring(caracter_in, caracter_out, text):
    index_in = text.index(caracter_in)
    index_out = text.index(caracter_out) 
    subcadena = text[index_in+1:index_out]
    return subcadena

# Obrir enllaç al navegador
def openBrowser(link):
    open_new(enllaç)

with open("Hello.txt", "r", encoding='utf8') as f:
    txt = f.read()
    print(txt)

if ")" in txt and txt[txt.find(")")+1] == "[":

    nom_enllaç = substring("(", ")", txt)
    enllaç = substring("[", "]", txt)

    txt = txt.replace("(" + nom_enllaç + ")" + "[" + enllaç + "]", ")^-^(")
    nou_txt = txt.split(")^-^(")

    labl1 = tk.Label(root, text = nou_txt[0]).pack(pady=10)
    btn = tk.Button(root, text = nom_enllaç, command= lambda: openBrowser(enllaç)).pack()
    labl2 = tk.Label(root, text = nou_txt[1]).pack(pady=10)

root.mainloop()  