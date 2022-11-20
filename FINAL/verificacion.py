class verificacion:
    def __init__(self):
        self.articulosDefinidos = ["el", "los", "la", "las"]
        self.articulosIndefinidos = ["un", "uno", "una", "unas", "unos"]
        self.sustantivosImpropios = ["adulto", "adultos", "joven", "jovenes", "perro", "perros", "gato", "gatos", "papá", "papás", ]
        self.sustantivosPropios = ["juan", "lorena", "kevin", "david", "maria", "ana"]
        self.verbos = ["juega", "juegan", "jugaron", "jugarán", "come", "comen", "comieron", "comerán", "canta", "cantan",
                        "cantaron", "cantarán", "salta", "saltan", "saltaron", "saltarán", "corren",  "corre", "corrió", "correrán"]
        self.adjetivos = ["grande", "feo", "malo", "bueno",
                        "divertido", "rapido", "bonito", "duro"]
        self.adverbios = ["muy", "demasiado", "poco", "bastante", "mucho", "poco", "bien", "mal", "divertido", "rapido", "bonito", "duro"]
        self.enlace = ["con"]
        self.palabrasTotal = self.articulosDefinidos + self.articulosIndefinidos + self.sustantivosImpropios + self.sustantivosPropios + self.verbos + self.adjetivos + self.adverbios + self.enlace
        self.listIndex = []  # Lista que almacena los indices de las palabras

    def verificacion1(self,palabras):  
        if (self.sustantivosPropios.__contains__(palabras[0].lower()) or self.articulosDefinidos.__contains__(palabras[0].lower()) and self.verbos.__contains__(palabras[1].lower())):
            return True
        else:
            return False


    def verificacion2(self,palabras): 
        if (self.articulosDefinidos.__contains__(palabras[0].lower()) or self.articulosIndefinidos.__contains__(palabras[0].lower()) and self.sustantivosImpropios.__contains__(palabras[1].lower()) and self.verbos.__contains__(palabras[2].lower())):
            return True
        else:
            return False


    def verificacion3(self,palabras): 
        if (self.articulosIndefinidos.__contains__(palabras[0].lower()) and self.sustantivosImpropios.__contains__(palabras[1].lower()) and self.verbos.__contains__(palabras[2].lower())):
            return True
        else:
            return False

    def verificacion4(self,palabras):  
        if (self.articulosDefinidos.__contains__(palabras[0].lower()) or self.articulosIndefinidos.__contains__(palabras[0].lower()) and self.sustantivosImpropios.__contains__(palabras[1].lower()) and self.verbos.__contains__(palabras[2].lower()) and self.adjetivos.__contains__(palabras[3].lower())):
            return True
        else:
            return False
        
    def verificacion5(self,palabras):  
        if (self.sustantivosPropios.__contains__(palabras[0].lower()) and self.verbos.__contains__(palabras[1].lower()) and self.adjetivos.__contains__(palabras[2].lower()) or self.adverbios.__contains__(palabras[2].lower())):
            return True
        else:
            return False
        
    def verificacion6(self,palabras): 
        if (self.sustantivosPropios.__contains__(palabras[0].lower()) or self.articulosDefinidos.__contains__(palabras[0].lower()) and self.verbos.__contains__(palabras[1].lower()) and self.adverbios.__contains__(palabras[2].lower()) or self.adjetivos.__contains__(palabras[2].lower())):
            return True
        else:
            return False
        
    def verificacion7(self,palabras): 
        if (self.sustantivosPropios.__contains__(palabras[0].lower()) and self.verbos.__contains__(palabras[1].lower()) and self.enlace.__contains__(palabras[2].lower()) and self.articulosDefinidos.__contains__(palabras[3].lower()) and self.sustantivosImpropios.__contains__(palabras[4].lower()) or self.articulosIndefinidos.__contains__(palabras[4].lower())):
            return True
        else:
            return False
        
    def verificacion8(self,palabras): 
        if (self.articulosDefinidos.__contains__(palabras[0].lower()) or self.articulosIndefinidos.__contains__(palabras[0].lower()) and self.sustantivosImpropios.__contains__(palabras[1].lower()) and self.verbos.__contains__(palabras[2].lower()) and self.enlace.__contains__(palabras[3].lower()) and self.articulosDefinidos.__contains__(palabras[4].lower()) or self.articulosIndefinidos.__contains__(palabras[4].lower()) and self.sustantivosImpropios.__contains__(palabras[5].lower())):
            return True
        else:
            return False
        


    def verificacionVerbo(self,palabras): #Verifica que el verbo esté solo una vez
        c = 0
        for x in palabras:
         if x in self.verbos:
            c+=1
        if c >= 2:
         return False
        else:
         return True
        
    def verificacionAdjetivo(self,palabras): #Verifica que el adjetivo esté solo una vez
        c = 0
        for x in palabras:
            if x in self.adjetivos:
                c+=1
        if c >= 2:
            return False
        else:
            return True
        
    def verificacionAdverbio(self,palabras): #Verifica que el adverbio esté solo una vez
        c = 0
        for x in palabras:
            if x in self.adverbios:
                c+=1
        if c >= 2:
            return False
        else:
            return True
        

    def validar(self,palabras):  # Valida que las palabras cumplan las reglas (verificaciones)
        if (self.verificacionAdjetivo(palabras) != True):
            return False
        if (self.verificacionAdverbio(palabras) != True):
            return False
        if(self.verificacionVerbo(palabras) != True):
         return False
        elif (self.verificacionVerbo(palabras)  or self.verificacionAdverbio(palabras) or self.verificacionAdjetivo(palabras) or self.verificacion1(palabras) or self.verificacion2(palabras) or self.verificacion3(palabras) or self.verificacion4(palabras) or self.verificacion5(palabras) or self.verificacion6(palabras) or self.verificacion7(palabras) or self.verificacion8(palabras)):
            return True
        else:
            return False


    def basePalabras(self,palabras):  # Funcion que almacena las palabras en una lista
        variable = True
        for i in palabras:
            if i not in self.palabrasTotal:
                variable = False
        return variable