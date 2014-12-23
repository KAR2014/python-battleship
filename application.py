# -*- coding: utf-8 -*-
"""BattleShip 3.0 """
import random
import os
import sys
import time

#Librerias del reproductor
import pygame.mixer
pygame.mixer.init(44100, -16, 2, 4096)
epica = pygame.mixer.Sound("epica.wav")   # Dura 9 segundos
pixer = pygame.mixer.Sound("inss.wav")
print "Reproduciendo ..."

################################################################
#########               Clase Single_player            #########
################################################################

class _Player(object):
    """Clase de Single Player"""

    def __init__(self):
        """ Iniciamos Variables Globales """
        self.sonido = pygame.mixer.Sound("pirata.wav")
        self.tablero = []
        self.board = []

        #Iniciamos Métodos
        self.armar_tableros()

    def limpiar(self):
        self.tablero = []
        self.board = []


    def armar_tableros(self):
        """ Armamos Tablero 1 """
        for tablero in range(0, 10):
            self.tablero.append(10 * ['♒'])

        for board in range(0, 10):
            self.board.append(10 * ['♒'])

    def print_tablero(self):
        """ Imprimimos Tablero 1 """
        for i in self.tablero:
            print "  ".join(i)

    def print_board(self):
        """ Imprimimos Tablero en Blanco """
        for i in self.board:
            print "  ".join(i)

    def opcion_pos(self):
        """ Definiremos posición Horizontal o Vertical (1/2) """
        return random.randint(1, 2)


    def fila_aleatoria(self):
        """ Fila Aleatoria """
        return random.randint(0, len(self.tablero)-1)

    def columna_aleatoria(self):
        """ Columna Aleatoria """
        return random.randint(0, len(self.tablero[0])-1)

    def validar_horizontal(self, barco_fila, barco_col, contador):
        """Validacion Posicion Horizontal"""
        cont_barcos = 0
        for i in range(0, contador):
            #print  "Contador: " + str(i)
            if self.tablero[barco_fila + i][barco_col] == "⚓":
                #print False
                cont_barcos += 1
            else:
                #print True
                cont_barcos += 0

        if cont_barcos == 0:
            barco_fila = 0
            barco_col = 0
            return 1
        else:
            barco_fila = 0
            barco_col = 0
            return 2

    def validar_vertical(self, barco_fila, barco_col, contador):
        """Validacion posicion Vertical"""
        cont_barcos = 0
        for i in range(0, contador):
            #print  "Contador: " + str(i)
            if self.tablero[barco_fila][barco_col + i] == "⚓":
                #print False
                cont_barcos += 1
            else:
                #print True
                cont_barcos += 0

        if cont_barcos == 0:
            barco_fila = 0
            barco_col = 0
            return 1
        else:
            barco_fila = 0
            barco_col = 0
            return 2

    def colocar_barcos(self):
        '''Posicionando Barcos'''    # Declaramos Sonido del Juego
        print "Reproduciendo ..."
        self.sonido.play(loops=4, maxtime=0, fade_ms=0)
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               BattleShip Single Player              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero()
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠             BattleShip Colocando Barcos             ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        kar1 = 0
        kar2 = 0
        kar3 = 0
        kar4 = 0
        kar5 = 0
        validar_h = 0
        validar_v = 0
        barco = 5
        print "\n                    ☠☠☠☠☠☠ 5. Remolcadores ☠☠☠☠☠☠"

        #Barcos de 5
        while kar5 < 2:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 5 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        kar5 += 1
                    elif validar_h == 2:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_fil > 5:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 5 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco)
                    if validar_v == 1:
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        kar5 += 1
                    elif validar_v == 2:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                elif bar_col > 5:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              5. Remolcadores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 4
        time.sleep(1)

        print "\n                    ☠☠☠☠☠☠ 4. Destructores ☠☠☠☠☠☠"
        #Barcos de 4
        while kar4 < 1:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 6 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print "Destructor # "+ str(kar4 + 1) + " Colocado"
                        for i in range(0, 4):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        kar4 += 1
                    elif validar_h == 2:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                elif bar_fil > 6:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 6 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco)
                    if validar_v == 1:
                        print "Destructor #"+ str(kar4 + 1) +" Colocado"
                        for i in range(0, 4):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        kar4 += 1
                    elif validar_v == 2:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                elif bar_col > 6:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              4. Destructores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 3
        time.sleep(1)


        print "\n                    ☠☠☠☠☠☠ 3. Fragatas ☠☠☠☠☠☠"

        #Barcos de 3
        while kar3 < 1:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 7 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print "Fragata #"+ str(kar3 + 1) +" Colocado"
                        for i in range(0, 3):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        kar3 += 1
                    elif validar_h == 2:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                elif bar_fil > 7:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 7 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco)
                    if validar_v == 1:
                        print "Fragata #"+ str(kar3 + 1) + " Colocado"
                        for i in range(0, 3):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        kar3 += 1
                    elif validar_v == False:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                elif bar_col > 7:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                3. Fragatas Colocados                ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 2
        time.sleep(1)

        print "\n                    ☠☠☠☠☠☠ 2. Patrulleros ☠☠☠☠☠☠"

        #Barcos de 2
        while kar2 < 2:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 8 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print "Patrullero #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        kar2 += 1
                    elif validar_h == 2:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                elif bar_fil > 8:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 8 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco)
                    if validar_v == 1:
                        print "Patrullero #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        kar2 += 1
                    elif validar_v == 2:
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                elif bar_col > 8:
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               2. Patrulleros Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 1
        time.sleep(1)


        print "\n                    ☠☠☠☠☠☠ 1. Submarinos ☠☠☠☠☠☠"

        #Barcos de 1
        while kar1 < 3:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            time.sleep(1)

            validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
            validar_v = self.validar_vertical(bar_fil, bar_col, barco)
            if validar_h == 1 and validar_v == 1:
                print "Submarino #"+ str(kar1 + 1) + " Colocado"
                self.tablero[bar_fil][bar_col] = "⚓"
                kar1 += 1
            elif validar_h == 2 and validar_v == 2:
                print "Lo Sentimos Hay un Barco en esa Posición"
                print "Restableciedo Coordenadas Espere ... ⌛"
                time.sleep(1)
                os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                1. Submarinos Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 0
        time.sleep(1)

        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               BattleShip: Ships in Board            ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero()

        time.sleep(1)

    def start_single(self):
        """Inicia el Single Player"""
        nombre = ""
        repetir = "si"
        while repetir == "si":
            explosion = pygame.mixer.Sound("ex.wav")
            while True:
                nombre = raw_input("Ingrese su Nombre: ")
                nombre = nombre.title()
                try:
                    nombre = float(nombre)
                    nombre = int(nombre)
                    print u"Debe ingresar un nombre válido\n"
                except(RuntimeError, NameError, ValueError):
                    if (len(nombre) <= 2):
                        print u"Debe ingresar un nombre válido\n"
                    else:
                        nombre = nombre
                        break

            self.colocar_barcos()
            os.system("clear")
            score = 0
            respuesta = 0
            repetido = 0
            asierto1 = 0
            asierto2 = 0
            adiv_fil = 0
            adiv_col = 0
            turno = 0
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print " ☠☠☠☠                  BattleShip: Start Game             ☠☠☠☠ "
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"

            while turno < 5:#¡De aquí en adelante todo debería ir en tu bucle for!
                #¡Asegúrate de indentar!
                while True:
                    print "Turno:", (turno +1)# ¡Muestra (turno + 1) aquí!
                    print
                    self.print_board()
                    print "\n"
                    adiv_fil = 0
                    adiv_col = 0
                    adiv_fil = raw_input("Adivina fila: ")#fila
                    adiv_col = raw_input("Adivina columna: ")#Columna
                    try:
                        adiv_fil = int(adiv_fil)
                        adiv_col = int(adiv_col)
                        if adiv_fil >= 0 and adiv_col >= 0:
                            break
                        else:
                            print "Ingrese coordenadas válidas\n"
                            time.sleep(1)
                            os.system("clear")
                    except(RuntimeError, TypeError, NameError, ValueError):
                        print "Ingrese coordenadas válidas\n"
                        time.sleep(1)
                        os.system("clear")
                if (adiv_fil >= 0 and adiv_fil <= 9) and (adiv_col >= 0 and adiv_col <= 9):
                    #fuera oceano
                    if (self.board[adiv_fil][adiv_col] == "☠" and asierto1 > 0) or (self.board[adiv_fil][adiv_col] == "X" and asierto2 > 0) :
                        print "Ya dijiste esa."
                        self.print_board()

                        #hundiendo barco
                    elif self.tablero[adiv_fil][adiv_col] == "⚓":
                        print "¡Felicitaciones! ¡Hundiste mi barco!"
                        score += 10
                        asierto1 += 1
                        explosion.play()
                        self.board[adiv_fil][adiv_col] = "☠"
                        self.print_board()

                    else:
                        #No impacte el barco
                        print "¡No impactaste mi barco!"
                        self.board[adiv_fil][adiv_col] = "X"
                        self.print_board()
                        asierto2 +=1
                    #Tiro Repetido    
                if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                        print "Vaya, esto ni siquiera está en el océano."
                        asierto1 += 1
                        asierto2 += 1
                        self.print_board()
                turno += 1
                #contador de turnos
                if turno == 5:
                    print "Terminó el juego"
                    #Contador de puntaje
                    if score == 40 or score == 50:
                        print "Felcitaciones "+ nombre +" Has Ganado"
                        print "Puntaje Final: ", (score)
                    elif score == 30:
                        print nombre + " Muy Bien Marino "
                        print "Puntaje Final: ", (score)
                    elif score <= 20:
                        print nombre + " Fatal Como Capitán eres Pésimo"
                        print "Puntaje Final: ", (score)
                time.sleep(2)
                os.system("clear")

            while True:
                repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                repetir = repetir.lower()
                try:
                    if repetir == "no":
                        self.sonido.stop()
                        os.system("clear")
                        menu()
                    elif repetir == "si":
                        self.sonido.stop()
                        time.sleep(1)
                        self.limpiar()
                        self.armar_tableros()
                        os.system("clear")
                        self.start_single()

                    else:
                        print "Error de ingreso"
                        time.sleep(1)
                        os.system("clear")
                except(RuntimeError, TypeError, NameError, ValueError):
                    os.system("clear")

