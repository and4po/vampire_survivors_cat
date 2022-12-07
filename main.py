import json
import os
# import random

json_file = ""
langs = ["en", "ca"]
lang = "en"
cat = 1

tags = []
en_text = []
ca_text = []

c = 0
type = 0
puti = ""

lang_dir = input("Ruta: ") or "FINALS(EN-CAT)/"

tipus = input("Tipus(csv-json, json-csv): ")
while tipus != "csv-json" and tipus != "json-csv" and tipus != "j-c" and tipus != "c-j":
    print("No t'entenc, comprova que ho has escrit bé.")
    tipus = input("Tipus(csv-json, json-csv): ")

if tipus == "json-csv" or tipus == "j-c":
    type = 1
else:
    type = 2

try:
    os.mkdir(lang_dir + "CSV/")
except:
    print("La carpeta CVS ja existeix, els arxius probablement es sobreescriuran.")

for json_file in os.listdir(lang_dir):

    if type == 1 and ".json" in json_file:
        # Opening JSON file
        with open(lang_dir + "/" + json_file) as f:
        
            #Llegeix l'arxiu
            data = json.load(f)

        
        for l in range(2):
            lang = langs[l]

            try:
                puti = data[lang]["translations"]
            except:
                print("Sense català")
                cat = 0
                continue

            for i in data[lang]["translations"]:

                if json_file != "lang.json":

                    for x in data[lang]["translations"][i]:
                        if lang == "en":
                            tags.append(i + "/" + x)
                            if "\n" in data[lang]["translations"][i][x]:
                                en_text.append((data[lang]["translations"][i][x]).replace("\n", "\\n"))
                            else:
                                en_text.append(data[lang]["translations"][i][x])

                            for c in range(len(en_text)):
                                ca_text.append("")
                        else:
                            if "\n" in data[lang]["translations"][i][x]:
                                ca_text[tags.index(i + "/" + x)] = (data[lang]["translations"][i][x].replace("\n", "\\n"))
                            else:
                                ca_text[tags.index(i + "/" + x)] = data[lang]["translations"][i][x]

                else:

                    if lang == "en":
                        tags.append(i)

                        if "\n" in data[lang]["translations"][i]:
                            en_text.append((data[lang]["translations"][i]).replace("\n", "\\n"))
                        else:
                            en_text.append(data[lang]["translations"][i])
                        
                        for c in range(len(en_text)):
                                ca_text.append("")
                    else:
                        if "\n" in data[lang]["translations"][i]:
                            ca_text[tags.index(i)] = (data[lang]["translations"][i].replace("\n", "\\n"))
                        else:
                            ca_text[tags.index(i)] = data[lang]["translations"][i]


            
        with open((lang_dir + "CSV/" + (json_file.replace(".json", ".csv"))), "w") as f:

            f.write("Identificador\tAnglès\tCatalà\n")

            for li in range(len(tags)):
                    f.write(tags[li] + "\t" + en_text[li] + "\t" + ca_text[li] + "\n")
            tags.clear()
            en_text.clear()
            ca_text.clear()