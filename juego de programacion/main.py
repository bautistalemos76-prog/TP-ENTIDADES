from entidades import (
    armaduras,
    armas,
    enemigos,
    generar_personaje,
    mostrar_armadura,
    mostrar_arma,
    mostrar_enemigo,
    mostrar_personaje,
)
from funciones import menu


def main():
    nombre = input("Ingrese el nombre de su personaje: ")
    personaje = generar_personaje(nombre)

    while True:
        opcion = menu()

        if opcion == 1:
            mostrar_personaje(personaje)
        elif opcion == 2:
            mostrar_enemigo(enemigos["arquero"])
        elif opcion == 3:
            print("Curar...")
        elif opcion == 4:
            mostrar_arma(armas["espada"])
            mostrar_armadura(armaduras["casco"])
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()