################################################################
#########               Clase Multiplayer             ##########
################################################################

class _Multi_Player(object):
    """Clase de _Multi_Player"""

    def __init__(self):
        """ Iniciamos Variables Globales """
        self.up = pygame.mixer.Sound("up.wav")
        self.explosion = pygame.mixer.Sound("ex.wav")
        self.tablero_J1 = []
        self.tablero_J2 = []
        self.board_J1 = []
        self.board_J2 = []
   
        #Iniciamos Métodos
        self.armar_tableros()

    def limpiar(self):
        self.tablero_J1 = []
        self.tablero_J2 = []
        self.board_J1 = []
        self.board_J2 = []
        
    def armar_tableros(self):
        """ Armamos Tablero 1 y 2 """
        for tablero in range(0, 10):
            self.tablero_J1.append(10 * ['♒'])

        for tablero in range(0, 10):
            self.tablero_J2.append(10 * ['♒'])

        for board in range(0, 10):
            self.board_J1.append(10 * ['♒'])

        for board in range(0, 10):
            self.board_J2.append(10 * ['♒'])

    def print_tablero(self, tablero):
        """ Imprimimos Tablero 1 """
        for i in tablero:
            print "  ".join(i)

    def print_board(self, board):
        """ Imprimimos Tablero en Blanco player 1 """
        for i in board:
            print "  ".join(i)

    def opcion_pos(self):
        """ Definiremos posición Horizontal o Vertical (1/2) """
        position = 0
        while True:
            position = raw_input("Indique Posicion del Barco: \n1. Vertical \n2. Horizontal\n\n")
            try:
                position = int(position)
                if position == 1 or position == 2:
                    break
                else:
                    print "Error Ingreso Incorrecto\n"
                    time.sleep(1)
                    os.system("clear")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("clear")
        return position


    def fila_player(self):
        """ Fila Player """
        fila = 0
        while True:
            fila = raw_input("Indica Fila: ")
            try:
                fila = int(fila)
                if fila >= 0 and fila <= 9:
                    break
                else:
                    print "¡Error! Coordenada Incorrecta\n"
                    time.sleep(1)
                    os.system("clear")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("clear")
        return fila

    def columna_player(self):
        """ Columna Player """
        columna = 0
        while True:
            columna = raw_input("Indica Columna: ")
            try:
                columna = int(columna)
                if columna >= 0 and columna <= 9:
                    break
                else:
                    print "¡Error! Coordenada Incorrecta\n"
                    time.sleep(1)
                    os.system("clear")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("clear")
        return columna

    def numero_barcos(self):
        """ Cantidad de Barcos """
        ship = 0
        while True:
            ship = raw_input("¿Cuantos Barcos Desea? ")
            try:
                ship = int(ship)
                if ship > 0:
                    break
                else:
                    print "Error Ingreso Incorrecto\n"
                    time.sleep(1)
                    os.system("clear")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("clear")
        return ship

    def validar_horizontal(self, barco_fila, barco_col, contador, tablero):
        """Validacion Posicion Horizontal"""

        cont_barcos = 0
        for i in range(0, contador):
            #print  "Contador: " + str(i)
            if tablero[barco_fila + i][barco_col] == "⚓":
                #print False
                cont_barcos += 1
            else:
                #print True
                cont_barcos += 0

        if cont_barcos == 0:
            barco_fila = 0
            barco_col = 0
            return 1
        else:
            barco_fila = 0
            barco_col = 0
            return 2

    def validar_vertical(self, barco_fila, barco_col, contador, tablero):
        """Validacion posicion Vertical"""

        cont_barcos = 0
        for i in range(0, contador):
            #print  "Contador: " + str(i)
            if tablero[barco_fila][barco_col + i] == "⚓":
                #print False
                cont_barcos += 1
            else:
                #print True
                cont_barcos += 0

        if cont_barcos == 0:
            barco_fila = 0
            barco_col = 0
            return 1
        else:
            barco_fila = 0
            barco_col = 0
            return 2

    def colocar_barcos_players(self, tablero, player):
        '''Posicionando Barcos'''    # Declaramos Sonido del Juego
        print "Reproduciendo ..."
        os.system("clear")
        board = []
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠             BattleShip Tablero: Jugador ",player,"         ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(tablero)
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠             BattleShip Colocando Barcos             ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        kar1 = 0
        kar2 = 0
        kar3 = 0
        kar4 = 0
        kar5 = 0
        cant_barcos = 0
        validar_h = 0
        validar_v = 0
        barco = 5
        while True:
            print "\n                    ☠☠☠☠☠☠ 5. Remolcadores ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if barco == 5:
                if (cant_barcos > 0) and (cant_barcos <= 3):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 3 barcos!"
                    time.sleep(1)
                    os.system("clear")

        #Barcos de 5
        while kar5 < cant_barcos:
            bar_fil = self.fila_player()
            bar_col = self.columna_player()
            print "FILA: " + str(bar_fil)
            print "COLUMNA: " + str(bar_col) + "\n"
            opcion = self.opcion_pos()
            print "Posición: "+ str(opcion)
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 5 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco, tablero)
                    if validar_h == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        kar5 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_h == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_fil > 5:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 5 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco, tablero)
                    if validar_v == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        kar5 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_v == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_col > 5:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              5. Remolcadores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(tablero)
        bar_fil = 0
        bar_col = 0 
        opcion = 0
        barco = 4
        time.sleep(1)

        while True:
            print "\n                    ☠☠☠☠☠☠ 4. Destructores ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if barco == 4:
                if (cant_barcos > 0) and (cant_barcos <= 4):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 4 barcos!"
                    time.sleep(1)
                    os.system("clear")

        #Barcos de 4
        while kar4 < cant_barcos:
            bar_fil = self.fila_player()
            bar_col = self.columna_player()
            print "FILA: " + str(bar_fil)
            print "COLUMNA: " + str(bar_col) + "\n"
            opcion = self.opcion_pos()
            print "Posición: "+ str(opcion)
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 6 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco, tablero)
                    if validar_h == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar4 + 1) + " Colocado"
                        for i in range(0, 4):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        kar4 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_h == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_fil > 6:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 6 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco, tablero)
                    if validar_v == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar4 + 1) + " Colocado"
                        for i in range(0, 4):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        kar4 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_v == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_col > 6:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              4. Destructores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(tablero)
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 3
        time.sleep(1)


        while True:
            print "\n                    ☠☠☠☠☠☠ 3. Fragatas ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if barco == 3:
                if (cant_barcos > 0) and (cant_barcos <= 6):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 6 barcos!"
                    time.sleep(1)
                    os.system("clear")

        #Barcos de 3
        while kar3 < cant_barcos:
            bar_fil = self.fila_player()
            bar_col = self.columna_player()
            print "FILA: " + str(bar_fil)
            print "COLUMNA: " + str(bar_col) + "\n"
            opcion = self.opcion_pos()
            print "Posición: "+ str(opcion)
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 7 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco, tablero)
                    if validar_h == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar3 + 1) + " Colocado"
                        for i in range(0, 3):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        kar3 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_h == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_fil > 7:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 7 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco, tablero)
                    if validar_v == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar3 + 1) + " Colocado"
                        for i in range(0, 3):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        kar3 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_v == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_col > 7:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                3. Fragatas Colocados                ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(tablero)
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 2
        time.sleep(1)

        while True:
            print "\n                    ☠☠☠☠☠☠ 2. Patrulleros ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if barco == 2:
                if (cant_barcos > 0) and (cant_barcos <= 10):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 10 barcos!"
                    time.sleep(1)
                    os.system("clear")

        #Barcos de 2
        while kar2 < cant_barcos:
            bar_fil = self.fila_player()
            bar_col = self.columna_player()
            print "FILA: " + str(bar_fil)
            print "COLUMNA: " + str(bar_col) + "\n"
            opcion = self.opcion_pos()
            print "Posición: "+ str(opcion)
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 8 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco, tablero)
                    if validar_h == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        kar2 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_h == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_fil > 8:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif opcion == 2:
                if bar_col <= 8 and bar_fil <= 9:
                    validar_v = self.validar_vertical(bar_fil, bar_col, barco, tablero)
                    if validar_v == 1:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Remolcador #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        kar2 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif validar_v == 2:
                        print "FILA: " + str(bar_fil)
                        print "COLUMNA: " + str(bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif bar_col > 7:
                    print "FILA: " + str(bar_fil)
                    print "COLUMNA: " + str(bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               2. Patrulleros Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(tablero)
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 1
        time.sleep(1)


        while True:
            print "\n                    ☠☠☠☠☠☠ 1. Submarinos ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if barco == 1:
                if (cant_barcos > 0) and (cant_barcos <= 15):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 15 barcos!"
                    time.sleep(1)
                    os.system("clear")

        #Barcos de 1
        while kar1 < cant_barcos:
            bar_fil = self.fila_player()
            bar_col = self.columna_player()
            print "FILA: " + str(bar_fil)
            print "COLUMNA: " + str(bar_col)
            time.sleep(1)

            validar_h = self.validar_horizontal(bar_fil, bar_col, barco, tablero)
            validar_v = self.validar_vertical(bar_fil, bar_col, barco, tablero)
            if validar_h == 1 and validar_v == 1:
                print "FILA: " + str(bar_fil)
                print "COLUMNA: " + str(bar_col)
                print "Submarino #"+ str(kar1 + 1) + " Colocado"
                tablero[bar_fil][bar_col] = "⚓"
                kar1 += 1
                raw_input("Presione Enter para Continuar ...")
            elif validar_h == 2 and validar_v == 2:
                print "FILA: " + str(bar_fil)
                print "COLUMNA: " + str(bar_col)
                print "Lo Sentimos Hay un Barco en esa Posición"
                print "Restableciedo Coordenadas Espere ... ⌛"
                time.sleep(1)
                os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                1. Submarinos Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        bar_fil = 0
        bar_col = 0
        opcion = 0
        barco = 0
        time.sleep(1)

        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               BattleShip: Ships in Board            ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(tablero)

        time.sleep(1)
        board = tablero
        tablero = []
        return board

    def play_j1(self, turno, score, nombre1, nombre2):
        """ Jugador 1 """
        repetido = 0
        while True:
            print "Turno:", (turno +1)# ¡Muestra (turno + 1) aquí!
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero",nombre1
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.tablero_J1)
            print "\n"
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero",nombre2
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.board_J2)
            print "\n"

            adiv_fil = raw_input("Adivina fila: ")#fila
            adiv_col = raw_input("Adivina columna: ")#Columna
            try:
                adiv_fil = int(adiv_fil)
                adiv_col = int(adiv_col)
                if adiv_fil >= 0 and adiv_col >= 0:
                    break
                else:
                    print "Ingrese coordenadas válidas\n"
                    time.sleep(1)
                    os.system("clear")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese coordenadas válidas\n"
                time.sleep(1)
                os.system("clear")
        if (adiv_fil >= 0 and adiv_fil <= 9) and (adiv_col >= 0 and adiv_col <= 9):
            #tiro repetido
            if (self.board_J2[adiv_fil][adiv_col] == "☠") or (self.board_J2[adiv_fil][adiv_col] == "X"):
                print "Ya dijiste esa."
                self.print_board(self.board_J2)
                #hundiendo barco
            elif self.tablero_J2[adiv_fil][adiv_col] == "⚓":
                print "¡Felicitaciones! ¡Hundiste mi barco!"
                score += 10
                self.explosion.play()
                self.board_J2[adiv_fil][adiv_col] = "☠"
                self.tablero_J2[adiv_fil][adiv_col] = "☠"
                self.print_board(self.board_J2)

            else:
                #No impacte el barco
                print "¡No impactaste mi barco!"
                self.board_J2[adiv_fil][adiv_col] = "X"
                self.tablero_J2[adiv_fil][adiv_col] = "X"
                self.print_board(self.board_J2)
        else:
            #fuera oceano
            if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                repetido += 1
                print "Vaya, esto ni siquiera está en el océano."
                self.print_board(self.board_J2)
        time.sleep(2)
        os.system("clear")
        return score

    def play_j2(self, turno, score, nombre1, nombre2):
        """ Jugador 2 """
        repetido = 0
        while True:
            print "Turno:", (turno +1)# ¡Muestra (turno + 1) aquí!
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero",nombre2
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.tablero_J2)
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero",nombre1
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.board_J1)
            print "\n"

            adiv_fil = raw_input("Adivina fila: ")#fila
            adiv_col = raw_input("Adivina columna: ")#Columna
            try:
                adiv_fil = int(adiv_fil)
                adiv_col = int(adiv_col)
                if adiv_fil >= 0 and adiv_col >= 0:
                    break
                else:
                    print "Ingrese coordenadas válidas\n"
                    time.sleep(1)
                    os.system("clear")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese coordenadas válidas\n"
                time.sleep(1)
                os.system("clear")
        #hundiendo barco
        if (adiv_fil >= 0 and adiv_fil <= 9) and (adiv_col >= 0 and adiv_col <= 9):
            #tiro repetido
            if (self.board_J1[adiv_fil][adiv_col] == "☠" ) or (self.board_J1[adiv_fil][adiv_col] == "X"):
                print "Ya dijiste esa."
                self.print_board(self.board_J1)
            elif self.tablero_J1[adiv_fil][adiv_col] == "⚓":
                print "¡Felicitaciones! ¡Hundiste mi barco!"
                score += 10
                self.explosion.play()
                self.board_J1[adiv_fil][adiv_col] = "☠"
                self.tablero_J1[adiv_fil][adiv_col] = "☠"
                self.print_board(self.board_J1)

            else:
                #No impacte el barco
                print "¡No impactaste mi barco!"
                self.board_J1[adiv_fil][adiv_col] = "X"
                self.tablero_J1[adiv_fil][adiv_col] = "X"
                self.print_board(self.board_J1)
        else:
            #fuera oceano
            if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                repetido += 1
                print "Vaya, esto ni siquiera está en el océano."
                self.print_board(self.board_J1)
        time.sleep(2)
        os.system("clear")
        return score

    def start_players(self):
        """Inicia el Multi_Player"""
        self.up.play(loops=5, maxtime=0, fade_ms=0)
        self.nombre1 = ""
        self.nombre2 = ""
        score = 0
        adiv_fil = 0
        adiv_col = 0
        cont_J1 = 0
        cont_J2 = 0
        puntaje_J1 = 0
        puntaje_J2 = 0
        repetir = "si"
        while repetir == "si":
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print " ☠☠☠☠                BattleShip Multi-Player              ☠☠☠☠ "
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            while True:
                print "Jugador 1: \n"
                self.nombre1 = raw_input("Ingrese su Nombre: ")
                self.nombre1 = self.nombre1.title()
                try:
                    self.nombre1 = float(self.nombre1)
                    self.nombre1 = int(self.nombre1)
                    print u"Debe ingresar un nombre válido\n"
                except(RuntimeError, NameError, ValueError):
                    if (len(self.nombre1) <= 2):
                        print u"Debe ingresar un nombre válido\n"
                    else:
                        self.nombre1 = self.nombre1
                        break
            while True:
                print "\n\nJugador 2: \n"
                self.nombre2 = raw_input("Ingrese su Nombre: ")
                self.nombre2 = self.nombre2.title()
                try:
                    self.nombre2 = float(self.nombre2)
                    self.nombre2 = int(self.nombre2)
                    print u"Debe ingresar un nombre válido\n"
                except(RuntimeError, NameError, ValueError):
                    if (len(self.nombre2) <= 2):
                        print u"Debe ingresar un nombre válido\n"
                    else:
                        self.nombre2 = self.nombre2
                        break
            print "             ☠☠☠☠☠☠☠☠☠☠☠☠☠☠ ",self.nombre1," ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠"
            raw_input("Presione Enter para Continuar ...")
            self.tablero_J1 = self.colocar_barcos_players(self.tablero_J1, self.nombre1)
            os.system("clear")

            print "             ☠☠☠☠☠☠☠☠☠☠☠☠☠☠ ",self.nombre2," ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠"
            raw_input("Presione Enter para Continuar ...")
            self.tablero_J2 = self.colocar_barcos_players(self.tablero_J2, self.nombre2)
            os.system("reset")
            turno = 0

            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print " ☠☠☠☠                  BattleShip: Start Game             ☠☠☠☠ "
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"

            while turno < 5:#¡De aquí en adelante todo debería ir en tu bucle for!

                cont_J1 = self.play_j1(turno, score, self.nombre1, self.nombre2) 
                cont_J2 = self.play_j2(turno, score, self.nombre1, self.nombre2)
                puntaje_J1 += cont_J1
                puntaje_J2 += cont_J2

                turno += 1
                #contador de turnos
                if turno == 5:
                    print "Terminó el juego"
                    print "Puntaje Jugador 1: "+ str(puntaje_J1)
                    print "Puntaje Jugador 2: "+ str(puntaje_J2)

                    if puntaje_J1 > puntaje_J2:
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
                        print "         ¡Felicitaciones! ",self.nombre1," ¡Has Ganado!      "
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
                    elif puntaje_J2 > puntaje_J1:
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
                        print "         ¡Felicitaciones! ",self.nombre2," ¡Has Ganado!       "
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
                    elif puntaje_J1 == puntaje_J2:
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
                        print " ☠☠☠☠           ¡Excelente Marinos han Empatado!          ☠☠☠☠ "
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            while True:
                repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                repetir = repetir.lower()
                try:
                    if repetir == "no":
                        self.up.stop()
                        os.system("clear")
                        menu()
                    elif repetir == "si":
                        self.up.stop()
                        time.sleep(1)
                        self.limpiar()
                        self.armar_tableros()
                        os.system("clear")
                        self.start_players()

                    else:
                        print "Error de ingreso"
                        time.sleep(1)
                        os.system("clear")
                except(RuntimeError, TypeError, NameError, ValueError):
                    os.system("clear")


