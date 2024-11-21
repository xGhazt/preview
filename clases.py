import random

# Adenina (A), Timina (T), Citosina (C) y Guanina (G)

def crear_adn():
    bases = ["A", "T", "C", "G"]
    adn = []
    
    for i in range (6):
        fila = ""
        for j in range (6):
            fila = fila + bases[random.randint(0,3)]
        adn.append(fila)   

    return adn

def mostrar_adn(adn):
        print("----------ADN----------")
        for fila in adn:
            print(" ".join(fila))  
        print("-----------------------")

#---------------------------------------------

class Detector:
    def __init__(self, adn):
        self.adn=adn
        self.mutacion=False

    def detectar_mutantes(self):
        
        if (self.detectar_mutacion_horizontal() or
            self.detectar_mutacion_vertical() or
            self.detectar_mutacion_diagonal()):

            print("hay mutacion")

            return self.mutacion
        else: 
            print("no hay mutacion")
            
            return self.mutacion


        
    '''DETECTAR MUTACION HORIZONTAL'''

    def detectar_mutacion_horizontal(self):

        for fila in self.adn:
            print("-------------")
            print(f"analizando fila: {fila}")

            contador=0
            for j in range (5):
                if fila[j] == fila[j+1]:
                    contador += 1
                else:
                    contador=0

                if contador == 3:
                    print("horizontal")
                    return self.mutacion==True
           
        return False       
        
    '''DETECTAR MUTACION VERTICAL'''
    def detectar_mutacion_vertical(self):

        for columna in range(6):
            print("-------------")
            print(f"analizando columna: {columna}")
            contador = 0
            base_anterior = None  

            for fila in self.adn:  
                base = fila[columna] 
                if base == base_anterior:  
                    contador += 1
                else:
                    contador = 0  

                base_anterior = base 
                
                if contador == 3: 
                    print("vertical")
                    return self.mutacion==True
                
        return False


    '''DETECTAR MUTACION DIAGONAL'''

    def detectar_mutacion_diagonal(self):

        '''buscar en diagonales principales(descendentes)'''
        for fila in range(3):  
            for columna in range(3):  
                if (self.adn[fila][columna] == self.adn[fila + 1][columna + 1] ==
                    self.adn[fila + 2][columna + 2] == self.adn[fila + 3][columna + 3]):
                    print("Mutación diagonal principal detectada")
                    
                    return self.mutacion==True

        '''buscar en diagonales secundarias(ascendentes)'''
        
        for fila in range(3, 6):  
            for columna in range(3):  
                if (self.adn[fila][columna] == self.adn[fila - 1][columna + 1] ==
                    self.adn[fila - 2][columna + 2] == self.adn[fila - 3][columna + 3]):
                    print("Mutación diagonal secundaria detectada")

                    return self.mutacion==True

        return False  

            






#---------------------------------------------

'''

class Radiacion(Mutador):
    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        pass

class Virus(Mutador):
    def crear_mutante(self, base_nitrogenada, posicion_inicial):
        pass

class Sanador:
    def __init__(self):
        pass

    def sanar_mutantes(self, adn):
        pass

'''


class Mutador:
    def __init__(self, base_nitrogenada, matriz_adn):
        self.base_nitrogenada = base_nitrogenada
        self.matriz_adn = [list(fila) for fila in matriz_adn]

    def crear_mutante(self):
        pass
    

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn, fila, columna):
        super().__init__(base_nitrogenada, matriz_adn)
        self.fila = fila
        self.columna = columna

    def crear_mutante(self, orientacion):
        """Crea una mutación en la matriz ADN (horizontal o vertical)."""

        
        

        try:
            # Verificar si la posición y la orientación son válidas antes de mutar
            if orientacion == "H":
                if self.columna + 3 >= len(self.matriz_adn[0]):
                    raise IndexError("La mutación horizontal se sale de los límites de la matriz.")
                for i in range(4):
                    self.matriz_adn[self.fila][self.columna + i] = self.base_nitrogenada
            elif orientacion == "V":
                if self.fila + 3 >= len(self.matriz_adn):
                    raise IndexError("La mutación vertical se sale de los límites de la matriz.")
                for i in range(4):
                    self.matriz_adn[self.fila + i][self.columna] = self.base_nitrogenada
            else:
                raise ValueError("Orientación inválida para Radiación. Use 'H' o 'V'.")
        
        except IndexError as e:
            print(f"Error de índice: {e}")
        except ValueError as e:
            print(f"Error de valor: {e}")
        
        return self.matriz_adn

class Virus(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn, fila, columna):
        super().__init__(base_nitrogenada, matriz_adn)
        self.fila = fila
        self.columna = columna

    def crear_mutante(self):

        """Crea una mutación diagonal (2 direcciones) en la matriz ADN."""

        try:
            # Verificar si la posición es válida antes de realizar la mutación diagonal
            if self.fila + 3 >= len(self.matriz_adn) or self.columna + 3 >= len(self.matriz_adn[0]):
                raise IndexError("La mutación diagonal se sale de los límites de la matriz.")
            
            # Realizar la mutación diagonal
            for i in range(4):
                self.matriz_adn[self.fila + i][self.columna + i] = self.base_nitrogenada

        except IndexError as e:
            print(f"Error de índice: {e}")
        
        return self.matriz_adn




# Crear ADN de ejemplo (6x6)
import random

def crear_adn():
    bases = ["A", "T", "C", "G"]
    adn = []
    for _ in range(6):
        fila = "".join(random.choice(bases) for _ in range(6))
        adn.append(list(fila))  # Convertir a lista de caracteres
    return adn

# Prueba de la mutación

# Crear ADN

'''

adn = crear_adn()
print("ADN inicial:")
for fila in adn:
    print("".join(fila))

'''

adn = ["GGATCA", "GATTCA", "CAACAT", "AAGAAT", "ATTGCG", "CGTTGT"]

mostrar_adn(adn)
# Crear una mutación de radiación horizontal
mutador_radiacion = Radiacion(base_nitrogenada="G", matriz_adn=adn, fila=0, columna=0)
adn_mutado_radiacion = mutador_radiacion.crear_mutante("H")

print("\nADN mutado (Radiación Horizontal):")
for fila in adn_mutado_radiacion:
    print("".join(fila))

# Crear una mutación de virus (diagonal)
mutador_virus = Virus(base_nitrogenada="C", matriz_adn=adn, fila=0, columna=0)
adn_mutado_virus = mutador_virus.crear_mutante()

print("\nADN mutado (Virus - Diagonal):")
for fila in adn_mutado_virus:
    print("".join(fila))





'''
ejemplo = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]

mutante_horizontal = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]

mutante_vertical = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]

adn = ["TGATCA", "GAAGCA", "CTCCAC", "CAGATA", "GTAGCC", "CAGTTC"]


'''


adn = ["GGATCA", "GATTCA", "CAACAT", "AAGAAT", "ATTGCG", "CGTTGT"]


mostrar_adn(adn)

detector = Detector(adn)

detector.detectar_mutantes()

'''


adn = crear_adn()

adn.mostrar_adn()

'''

















































'''
class ADN:
    def __init__(self, adn):
        self.adn = adn
        print("-----------------------")
        print(adn)

    def mostrar_adn(self):
        print("----------ADN----------")
        for fila in self.adn:
            print(" ".join(fila))  

'''