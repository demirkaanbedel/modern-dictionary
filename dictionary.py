print("Hi! Welcome to modern words dictionary! You ask we awnser!")
while True:
    words = {
        "lol" : "response to something funny",
        "cringe" : "something strange or embarrassing",
        "rofl" : "bir şakaya karşılık cevap",
        "sheesh" : "disapprove",
        "creepy" : "scary",
        "aggro" : "aggressive/angry",
    }
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    if word in words.keys():
        print(word," words meaning=",words[word])
    else:
        print("This word is not avaible.")