################################################################
#########                   Clase Menu                ##########
################################################################


def instrucciones():
    epica.stop()
    pixer.play(loops=4, maxtime=0, fade_ms=0)
    os.system("reset")
    print "Bienvenido a las Instrucciones"
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "        
    print " ☠☠☠☠                  BattleShip: Instrucciones          ☠☠☠☠ "
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"

    print """Batalla Naval es un juego donde debes 
            asertar la ubicación de barcos enemigos y acabar con
            toda la flota."""
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n"  
    print """Single Player: En este módulo tendras 5 oportunidades
            para acertar la mayor cantidad de barcos posibles y obtener la mayor 
            cantidad de puntos.\n"""

    print """Multiplayer: En este módulo puedes jugar contra un amigo
            ya que los dos deben esconder cuantos barcos desean y luego 
            empezar el ataque; y gana el que mas barcos haya hundido.\n"""

    print"""   Barcos Existentes:
            1. Submarino de 1 Posición
            2. Patrullero de 2 Posiciónes
            3. Fragata de 3 Posiciónes
            4. Destructor de 4 Posiciónes
            5. Remolcador de 5 Posiciónes"""
    

    raw_input("Presione enter para continuar... ")
    pixer.stop()
    os.system("reset")
    menu()
    epica.play()

def play1():
    epica.stop()
    print "Bienvenido a Single Player"
    os.system("clear")
    batalla = _Player()
    batalla.start_single()
    os.system("clear")
    menu()
    epica.play()


