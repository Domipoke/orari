import pandas as pd

ex = pd.read_excel("./orario.xlsx")
orario = {}
#range(len(ex.index))

for i in range(len(ex.index)):
    doc_name = ex.loc[i][0]
    
    for k in range(1,36):
        classe = ex.loc[i][k]
        time = ex.columns[k]
        if classe != "nan": 
            if not classe in orario.keys():
                orario[classe] = {
                    "Lunedì_08:00": "",
                    "Lunedì_09:00": "",
                    "Lunedì_10:00": "",
                    "Lunedì_11:00": "",
                    "Lunedì_12:00": "",
                    "Lunedì_13:00": "",
                    "Lunedì_14:00": "",
                    
                    "Martedì_08:00": "",
                    "Martedì_09:00": "",
                    "Martedì_10:00": "",
                    "Martedì_11:00": "",
                    "Martedì_12:00": "",
                    "Martedì_13:00": "",
                    "Martedì_14:00": "",

                    "Mercoledì_08:00": "",
                    "Mercoledì_09:00": "",
                    "Mercoledì_10:00": "",
                    "Mercoledì_11:00": "",
                    "Mercoledì_12:00": "",
                    "Mercoledì_13:00": "",
                    "Mercoledì_14:00": "",

                    "Giovedì_08:00": "",
                    "Giovedì_09:00": "",
                    "Giovedì_10:00": "",
                    "Giovedì_11:00": "",
                    "Giovedì_12:00": "",
                    "Giovedì_13:00": "",
                    "Giovedì_14:00": "",

                    "Venerdì_08:00": "",
                    "Venerdì_09:00": "",
                    "Venerdì_10:00": "",
                    "Venerdì_11:00": "",
                    "Venerdì_12:00": "",
                    "Venerdì_13:00": "",
                    "Venerdì_14:00": "",
                }
            orario[classe][time]=doc_name


def ask_forClass():
    c=input("Classe? es. 1T:  ")
    if c in orario.keys():
        ora=orario[c]
        res = pd.DataFrame({
            "Lunedì":[
                ora["Lunedì_08:00"],
                ora["Lunedì_09:00"],
                ora["Lunedì_10:00"],
                ora["Lunedì_11:00"],
                ora["Lunedì_12:00"],
                ora["Lunedì_13:00"],
                ora["Lunedì_14:00"],
            ],
            "Martedì":[
                ora["Martedì_08:00"],
                ora["Martedì_09:00"],
                ora["Martedì_10:00"],
                ora["Martedì_11:00"],
                ora["Martedì_12:00"],
                ora["Martedì_13:00"],
                ora["Martedì_14:00"],
            ],
            "Mercoledì":[
                ora["Mercoledì_08:00"],
                ora["Mercoledì_09:00"],
                ora["Mercoledì_10:00"],
                ora["Mercoledì_11:00"],
                ora["Mercoledì_12:00"],
                ora["Mercoledì_13:00"],
                ora["Mercoledì_14:00"],
            ],
            "Giovedì":[
                ora["Giovedì_08:00"],
                ora["Giovedì_09:00"],
                ora["Giovedì_10:00"],
                ora["Giovedì_11:00"],
                ora["Giovedì_12:00"],
                ora["Giovedì_13:00"],
                ora["Giovedì_14:00"],
            ],
            "Venerdì":[
                ora["Venerdì_08:00"],
                ora["Venerdì_09:00"],
                ora["Venerdì_10:00"],
                ora["Venerdì_11:00"],
                ora["Venerdì_12:00"],
                ora["Venerdì_13:00"],
                ora["Venerdì_14:00"],
            ]
        },index=["08:00","09:00","10:00","11:00","12:00","13:00","14:00"])
        print(res)
    ask_forClass()
ask_forClass()
