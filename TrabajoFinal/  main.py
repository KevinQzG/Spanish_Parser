from verificacion import verificacion
# Analizador de oraciones simples en español
verificador = verificacion()


def volverIngresar():  # Funcion que pregunta si se quiere volver a ingresar una oracion
    print("\033[;31m" + "¿Desea volver a ingresar una oración?" + "\033[0m")
    print("\033[;36m" + "1. Continuar" + "\033[0m")
    print("\033[;36m" + "2. No, quiero salir" + "\033[0m")
    option = input("\033[;31m" "\n" + "Seleccione una opción: " + "\033[0m")
    if option == "1":
        Menu()
    elif option == "2":
        salida()
    else:
        print("\033[;31m" + "\n" +
              "Opción no valida, intente nuevamente" + "\033[0m")
        Menu()


def salida():  # Funcion que sale del programa
    print("\033[;31m" + "\n" +
          "Gracias por usar el analizador de oraciones en español de Juan Esteban y Kevin" + "\033[0m")
    exit()


def Menu():  # Funcion que muestra el menu
    while True:
        print("\033[;31m" + "\n" +
              "*-~--~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-*" + "\033[0m")
        print("\033[;36m" + "* Bienvenido al analizador de oraciones simples en español de Juan Esteban y Kevin *" + "\033[0m")
        print("\033[;31m" + "*-~--~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-*" + "\033[0m" + "\n")
        print("\033[;31m" +
              "Seleccione una opción para continuar:" + "\n" + "\033[0m")
        print("\033[;36m" + "1. Ingresar oración" + "\033[0m")
        print("\033[;36m" + "2. Salir" + "\033[0m" + "\n")

        option = input("\033[;31m" "\n" +
                       "Seleccione una opción: " + "\033[0m")
        if option == "2":
            salida()
        if option != "1" and option != "2":
            print(
                "\033[;31m" + "Opción no válida, ingrese una opción valida" + "\033[0m")
            continue
        if option == "1":
            print("\033[;31m" + "\n" +
                  "La palabras de palabras válidas son:" + "\n" + "\033[0m")
            print("\033[;36m" + "Artículos definidos: " +
                  str(verificador.articulosDefinidos) + "\033[0m")
            print("\033[;36m" + "Artículos indefinidos: " +
                  str(verificador.articulosIndefinidos) + "\033[0m")
            print("\033[;36m" + "Sustantivos impropios: " +
                  str(verificador.sustantivosImpropios) + "\033[0m")
            print("\033[;36m" + "Sustantivos propios: " +
                  str(verificador.sustantivosPropios) + "\033[0m")
            print("\033[;36m" + "Verbos: " +
                  str(verificador.verbos) + "\033[0m")
            print("\033[;36m" + "Adjetivos: " +
                  str(verificador.adjetivos) + "\033[0m")
            print("\033[;36m" + "Adverbios: " +
                  str(verificador.adverbios) + "\033[0m")
            print("\033[;36m" + "Enlaces: " +
                  str(verificador.enlace) + "\033[0m")

            oracion = input(
                "\033[;31m" + "\n" + "Ingrese la oración a analizar:" + "\n" + "\033[0m").lower()
            palabras = oracion.split(" ")  # Separa la oracion en palabras

            # Verifica si las palabras de la oracion estan en la base de palabras
            if not verificador.basePalabras(palabras):
                print(
                    "\033[;31m" + "\n" + "Hay palabras que no estan en la base de palabras, ingrese una oración con palabras validas" + "\n" + "\033[0m")
                Menu()

            if verificador.validar(palabras):  # Si la oracion es valida
                print("\033[;32m" + "\n" +
                      "La oración ingresada es válida" + "\033[0m")
                volverIngresar()

            else:  # Si la oracion no es valida
                print("\033[;31m" + "\n" + "Oración inválida, no se puede tener más de un verbo, adjetivo y/o adverbio en una oración simple" + "\n" + "\033[0m")
                volverIngresar()


def main():  # Funcion principal
    Menu()


if __name__ == "__main__":  # Llamado a la funcion principal (buenas practicas)
    main()


# Creado por Juan Esteban y Kevin
