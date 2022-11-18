# Analizador de oraciones simples en español

articulosDefinidos = ["el", "los", "la", "las"]
articulosIndefinidos = ["un", "uno", "una", "unas", "unos"]
sustantivosImpropios = ["adulto", "adultos", "joven", "jovenes",
                        "perro", "perros", "gato", "gatos", "papá", "papás", ]
sustantivosPropios = ["juan", "lorena", "kevin", "david", "maria", "ana"]
verbos = ["juega", "juegan", "jugaron", "jugarán", "come", "comen", "comieron", "comerán", "canta", "cantan",
          "cantaron", "cantarán", "salta", "saltan", "saltaron", "saltarán", "corren",  "corre", "corrió", "correrán"]
adjetivos = ["grande", "feo", "malo", "bueno",
             "divertido", "rapido", "bonito", "duro"]
adverbios = ["muy", "demasiado", "poco", "bastante", "mucho", "poco", "bien", "mal", "divertido", "rapido", "bonito", "duro"]
enlace = ["con"]

palabrasTotal = articulosDefinidos + articulosIndefinidos + sustantivosImpropios + sustantivosPropios + verbos + adjetivos + adverbios + enlace

listIndex = []  # Lista que almacena los indices de las palabras



def verificacion1(palabras):  
    if (sustantivosPropios.__contains__(palabras[0].lower()) or articulosDefinidos.__contains__(palabras[0].lower()) and verbos.__contains__(palabras[1].lower())):
        return True
    else:
        return False


def verificacion2(palabras): 
    if (articulosDefinidos.__contains__(palabras[0].lower()) or articulosIndefinidos.__contains__(palabras[0].lower()) and sustantivosImpropios.__contains__(palabras[1].lower()) and verbos.__contains__(palabras[2].lower())):
        return True
    else:
        return False


def verificacion3(palabras): 
    if (articulosIndefinidos.__contains__(palabras[0].lower()) and sustantivosImpropios.__contains__(palabras[1].lower()) and verbos.__contains__(palabras[2].lower())):
        return True
    else:
        return False

def verificacion4(palabras):  
    if (articulosDefinidos.__contains__(palabras[0].lower()) or articulosIndefinidos.__contains__(palabras[0].lower()) and sustantivosImpropios.__contains__(palabras[1].lower()) and verbos.__contains__(palabras[2].lower()) and adjetivos.__contains__(palabras[3].lower())):
        return True
    else:
        return False
    
def verificacion5(palabras):  
    if (sustantivosPropios.__contains__(palabras[0].lower()) and verbos.__contains__(palabras[1].lower()) and adjetivos.__contains__(palabras[2].lower()) or adverbios.__contains__(palabras[2].lower())):
        return True
    else:
        return False
    
def verificacion6(palabras): 
    if (sustantivosPropios.__contains__(palabras[0].lower()) or articulosDefinidos.__contains__(palabras[0].lower()) and verbos.__contains__(palabras[1].lower()) and adverbios.__contains__(palabras[2].lower()) or adjetivos.__contains__(palabras[2].lower())):
        return True
    else:
        return False
    
def verificacion7(palabras): 
    if (sustantivosPropios.__contains__(palabras[0].lower()) and verbos.__contains__(palabras[1].lower()) and enlace.__contains__(palabras[2].lower()) and articulosDefinidos.__contains__(palabras[3].lower()) and sustantivosImpropios.__contains__(palabras[4].lower()) or articulosIndefinidos.__contains__(palabras[4].lower())):
        return True
    else:
        return False
    
def verificacion8(palabras): 
    if (articulosDefinidos.__contains__(palabras[0].lower()) or articulosIndefinidos.__contains__(palabras[0].lower()) and sustantivosImpropios.__contains__(palabras[1].lower()) and verbos.__contains__(palabras[2].lower()) and enlace.__contains__(palabras[3].lower()) and articulosDefinidos.__contains__(palabras[4].lower()) or articulosIndefinidos.__contains__(palabras[4].lower()) and sustantivosImpropios.__contains__(palabras[5].lower())):
        return True
    else:
        return False
    


def verificacionVerbo(palabras): #Verifica que el verbo esté solo una vez
    c = 0
    for x in palabras:
      if x in verbos:
        c+=1
    if c >= 2:
      return False
    else:
      return True
    
def verificacionAdjetivo(palabras): #Verifica que el adjetivo esté solo una vez
    c = 0
    for x in palabras:
        if x in adjetivos:
            c+=1
    if c >= 2:
        return False
    else:
        return True
    
def verificacionAdverbio(palabras): #Verifica que el adverbio esté solo una vez
    c = 0
    for x in palabras:
        if x in adverbios:
            c+=1
    if c >= 2:
        return False
    else:
        return True
    

def validar(palabras):  # Valida que las palabras cumplan las reglas (verificaciones)
    if (verificacionAdjetivo(palabras) != True):
        return False
    if (verificacionAdverbio(palabras) != True):
        return False
    if(verificacionVerbo(palabras) != True):
      return False
    elif (verificacionVerbo(palabras)  or verificacionAdverbio(palabras) or verificacionAdjetivo(palabras) or verificacion1(palabras) or verificacion2(palabras) or verificacion3(palabras) or verificacion4(palabras) or verificacion5(palabras) or verificacion6(palabras) or verificacion7(palabras) or verificacion8(palabras)):
        return True
    else:
        return False


def basePalabras(palabras):  # Funcion que almacena las palabras en una lista
    variable = True
    for i in palabras:
        if i not in palabrasTotal:
            variable = False
    return variable


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
        print("\033[;31m" + "\n" + "Opción no valida, intente nuevamente" + "\033[0m")
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
                  str(articulosDefinidos) + "\033[0m")
            print("\033[;36m" + "Artículos indefinidos: " +
                  str(articulosIndefinidos) + "\033[0m")
            print("\033[;36m" + "Sustantivos impropios: " +
                  str(sustantivosImpropios) + "\033[0m")
            print("\033[;36m" + "Sustantivos propios: " +
                  str(sustantivosPropios) + "\033[0m")
            print("\033[;36m" + "Verbos: " + str(verbos) + "\033[0m")
            print("\033[;36m" + "Adjetivos: " + str(adjetivos) + "\033[0m")
            print("\033[;36m" + "Adverbios: " + str(adverbios) + "\033[0m")
            print("\033[;36m" + "Enlaces: " + str(enlace) + "\033[0m")

            oracion = input(
                "\033[;31m" + "\n" + "Ingrese la oración a analizar:" + "\n" + "\033[0m").lower()
            palabras = oracion.split(" ")  # Separa la oracion en palabras

            # Verifica si las palabras de la oracion estan en la base de palabras
            if not basePalabras(palabras):
                print(
                    "\033[;31m" + "\n" + "Hay palabras que no estan en la base de palabras, ingrese una oración con palabras validas" + "\n" + "\033[0m")
                Menu()

            if validar(palabras):  # Si la oracion es valida
                print("\033[;32m" + "\n" +
                      "La oración ingresada es válida" + "\033[0m")
                volverIngresar()

            else:  # Si la oracion no es valida
                print("\033[;31m" + "\n" + "Oración inválida" + "\033[0m")
                volverIngresar()


def main():  # Funcion principal
    Menu()


if __name__ == "__main__":  # Llamado a la funcion principal (buenas practicas)
    main()


#Creado por Juan Esteban y Kevin