def play1_2():
    epica.stop()
    print "Bienvenido a MultiPlayer"
    os.system("clear")
    naval = _Multi_Player()
    naval.start_players()
    menu()
    epica.play()

def salir():
    print "Saliendo ..."
    time.sleep(2)
    os.system("clear")
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
    print " ☠☠☠☠                  Batalla Naval 4.0                  ☠☠☠☠ "
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n"
    print u"                    ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠"
    print u"                        Kevin Herrera"
    print u"                    ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠\n"
    print u"                  KAR_KO,INDUSTRIS Copright ®"
    time.sleep(1)
    sys.exit()

def menu():
    menu = {1:instrucciones, 2:play1, 3:play1_2, 4:salir}
    validar = False
    opcion = 0
    epica.play(loops=3, maxtime=0, fade_ms=0)
    while True:

        print"                           ***** BattleShip Menú © ***** \n"
        print "1. Instrucciones"
        print "2. Single Player"
        print "3. MultiPlayer"
        print "4. Salir"

        opcion = raw_input("Ingresa una opción: ")
        try:
            opcion = int(opcion)
            if opcion > 0 and opcion <= 4:
                break
            else:
                print "Ingrese opción válida\n"
                time.sleep(1)
                os.system("clear")
        except(RuntimeError, TypeError, NameError, ValueError):
            print "Ingrese opción válida\n"
            time.sleep(1)
            os.system("clear")

    if menu.has_key(opcion):    
        print 'Si tiene la clave buscada'
        valor = menu[opcion]()
    else:    
        print 'No existe la clave buscada'

    opcion = 0
menu()
