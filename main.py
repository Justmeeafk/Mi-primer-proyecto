meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "Fomo": "Miedo a perderse de un evento/actividad",
    "IDK": "I dont know no lo se en ingles",
    "Idc": "No me importa en ingles",
    "CREEPY": "aterrador, siniestro",
}

word = input("Escribe una palabra: ")

if word in meme_dict.keys(
⌄
⌄
):
    print(meme_dict[word])
else:
    print("Esa palabra no está en el diccionario.")
