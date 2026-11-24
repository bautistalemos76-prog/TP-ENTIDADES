import random

vida_maxima = 100

personaje_principal = {
    "nombre": "",
    "vida_maxima": vida_maxima,
    "vida_actual": vida_maxima,
    "fuerza": 0,
    "suerte": 0,
    "monedas": 0,
    "pociones": 0,
    "arma": {},
    "armadura": {},
}

armas = {
    "espada": {
        "nombre": "espada",
        "daño": 60,
        "critico": 80,
        "precio": 1200,
    },
    "arco": {
        "nombre": "arco",
        "daño": 30,
        "critico": 50,
        "precio": 1500,
    },
}

armaduras = {
    "casco": {
        "resistencia": 100,
        "precio": 2700,
    },
    "pechera": {
        "resistencia": 150,
        "precio": 3500,
    },
}

enemigos = {
    "arquero": {
        "nombre": "arquero",
        "vida": 100,
        "daño": 30,
        "tesoro": 1500,
    },
    "zombie": {
        "nombre": "zombie",
        "vida": 130,
        "daño": 20,
        "tesoro": 2000,
    },
}


def mostrar_enemigo(enemigo: dict):
    print(enemigo["nombre"])
    print(enemigo["vida"])
    print(enemigo["daño"])
    print(enemigo["tesoro"])


def generar_personaje(nombre):
    global personaje_principal
    personaje = personaje_principal.copy()

    personaje["nombre"] = nombre
    personaje["fuerza"] = random.randint(1, 100)
    personaje["suerte"] = random.randint(1, 100)

    mostrar_personaje(personaje)

    return personaje


def mostrar_personaje(personaje: dict):
    print("Nombre: ", personaje["nombre"])
    print("Vida: ", personaje["vida_actual"], "/", personaje["vida_maxima"])
    print("Suerte: ", personaje["suerte"])


def mostrar_arma(arma: dict):
    print("Daño", arma["daño"])
    print("Daño Citico", arma["critico"])
    print("Precio:", arma["precio"])


def mostrar_armadura(armadura: dict):
    print("Resistencia", armadura["resistencia"])
    print("Precio:", armadura["precio"])