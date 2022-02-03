class  Pawns:
    
    """
    En esta clase se recreará el juego Pawns
    """
    points = {"A": 1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":5,"L":1,
              "M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}
    
    def __init__(self):
        """
        El contructor le dará el atributo letters al objeto.
        """
        self.letters = []

    
    def addPawn(self,c = ""):
        """
        Este método agregará el valor de c a letters
        c = caracter str
        """
        assert type(c) == str and len(c) == 1, "c tiene que ser un solo carater str"
        c = c.upper()
        self.letters.append(c)
        return 


    def addPawns(self,c="",n=1):
        """
        Método que agrega n veces el caracter c.
        n = int igual o mayor a 1.
        c = caracter str
        """
        if not type(c) is str and not type(n) is int:
            raise TypeError("c debe ser caracter str y n debe ser entero.")
        elif len(c) != 1 or n<1:
            raise ValueError("c debe ser solo un caracter y n debe ser mayor o igual a 1.")
        c = c.upper()
        for _ in range(n):
            self.addPawn(c)
    @property
    def createBag(self):
        """
        creará las fichas descritas en el enunciado
        """
        import pandas as pd
        df = pd.read_csv("F:/CARPETAS/Cursos/Python/proyecto/bag_of_pawns.csv")
        filas , c = df.shape
        for i in range(filas):
            self.addPawns(df["Letter"][i],df["Count"][i])
        return 
    
    @property
    def showPawns(self):
        obj = self.getFrequency
        obj.showFrecuency
    
    @property
    def takeRandomPawn(self):
        """
        saca una ficha de la bolsa de forma aleatoria
        """
        import numpy as np
        num = np.random.randint(0, len(self.letters))
        c = self.letters.pop(num)
        return c
    
    @property
    def getFrequency(self):
        """
        devuelva un objeto de la clase FrequencyTable con las apariciones de cada ficha del objeto.
        """
        frec = FrequencyTable()
        for e in self.letters:
            frec.update(e)
        return frec
    
    def takePawn(self, c):
        assert type(c) == str and len(c) == 1, "c debe ser un caracter"
        self.letters.remove(c)
        
    @property
    def getTotalPawns(self):
        return len(self.letters)
    
    @staticmethod
    def getPoints(c):
        return Pawns.points[c.upper()]
    @staticmethod
    def showPawnsPoints():
        print("\tLetra\t:\tPuntos")
        for key in Pawns.points:
            print("\t{}\t:\t{}".format(key, Pawns.getPoints(key)))
    
        
        
class Word:
    
    def __init__(self):
        self.word = []
        
    def __str__(self):
        string = ""
        for e in self.word:
            string = string + e
        return string
    
    def areEqual(self , w):
        return self.word == w.word
    
    @property    
    def isEmpty(self):
        return (True if len(self.word) == 0 else False)
    
    @classmethod
    def readWord(cls):
        word = input("Ingresa una palabra sin espacios: ")
        assert (len(word.split()) == 1) or word == "", "Debe ser una palabara sin espacios"
        out = Word()
        for e in word.upper():
            out.word.append(e)
        return out
    
    @staticmethod
    def readWordFromFile(f):
        return list(f.readline())[:-1]
    
    def getFrequency(self):
        frec = FrequencyTable()
        for e in self.word:
            frec.update(e)
        return frec

    def getLengthWord(self):
        return len(self.word)
        
    
    
class Dictionary:
    filepath = "F:/CARPETAS/Cursos/Python/proyecto/dictionary.txt"
    
    @staticmethod
    def validateWord(word):
        with open(Dictionary.filepath , mode = "r") as f:
            resl = False
            while 1:
                w = Word.readWordFromFile(f)
                if w == word.word:
                    resl = True
                    break
                if len(w) == 0:
                    break
        return resl
    
    @staticmethod
    def showWord(pawns):
        with open(Dictionary.filepath , mode = "r") as f:
            word_dic = Word()
            while True:
                word_dic.word = Word.readWordFromFile(f)
                if len(word_dic.word) == 0:
                    break
                elif len(word_dic.word) == 1:
                    continue 
                else:
                    if FrequencyTable.isSubset(word_dic.getFrequency(), pawns.getFrequency):
                        print(word_dic)
                    else:
                        continue
    @staticmethod
    def showWordPlus(pawns, c):
        c = c.upper()
        with open(Dictionary.filepath , mode = "r") as f:
            word_dic = Word()
            pawns.letters.append(c)
            while True:
                word_dic.word = Word.readWordFromFile(f)
                if len(word_dic.word) == 0:
                    pawns.letters.remove(c)
                    break
                elif len(word_dic.word) == 1:
                    continue
                else:
                    if FrequencyTable.isSubset(word_dic.getFrequency(), pawns.getFrequency):
                        if not c in word_dic.word:
                            continue
                        else:
                            print(word_dic)
                    else:
                        continue
                    
            
            
            

class FrequencyTable:
    
    def __init__(self):
        self.letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.frecuencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    @property
    def showFrecuency(self):
        for i in range(len(self.frecuencies)):
            if self.frecuencies[i] != 0:
                print("Frecuencia de letra {} : {}".format(self.letters[i],self.frecuencies[i]))
    
    @staticmethod
    def isSubset(obj1 , obj2):
        """
        recibe dos objetos de la clase FrequencyTable y determina si el primer objeto es subconjunto del segundo.
        Es decir, que las letras del primer objeto están repetidas igual o menos veces que en el segundo objeto.
        """
        resl = True
        for i in range(len(obj1.frecuencies)):
            comp = obj1.frecuencies[i] - obj2.frecuencies[i]
            if comp > 0:
                resl = False
                break
        return resl
    
    def update(self,c):
        c = c.upper()
        assert c in self.letters, "c debe ser una letra"
        self.frecuencies[self.letters.index(c)] += 1
    
class Board:
    
    score = 0
    
    def __init__(self):
        import numpy as np
        l = [" " for _ in range(15)]
        l2= []
        for _ in range(15):
            l2.append(l)
        self.board = np.array(l2)
        self.totalWords = 0
        self.totalPawns = 0
        
    @property
    def showBoard(self):
        
        
        lsep, lnum = "", ""
        for i in range(15):
            lnum += " {}{} ".format("0" if i < 10 else "",i)
            if i <14:
                lsep += "*---"
            else:
                lsep += "*---*"
        print(lnum)
        for i in range(15):
            larray = ""
            print(lsep)
            for j in range(15):
                larray += "| {} {}".format(self.board[i,j], "" if j <14 else "|")
            print(larray + " {}{}".format("0" if i < 10 else "", i))
        print(lsep)
    
    
    def placeWord(self, player_pawns, word, x, y, direction):
        direction = direction.upper()
        

        if direction == "V":

            for i in  range(len(word.word)):
                if self.board[x + i, y] == word.word[i]:
                    continue
                else:
                    self.board[x + i,y] = word.word[i]
                    player_pawns.takePawn(word.word[i])
                    self.totalPawns += 1
                    Board.score += Pawns.getPoints(word.word[i])
            
        else:
            for i in  range(len(word.word)):
                if self.board[x, y+i] == word.word[i]:
                    continue
                else:
                    self.board[x,y+i] = word.word[i]
                    player_pawns.takePawn(word.word[i])
                    self.totalPawns += 1
                    Board.score += Pawns.getPoints(word.word[i])
        self.totalWords += 1
    
    def isPossible(self, word, x, y,direction):
        direction = direction.upper()
        message = ""
        x0 = x
        y0 = y

        # Si es el primer turno, comprobamos si alguna ficha se sitúa sobre la casilla central
        if self.totalWords == 0:
            message = "Ninguna ficha pasa por la casilla central"
            if direction == "V":
                if y0 != 7:
                    return (False, message)
                elif x0 + word.getLengthWord() - 1 < 7 or x0 > 7:
                    return (False, message)
                    
            if direction == "H":
                if x0 != 7:
                    return (False, message)
                elif y0 + word.getLengthWord() - 1 < 7 or y0 > 7:
                    return (False, message)

        else:
            # Comprobamos si la palabra se sale del tablero
            message = "La palabra se sale de los límites del tablero"
            if (x0 < 0 or x0 >= 15 or y0 < 0 or y0 >= 15):
                return (False, message)
            if direction == "V" and x0 + word.getLengthWord() - 1 >= 15:
                return (False, message)
            if direction == "H" and y0 + word.getLengthWord() - 1 >= 15:
                return (False, message)
                
            # Comprobamos si se utiliza alguna ficha del tablero para formar la palabra
            x = x0
            y = y0
            blanks = []
            for c in word.word:
                if self.board[x,y] == " ":
                    blanks.append(c)
                if direction == "V":
                    x += 1
                if direction == "H":
                    y += 1
                
            if len(blanks) == word.getLengthWord():
                message = "No se está utilizando ninguna ficha del tablero"
                return (False, message)

            # Comprobamos si la casilla está libre u ocupada por la misma letra
            x = x0
            y = y0
            for c in word.word:
                if self.board[x,y] != " " and self.board[x,y] != c:
                    message = "Hay una ficha diferente ocupando una posición"
                    return (False, message)
                if direction == "V":
                    x += 1
                if direction == "H":
                    y += 1
                    
            # Comprobamos si se coloca una nueva ficha en el tablero
            x = x0
            y = y0
            matching = []
            for c in word.word:
                if self.board[x,y] == c:
                    matching.append(c)
                if direction == "V":
                    x += 1
                if direction == "H":
                    y += 1
                
            if len(matching) == word.getLengthWord():
                message = "No se está colocando ninguna ficha nueva en el tablero"
                return (False, message)
            
                
            # Comprobamos que no hay fichas adicionales a principio y final de palabra
            message = "Hay fichas adicionales a principio o final de palabra"
            x = x0
            y = y0
            if direction == "V" and ((x != 0 and self.board[x - 1,y] != " ") or (x + word.getLengthWord() != 14 and self.board[x + word.getLengthWord(),y] != " ")):
                return (False, message)
            if direction == "H" and ((y != 0 and self.board[x,y - 1] != " ") or (y + word.getLengthWord() != 14 and self.board[x,y + word.getLengthWord()] != " ")):
                return (False, message)
        
        message = "La palabra se puede situar en el tablero"
        return (True, message)
    
    def getPawns(self, word, x,y,direction):
        resl = Word()
        posible , message = self.isPossible(word, x,y,direction)
        word = word.word
        if posible:
            if direction == "V":
                for i in range(len(word)):
                    if self.board[x+i, y] != word[i]:
                        resl.word.append(word[i])
            else:
                for i in range(len(word)):
                    if self.board[x, y + i] != word[i]:
                        resl.word.append(word[i])
            return resl
        else:
            print(message)
            
    def showWordPlacement(self, pawns, word):
        print(word)
        x , y = self.board.shape
        for i in range(x):
            for j in range(y):
                if self.isPossible(word,i,j,"V")[0]:
                    get_pawns = self.getPawns(word,i,j,"V")
                    if FrequencyTable.isSubset(get_pawns.getFrequency(), pawns.getFrequency):
                        
                        print("Posición: ({},{}), dirección: 'V'".format(i,j))
        for i in range(x):
            for j in range(y):
                if self.isPossible(word,i,j,"H")[0]:
                    get_pawns = self.getPawns(word,i,j,"H")
                    if FrequencyTable.isSubset(get_pawns.getFrequency(), pawns.getFrequency):
                        
                        print("Posición: ({},{}), dirección: 'H'".format(i,j))

class Main_Ayuda:
    
    def helper_welcome():
        with open("F:/CARPETAS/Cursos/Python/proyecto/welcome_message.txt" , mode = "r") as f:
            for line in f.readlines():
                print(line)
    def helper_intructions():
        with open("F:/CARPETAS/Cursos/Python/proyecto/instructions_message.txt" , mode = "r") as f:
            for line in f.readlines():
                print(line)
    def help_ayuda():
        ayuda = input("¿Necesitas ayuda?\nPresiona la tecla 'h' por ayuda: ")
        if ayuda == "h" or ayuda == "H":
            print("1 -> Para saber que palabras se pueden formar con tus fichas.")
            print("2 -> Para saber que palabras se pueden formar con tus fichas utilizando una letra del tablero.")
            print("3 -> Para saber en donde puedes colocar alguna palabra.")
            option  = int(input("Opción: "))
            return option
    def help_palabras(player_pwans, board):
        option = Main_Ayuda.help_ayuda()
        if option == 1:
            Dictionary.showWord(player_pwans)
        elif option == 2:
            letter = input("¿Qué letra deseas utilizar? : ")
            Dictionary.showWordPlus(player_pwans, letter)
        elif option == 3:
            while True:
                word = Word().readWord()
                if Dictionary().validateWord(word):
                    board.showWordPlacement(pawns = player_pwans, word = word)
                    break
                else:
                    print("La palabra no es valida, vuelve a intentarlo.")
            
        
    def S_continuar():
        import os
        flag = input("Presiona cualquier otra tecla para continuar.")
        flag = flag.upper()
        if len(flag) != 0:
            os.system ("cls")
            return
        
    def options_end(player_pwans, board):
        
        while True: 
            print("¿Qué deseas hacer?\n1 -> Continuar con el juego.\n2 -> Consultar tus fichas.\n3 -> Consultar tus puntos\n4 -> Consultar los puntos de alguna ficha.\n5 -> Salir del juego")
            option = int(input())
            if option == 1:
                continuar = True
                return continuar
            elif option == 2:
                print("Tus fichas son:")
                player_pwans.showPawns
            elif option == 3:
                print("Tus puntos son: {}".format(board.score))
            elif option == 4:
                Pawns.showPawnsPoints()
            elif option == 5:
                continuar = False
                return continuar
    
    def play_word(player,board, bag):
    
        word = Word().readWord()
        if Dictionary.validateWord(word):
            if FrequencyTable.isSubset(word.getFrequency(), player.getFrequency):
                print("indica la posición del 0 - 14, filas y columnas y la dirección Vertical 'V' u Horizontal 'H'")
                x = int(input("Filas: "))
                y = int(input("Columnas: "))
                direc = input("Dirección: ")
                is_posible = board.isPossible(word, x, y,direc)
                if is_posible[0]:
                    board.placeWord(player, word, x, y, direc)
                    while player.getTotalPawns < 7:
                        player.addPawn(bag.takeRandomPawn)
                    board.showBoard
                else:
                    print(is_posible[1])
            else:
                print("La palabra no puede ser formada con tus fichas actuales.")
        else:
            print("La palabra no es valida, intentalo de nuevo.\n")
            
            
        
                
    