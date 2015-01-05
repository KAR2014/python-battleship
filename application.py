#-*- coding: utf-8 -*-
"""BattleShip 6.0 """
import random
import os
import sys
import time

#Librerias del reproductor
import pygame.mixer
pygame.mixer.init(44100, -16, 2, 4096)
EPICA = pygame.mixer.Sound("epica.wav")   # inicializo el sonido de los menus - EPICA
PIXER = pygame.mixer.Sound("inss.wav")

##############################################################
##############        Clase Single_player      ###############
##############################################################

class _Player(object):
    """Clase de Single Player"""

    def __init__(self):
        """ Iniciamos Variables Globales """
        self.sonido = pygame.mixer.Sound("pirata.wav") #inicializo el sonido - PIRATA
        self.explosion = pygame.mixer.Sound("ex.wav") #inicializo el sonido - EX
        self.epica = pygame.mixer.Sound("epica.wav") #inicializo el sonido - EPICA
        self.pixer = pygame.mixer.Sound("inss.wav") #inicializo el sonido - INSS
        self.medallas = {}
        self.puntos = {}
        self.tablero = []
        self.board = []

        #Iniciamos Métodos
        self.armar_tableros()

    def limpiar(self):
        """ Limpiar """
        self.tablero = []
        self.board = []


    def armar_tableros(self):
        """ Armamos Tablero 1 """
        for _ in range(0, 10):
            self.tablero.append(10 * ['♒'])

        for _ in range(0, 10):
            self.board.append(10 * ['♒'])

    def print_tablero(self):
        """ Imprimimos Tablero 1 """
        print "   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |"
        print "   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  \n"
        cont = 0
        for i in self.tablero:
            print str(cont) + "  |  " + "  |  ".join(i) + "  |"
            print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
            cont += 1

    def print_board(self):
        """ Imprimimos Tablero en Blanco """
        print "   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |"
        print "   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  \n"
        cont = 0
        for i in self.board:
            print str(cont) + "  |  " + "  |  ".join(i) + "  |"
            print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n"
            cont += 1

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

    def colocar_barcos(self, ship5, ship4, ship3, ship2, ship1, bomba):
        '''Posicionando Barcos'''    # Declaramos Sonido del Juego
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               BattleShip Single Player              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero()
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠             BattleShip Colocando Barcos             ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        no_barcos = 0
        validar_h = 0
        validar_v = 0
        barco = 5
        print "\n                    ☠☠☠☠☠☠ 5. Remolcadores ☠☠☠☠☠☠"

        #Barcos de 5
        while no_barcos < ship5:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            time.sleep(1)
            print str(opcion)
            if opcion == 1:
                if bar_fil <= 5 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print str(bar_fil)
                        print str(bar_col)
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 5):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        print str(bar_fil)
                        print str(bar_col)
                        for i in range(0, 5):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        time.sleep(1)


        print "\n                    ☠☠☠☠☠☠ 4. Destructores ☠☠☠☠☠☠"
        #Barcos de 4
        while no_barcos < ship4:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            print str(opcion)
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 6 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print "Destructor # "+ str(no_barcos + 1) + " Colocado"
                        print str(bar_fil)
                        print str(bar_col)
                        for i in range(0, 4):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Destructor #"+ str(no_barcos + 1) +" Colocado"
                        print str(bar_fil)
                        print str(bar_col)
                        for i in range(0, 4):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        barco = 3
        time.sleep(1)


        print "\n                    ☠☠☠☠☠☠ 3. Fragatas ☠☠☠☠☠☠"

        #Barcos de 3
        while no_barcos < ship3:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            print str(opcion)
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 7 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print "Fragata #"+ str(no_barcos + 1) +" Colocado"
                        print str(bar_fil)
                        print str(bar_col)
                        for i in range(0, 3):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Fragata #"+ str(no_barcos + 1) + " Colocado"
                        print str(bar_fil)
                        print str(bar_col)
                        for i in range(0, 3):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        barco = 2
        time.sleep(1)

        print "\n                    ☠☠☠☠☠☠ 2. Patrulleros ☠☠☠☠☠☠"

        #Barcos de 2
        while no_barcos < ship2:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            opcion = self.opcion_pos()
            print str(opcion)
            time.sleep(1)
            if opcion == 1:
                if bar_fil <= 8 and bar_col <= 9:
                    validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
                    if validar_h == 1:
                        print "Patrullero #"+ str(no_barcos + 1) + " Colocado"
                        print str(bar_fil)
                        print str(bar_col)
                        for i in range(0, 2):
                            self.tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Patrullero #"+ str(no_barcos + 1) + " Colocado"
                        print str(bar_fil)
                        print str(bar_col)
                        for i in range(0, 2):
                            self.tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        opcion = 0
        barco = 1
        time.sleep(1)


        print "\n                    ☠☠☠☠☠☠ 1. Submarinos ☠☠☠☠☠☠"

        #Barcos de 1
        while no_barcos < ship1:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            time.sleep(1)

            validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
            validar_v = self.validar_vertical(bar_fil, bar_col, barco)
            if validar_h == 1 and validar_v == 1:
                print str(bar_fil)
                print str(bar_col)
                print "Submarino #"+ str(no_barcos + 1) + " Colocado"
                self.tablero[bar_fil][bar_col] = "⚓"
                no_barcos += 1
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
        no_barcos = 0
        barco = 1
        time.sleep(1)

        print "\n                    ☠☠☠☠☠☠  ☠. Bombas ☠☠☠☠☠☠"
        while no_barcos < bomba:
            bar_fil = self.fila_aleatoria()
            bar_col = self.columna_aleatoria()
            time.sleep(1)

            validar_h = self.validar_horizontal(bar_fil, bar_col, barco)
            validar_v = self.validar_vertical(bar_fil, bar_col, barco)
            if validar_h == 1 and validar_v == 1:
                print "Bomba #"+ str(no_barcos + 1) + " Colocada"
                print str(bar_fil)
                print str(bar_col)
                self.tablero[bar_fil][bar_col] = "*"
                no_barcos += 1
            elif validar_h == 2 and validar_v == 2:
                print "Lo Sentimos Hay un Barco en esa Posición"
                print "Restableciedo Coordenadas Espere ... ⌛"
                time.sleep(1)
                os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                  ☠. Bombas Colocadas                ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        bar_fil = 0
        bar_col = 0
        opcion = 0
        no_barcos = 0
        barco = 0
        time.sleep(1)

        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               BattleShip: Ships in Board            ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero()

        time.sleep(1)

    def start_single(self, nivel, oportunidad, nombre):
        """Inicia el Single Player"""

        if nivel == 1:
            self.colocar_barcos(1, 1, 1, 1, 1, 1)
        elif nivel == 2:
            self.colocar_barcos(1, 1, 1, 2, 2, 2)
        elif nivel == 3:
            self.colocar_barcos(1, 1, 2, 3, 3, 3)
        elif nivel == 4:
            self.colocar_barcos(2, 2, 2, 3, 3, 4)
        elif nivel == 5:
            self.colocar_barcos(3, 3, 3, 3, 3, 5)

        os.system("clear")
        score = 0
        decremento = oportunidad
        asierto1 = 0
        asierto2 = 0
        adiv_fil = 0
        adiv_col = 0
        turno = 0
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print "                   BattleShip Tablero: ", nombre
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"

        while turno < oportunidad:#¡De aquí en adelante todo debería ir en tu bucle for!
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
                    os.system("reset")
            if (adiv_fil >= 0 and adiv_fil <= 9) and (adiv_col >= 0 and adiv_col <= 9):
                #Tiro Repetido
                if (self.board[adiv_fil][adiv_col] == "☠" and asierto1 > 0) or \
                    (self.board[adiv_fil][adiv_col] == "X" and asierto2 > 0):
                    print "Ya dijiste esa."
                    self.print_board()

                    #hundiendo barco
                elif self.tablero[adiv_fil][adiv_col] == "⚓":
                    print "¡Felicitaciones! ¡Hundiste mi barco!"
                    score += 10 #Contador de puntaje
                    asierto1 += 1
                    self.explosion.play()
                    self.board[adiv_fil][adiv_col] = "☠"
                    self.print_board()
                elif self.tablero[adiv_fil][adiv_col] == "*":
                    print " Lo sentimos has impactado en la Bomba has Perdido "
                    score = 0
                    break
                    return score
                else:
                    #No impacte el barco
                    print "¡No impactaste mi barco!"
                    self.board[adiv_fil][adiv_col] = "X"
                    self.print_board()
                    asierto2 += 1
            #fuera oceano
            if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                print "Vaya, esto ni siquiera está en el océano."
                asierto1 += 1
                asierto2 += 1
                self.print_board()

            turno += 1 #contador de turnos
            decremento -= 1
            print "Turnos Restantes: "+ str(decremento)
            print "puntos al momento: "+ str(score)

            time.sleep(2)
            os.system("clear")

            if turno == oportunidad:
                print "Terminó el juego"
                time.sleep(1)
                return score
    def ascenso(self, nombre, level, score):
        """LLenamos el diccionario medallas """
        game_over = 0

        if level == 1:
            os.system("clear")
            self.medallas[nombre] = "Cabo"
            self.puntos[nombre] = score

        if level == 2:
            self.medallas[nombre] = "Sargento"
            self.puntos[nombre] = score

        if level == 3:
            self.medallas[nombre] = "Teniente"
            self.puntos[nombre] = score

        if level == 4:
            self.medallas[nombre] = "Capitán"
            self.puntos[nombre] = score

        if level == 5:
            self.medallas[nombre] = "Mayor"
            self.puntos[nombre] = score
            game_over = 1

        print "   *******   Battleship ****** Detalles de la Misión ***** "
        print "Misión: "+ str(level)
        print "Nombre: "+ nombre
        print "Puntos: "+ str(self.puntos[nombre])
        print "Rango Naval: "+ str(self.medallas[nombre]) + "\n"
        raw_input("Presione Enter para tu siguiente misión... ")
        os.system("reset")

        if game_over == 1:
            print "¡Felicitaciones Mayor! Bien Jugado "
            raw_input("Presione Enter para Continuar... ")

    def misiones(self, mision, nombre):
        """Aqui colocamos la impresion de las misiones"""
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                     Batalla Naval                   ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        if mision == 1: # MISION 1
            print """
                        Battleship * Misión 1:

            Muy bien """+ nombre + """ desidiste entrar en
            en la marina veremos si eres digno de estar aquí.


            Deberas en 5 oportunidades enfrentar a la 
            flota enemiga y conseguir de 40-50 puntos,
            y colocamos una bomba por ahi, ojalá no tropiezes con ella,
            ja ja ja ja...

            ¡ Suerte Novato !
            """
            raw_input("Presione enter para continuar... ")
            os.system("reset")

        if mision == 2: # MISION 2
            print """        Battleship * Misión 2:

            Muy bien Cabo demuestra que mereces tu placa...

            Ahora la flota se ha incrementado debes en 7 oportunidades
            conseguir de 60-70 puntos, ¡ojo no dije que ya no hubieran
            Bombas! 

            Nos vemos en tu siguiente Misión...
            Bueno si sales de esta

            ¡ Suerte Cabo !

            """
            raw_input("Presione enter para continuar... ")
            os.system("reset")

        if mision == 3: # MISION 3
            print """        Battleship * Misión 3:

            Muy bien Sargento veremos si mereces seguir en el NAVY...

            En esta misión deberas enfrentar a una flota aún más
            peligrosa, con bombas, más barcos y más duro para tí.

            Ahora contaras con 10 oportunidades para 
            conseguir de 80-100 puntos. 

            Adelante Sorprendeme...

            ¡ Suerte Sargento !

            """
            raw_input("Presione enter para continuar... ")
            os.system("reset")

        if mision == 4:# MISION 4
            print """        Battleship * Misión 4:

            Muy bien Teniente veremos como
            te va en esta ocasión...

            Tu desafio es lograr de 110-120 puntos
            en 12 oportunidades y como es costumbre 
            las bombas incrementaron ja ja.

            El reto es cada vez mas peligroso

            ¿Crees poder logarlo? ...

            ¡ Suerte Teniente !

            """
            raw_input("Presione enter para continuar... ")
            os.system("reset")

        if mision == 5: # MISION 5
            print """        Battleship * Misión 5:

            Muy bien Capitán la primer 
            batalla a su cargo.

            Acabe con la mayor cantidad de barcos
            de la mega flota naval dispuesta a que lo 
            despidan del NAVY.

            Con 15 oportunidades debes conseguir
            de 130-150 puntos para consagrarte
            como MAYOR y además dueño de tu 
            propia Flota Naval.

            Escuche que el clima no te va ayudar mucho.

            Todo depende de Ti.

            Dime, ¿Tienes lo que se necesita
            para llevar esa insignia? ...

            ¡ Suerte Capitán !

            """
            raw_input("Presione enter para continuar... ")
            os.system("reset")

    def niveles(self):
        """Metodo nuevo de nivles para el single player"""
        self.sonido.play(loops=5, maxtime=0, fade_ms=0)
        self.limpiar()
        self.armar_tableros()
        nombre = ""
        level = 1
        puntos = 0
        repetir = "si"
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                     Batalla Naval                   ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n"
        print " Ya que desidiste ingresar en el NAVY \n"
        while True:
            nombre = raw_input("Ingrese su Nombre Soldado: ")
            nombre = nombre.title()
            try:
                nombre = float(nombre)
                nombre = int(nombre)
                print u"Debe ingresar un nombre válido\n"
            except(RuntimeError, NameError, ValueError):
                if len(nombre) <= 2:
                    print u"Debe ingresar un nombre válido\n"
                else:
                    nombre = nombre
                    break

        if level == 1: # Entrando al Nivel 1
            while repetir == "si":
                self.misiones(level, nombre)
                time.sleep(1)
                puntos = self.start_single(1, 5, nombre)
                os.system("reset")

                if puntos >= 40 and puntos <= 50:
                    print "Misión Cumplida Soldado"
                    print "Na... Suerte de Principiantes"
                    print nombre + " Bien has sido ascendido a Cabo "
                    time.sleep(2)
                    self.ascenso(nombre, level, puntos)
                    self.limpiar()
                    level += 1
                    break
                elif puntos <= 30:
                    print "Misión Fallida Soldado"
                    print nombre + """ Ja ja ja, parece que el NAVY es demasiado para Tí.
                    Mejor Suerte la Próxima, si te atreves por supuesto."""
                    while True:
                        repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                        repetir = repetir.lower()
                        try:
                            if repetir == "no":
                                self.sonido.stop()
                                os.system("reset")
                                self.menu_single()
                            elif repetir == "si":
                                self.sonido.stop()
                                time.sleep(1)
                                self.limpiar()
                                self.armar_tableros()
                                os.system("reset")
                                self.sonido.play(loops=8, maxtime=0, fade_ms=0)
                                break
                            else:
                                print "Error de ingreso"
                                time.sleep(1)
                                os.system("reset")
                        except(RuntimeError, TypeError, NameError, ValueError):
                            os.system("reset")
                time.sleep(2)
                os.system("reset")
        self.limpiar()
        self.armar_tableros()

        if level == 2: #Entrando al Nivel 2
            while repetir == "si":
                self.misiones(level, nombre)
                time.sleep(1)
                puntos = self.start_single(2, 7, nombre)
                os.system("reset")

                if puntos >= 60 and puntos <= 70:
                    print "Misión Cumplida Soldado"
                    print "No estubo mal..."
                    print nombre +" has sido ascendido a Sargento"
                    time.sleep(2)
                    self.ascenso(nombre, level, puntos)
                    self.limpiar()
                    level += 1
                    break
                elif puntos <= 40:
                    print "Misión Fallida Soldado"
                    print "El NAVY es para soldados no para aficionados."
                    print "Intentalo de Nuevo, si tines agallas."
                    while True:
                        repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                        repetir = repetir.lower()
                        try:
                            if repetir == "no":
                                self.sonido.stop()
                                os.system("reset")
                                self.menu_single()
                            elif repetir == "si":
                                self.sonido.stop()
                                time.sleep(1)
                                self.limpiar()
                                self.armar_tableros()
                                os.system("reset")
                                self.sonido.play(loops=8, maxtime=0, fade_ms=0)
                                break
                            else:
                                print "Error de ingreso"
                                time.sleep(1)
                                os.system("reset")
                        except(RuntimeError, TypeError, NameError, ValueError):
                            os.system("reset")
                time.sleep(2)
                os.system("reset")
        self.limpiar()
        self.armar_tableros()

        if level == 3: # Entrando al Nivel 3
            while repetir == "si":
                self.misiones(level, nombre)
                time.sleep(1)
                puntos = self.start_single(3, 10, nombre)
                os.system("reset")

                if puntos >= 70 and puntos <= 100:
                    print "Misión Cumplida Soldado"
                    print "Debo admitir que lo hiciste bien."
                    print nombre +" has sido ascendido a Teniente"
                    time.sleep(2)
                    self.ascenso(nombre, level, puntos) #Se Actualiza el valor del diccionario
                    self.limpiar()
                    level += 1
                    break
                elif puntos <= 60:
                    print "Misión Fallida Soldado"
                    print "¿Y eso es lo único que tienes?"
                    print "Es solo el inicio de lo más difícil.\n ¿Tienes más para Dar?"
                    while True:
                        repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                        repetir = repetir.lower()
                        try:
                            if repetir == "no":
                                self.sonido.stop()
                                os.system("reset")
                                self.menu_single()
                            elif repetir == "si":
                                self.sonido.stop()
                                time.sleep(1)
                                self.limpiar()
                                self.armar_tableros()
                                os.system("reset")
                                self.sonido.play(loops=8, maxtime=0, fade_ms=0)
                                break
                            else:
                                print "Error de ingreso"
                                time.sleep(1)
                                os.system("reset")
                        except(RuntimeError, TypeError, NameError, ValueError):
                            os.system("reset")
                time.sleep(2)
                os.system("reset")
        self.limpiar()
        self.armar_tableros()

        if level == 4: # Entrando al Nivel 4
            while repetir == "si":
                self.misiones(level, nombre)
                time.sleep(1)
                puntos = self.start_single(4, 12, nombre)
                os.system("reset")

                if puntos >= 100 and puntos <= 120:
                    print "Misión Cumplida Soldado"
                    print "No pense que pudieras logarlo, pero en fin."
                    print nombre +" has sido ascendido a Capitán"
                    time.sleep(2)
                    self.ascenso(nombre, level, puntos) #Se Actualiza el valor del diccionario
                    self.limpiar()
                    level += 1
                    break
                elif puntos <= 90:
                    print "Misión Fallida Soldado"
                    print """Algo me decia que no eras capaz de
                    completar esta misión.

                    Y así te haces llamar Teniente?

                    Eso es todo lo que tiene Soldado?"""
                    while True:
                        repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                        repetir = repetir.lower()
                        try:
                            if repetir == "no":
                                self.sonido.stop()
                                os.system("reset")
                                self.menu_single()
                            elif repetir == "si":
                                self.sonido.stop()
                                time.sleep(1)
                                self.limpiar()
                                self.armar_tableros()
                                os.system("reset")
                                self.sonido.play(loops=8, maxtime=0, fade_ms=0)
                                break
                            else:
                                print "Error de ingreso"
                                time.sleep(1)
                                os.system("reset")
                        except(RuntimeError, TypeError, NameError, ValueError):
                            os.system("reset")
                time.sleep(2)
                os.system("reset")
        self.limpiar()
        self.armar_tableros()

        if level == 5: # Entrando al Nivel 5
            while repetir == "si":
                self.misiones(level, nombre)
                time.sleep(1)
                puntos = self.start_single(5, 15, nombre)
                os.system("reset")

                if puntos >= 120 and puntos <= 150:
                    print "Misión Cumplida Soldado"
                    print "Excelente Trayecto Señor."
                    print nombre +""" has sido ascendido a Capitán
                    Y con ello tu propia Flota Naval.
                    En hora buena...
                    """
                    time.sleep(2)
                    self.ascenso(nombre, level, puntos) #Se Actualiza el valor del diccionario
                    self.limpiar()
                    level += 1
                    break
                elif puntos <= 100:
                    print "Misión Fallida Soldado"
                    print """Creí que podrias con ellos.
                    ¿Qué pasó?

                    ¿Es mucho para tí,
                    o te vas a rendir?"""
                    while True:
                        repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                        repetir = repetir.lower()
                        try:
                            if repetir == "no":
                                self.sonido.stop()
                                os.system("reset")
                                self.menu_single()
                            elif repetir == "si":
                                self.sonido.stop()
                                time.sleep(1)
                                self.limpiar()
                                self.armar_tableros()
                                os.system("reset")
                                self.sonido.play(loops=8, maxtime=0, fade_ms=0)
                                break
                            else:
                                print "Error de ingreso"
                                time.sleep(1)
                                os.system("reset")
                        except(RuntimeError, TypeError, NameError, ValueError):
                            os.system("reset")
                time.sleep(2)
                os.system("reset")
        self.limpiar()
        self.armar_tableros()
        self.menu_single()

    def rango_naval(self):
        """ Titulos del Single Player"""
        self.pixer.play(loops=3, maxtime=0, fade_ms=0)
        ordenar = self.medallas
        por_puntos = self.puntos

        print"                   ***** BattleShip Medallero * Single Player © ***** \n"

        #print ordenar
        for i in por_puntos:
            print "Nombre: "+ str(i)
            print "Puntos: "+ str(por_puntos[i])
            print "Rango Naval: "+ str(ordenar[i]) + "\n\n"

        raw_input("Presione enter para continuar... ")
        self.pixer.stop()
        os.system("reset")
        self.menu_single()

    def instrucciones_single(self):
        """Instrucciones del Single Player"""
        self.pixer.play(loops=2, maxtime=0, fade_ms=0)
        print"                           ***** BattleShip Instrucciones * Single Player © ***** \n"
        print """
        En este modo de juego deberas completar 5 
        misiones navales como jamás lo imaginaste.

        Las Misiones se cargaran automáticamente y para empezar el ataque 
        deberas ingresar las coordenadas a tu elección (fila-columna).
        Dimensiones del tablero 10 filas enumeradas del (0-9) y 
        10 columnas enumeradas del (0-9), ¡Ojo deberan ser numeros enteros!

        En cada misión se incrementara la cantidad de barcos a derribar y Bombas
        ocultas que se pondran en cualquier posición de tu tablero; ojo si caes en 
        una bomba el juego terminara...

        Ascenderas de puesto con forme vayas completando cada una, a demás tendras 
        un determinado número de intentos para lograr tu misión.
        Rangos Navales que Puedes Alcanzar: 

        1. Cabo
        2. Sargento
        3. Teniente 
        4. Capitán
        5. Mayor

        Te informo las Fuerzas Navales (NAVY) ¡NO SON PARA NIÑOS!

        ¿Te crees capaz de cumplir este desafio?

        ¿Estás listo para 
                            Batalla Naval ?\n"""

        raw_input("Presione enter para continuar... ")
        self.pixer.stop()
        os.system("reset")
        self.menu_single()

    def menu_single(self):
        """funcion menu single player"""
        self.epica.play(loops=3, maxtime=0, fade_ms=0)
        menu_sing = {1:self.instrucciones_single, 2:self.niveles, 3:self.rango_naval, 4:menu}
        opcion = 0
        while True:

            print"                    ***** BattleShip Menú * Single Player © ***** \n"
            print "1. Instrucciones"
            print "2. Jugar"
            print "3. Medallero"
            print "4. Volver al Menú Principal"

            opcion = raw_input("Ingresa una opción: ")
            try:
                opcion = int(opcion)
                if opcion > 0 and opcion <= 4:
                    break
                else:
                    print "Ingrese opción válida\n"
                    time.sleep(1)
                    os.system("reset")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese opción válida\n"
                time.sleep(1)
                os.system("reser")

        if menu_sing.has_key(opcion) and opcion == 4:
            self.epica.stop()
            os.system("reset")
            menu_sing[opcion]()
        else:
            self.epica.stop()
            os.system("reset")
            menu_sing[opcion]()

        opcion = 0


##############################################################
##############        Clase Multi-Player       ###############
##############################################################


class _Mplayer(object):
    """Clase de _Mplayer"""

    def __init__(self):
        """ Iniciamos Variables Globales """
        self.batalla = pygame.mixer.Sound("up.wav") #declaramos el sonido - UP
        self.explosion = pygame.mixer.Sound("ex.wav") #declaramos el sonido - EX
        self.epica = pygame.mixer.Sound("epica.wav") #iniciamos el sonido - EPICA
        self.pixer = pygame.mixer.Sound("inss.wav") #iniciamos el sonido - INSS

        self.nombre1 = ""
        self.nombre2 = ""
        self.tabla_de_puntajes = {}
        self.rangos = {}
        self.tablero_j1 = []
        self.tablero_j2 = []
        self.board_j1 = []
        self.board_j2 = []

        #Iniciamos Métodos
        self.armar_tableros()

    def limpiar(self):
        """ Limpiar """
        self.tablero_j1 = []
        self.tablero_j2 = []
        self.board_j1 = []
        self.board_j2 = []

    def armar_tableros(self):
        """ Armamos Tablero 1 y 2 """
        for _ in range(0, 10):
            self.tablero_j1.append(10 * ['♒'])
            self.tablero_j2.append(10 * ['♒'])
            self.board_j1.append(10 * ['♒'])
            self.board_j2.append(10 * ['♒'])

    def print_tablero(self, tablero):
        """ Imprimimos Tablero 1 """
        print "   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |"
        print "   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  \n"
        cont = 0
        for i in tablero:
            print str(cont) + "  |  " + "  |  ".join(i) + "  |"
            print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
            cont += 1

    def print_board(self, board):
        """ Imprimimos Tablero en Blanco player 1 """
        print "   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |"
        print "   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  \n"
        cont = 0
        for i in board:
            print str(cont) + "  |  " + "  |  ".join(i) + "  |"
            print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
            cont += 1

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
                    os.system("reset")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("reset")
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
                    os.system("reset")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("reset")
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
                    os.system("reset")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("reset")
        return columna

    def numero_barcos(self, bomba):
        """ Cantidad de Barcos """
        ship = 0
        while True:
            if bomba == "bomba":
                ship = raw_input("¿Cuantas Bombas Desea? ")
            else:
                ship = raw_input("¿Cuantos Barcos Desea? ")
            try:
                ship = int(ship)
                if ship > 0:
                    break
                else:
                    print "Error Ingreso Incorrecto\n"
                    time.sleep(1)
                    os.system("reset")
            except (KeyboardInterrupt, RuntimeError, TypeError, NameError, ValueError):
                print "Error Ingreso Incorrecto\n"
                time.sleep(1)
                os.system("reset")
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
        os.system("reset")
        board = []
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print "              BattleShip Tablero Jugador: ", player
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(tablero)
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠             BattleShip Colocando Barcos             ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        no_barcos = 0
        cant_barcos = 0
        validar_h = 0
        validar_v = 0
        barco = 5
        while True:
            print "\n                    ☠☠☠☠☠☠ 5. Remolcadores ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos(0)

            if barco == 5:
                if (cant_barcos > 0) and (cant_barcos <= 3):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 3 barcos!"
                    time.sleep(1)
                    os.system("reset")

        #Barcos de 5
        while no_barcos < cant_barcos:
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 5):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 5):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        barco = 4
        time.sleep(1)

        while True:
            print "\n                    ☠☠☠☠☠☠ 4. Destructores ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos(0)

            if barco == 4:
                if (cant_barcos > 0) and (cant_barcos <= 4):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 4 barcos!"
                    time.sleep(1)
                    os.system("reset")

        #Barcos de 4
        while no_barcos < cant_barcos:
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 4):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 4):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        barco = 3
        time.sleep(1)


        while True:
            print "\n                    ☠☠☠☠☠☠ 3. Fragatas ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos(0)

            if barco == 3:
                if (cant_barcos > 0) and (cant_barcos <= 6):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 6 barcos!"
                    time.sleep(1)
                    os.system("reset")

        #Barcos de 3
        while no_barcos < cant_barcos:
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 3):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 3):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        barco = 2
        time.sleep(1)

        while True:
            print "\n                    ☠☠☠☠☠☠ 2. Patrulleros ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos(0)

            if barco == 2:
                if (cant_barcos > 0) and (cant_barcos <= 10):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 10 barcos!"
                    time.sleep(1)
                    os.system("reset")

        #Barcos de 2
        while no_barcos < cant_barcos:
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 2):
                            tablero[bar_fil + i][bar_col] = "⚓"
                        no_barcos += 1
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
                        print "Remolcador #"+ str(no_barcos + 1) + " Colocado"
                        for i in range(0, 2):
                            tablero[bar_fil][bar_col+i] = "⚓"
                        no_barcos += 1
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
        no_barcos = 0
        barco = 1
        time.sleep(1)


        while True:
            print "\n                    ☠☠☠☠☠☠ 1. Submarinos ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos(0)

            if barco == 1:
                if (cant_barcos > 0) and (cant_barcos <= 15):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 15 barcos!"
                    time.sleep(1)
                    os.system("reset")

        #Barcos de 1
        while no_barcos < cant_barcos:
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
                print "Submarino #"+ str(no_barcos + 1) + " Colocado"
                tablero[bar_fil][bar_col] = "⚓"
                no_barcos += 1
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
        no_barcos = 0
        opcion = 0
        barco = 1
        time.sleep(1)

        while True:
            print "\n                    ☠☠☠☠☠☠ *. Bombas ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos("bomba")

            if barco == 1:
                if (cant_barcos > 0) and (cant_barcos <= 7):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 7 barcos!"
                    time.sleep(1)
                    os.system("reset")

        print "\n                    ☠☠☠☠☠☠  ☠. Bombas ☠☠☠☠☠☠"
        while no_barcos < cant_barcos:
            bar_fil = self.fila_player()
            bar_col = self.columna_player()
            print "FILA: " + str(bar_fil)
            print "COLUMNA: " + str(bar_col)
            time.sleep(1)

            validar_h = self.validar_horizontal(bar_fil, bar_col, barco, tablero)
            validar_v = self.validar_vertical(bar_fil, bar_col, barco, tablero)
            if validar_h == 1 and validar_v == 1:
                print "Bomba #"+ str(no_barcos + 1) + " Colocada"
                print str(bar_fil)
                print str(bar_col)
                tablero[bar_fil][bar_col] = "*"
                no_barcos += 1
            elif validar_h == 2 and validar_v == 2:
                print "Lo Sentimos Hay un Barco en esa Posición"
                print "Restableciedo Coordenadas Espere ... ⌛"
                time.sleep(1)
                os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                  ☠. Bombas Colocadas                ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        bar_fil = 0
        bar_col = 0
        opcion = 0
        no_barcos = 0
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

    def play_j1(self, turno, score, nombre1, nombre2, oportunidad):
        """ Jugador 1 """
        decremento = oportunidad
        while True:
            print "Turno:", (turno +1)# ¡Muestra (turno + 1) aquí!
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero", nombre1
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.tablero_j1)
            print "\n"
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero", nombre2
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.board_j2)
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
                    os.system("reset")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese coordenadas válidas\n"
                time.sleep(1)
                os.system("reset")
        if (adiv_fil >= 0 and adiv_fil <= 9) and (adiv_col >= 0 and adiv_col <= 9):
            #tiro repetido
            if (self.board_j2[adiv_fil][adiv_col] == "☠") or \
                (self.board_j2[adiv_fil][adiv_col] == "X"):
                print "Ya dijiste esa."
                self.print_board(self.board_j2)
                #hundiendo barco
            elif self.tablero_j2[adiv_fil][adiv_col] == "⚓":
                print "¡Felicitaciones! ¡Hundiste mi barco!"
                score += 10
                self.explosion.play()
                self.board_j2[adiv_fil][adiv_col] = "☠"
                self.tablero_j2[adiv_fil][adiv_col] = "☠"
                self.print_board(self.board_j2)

            elif self.tablero_j1[adiv_fil][adiv_col] == "*":
                print "¡ Fatal Marino has impactado en la bomba !"
                score = 0
                return 16

            else:
                #No impacte el barco
                print "¡No impactaste mi barco!"
                self.board_j2[adiv_fil][adiv_col] = "X"
                self.tablero_j2[adiv_fil][adiv_col] = "X"
                self.print_board(self.board_j2)
        else:
            #fuera oceano
            if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                print "Vaya, esto ni siquiera está en el océano."
                self.print_board(self.board_j2)
        print "Turnos Restantes: "+ str(decremento - 1)
        print "puntos al momento: "+ str(score)
        time.sleep(2)
        os.system("reset")
        return score

    def play_j2(self, turno, score, nombre1, nombre2, oportunidad):
        """ Jugador 2 """
        decremento = oportunidad
        while True:
            print "Turno:", (turno +1)# ¡Muestra (turno + 1) aquí!
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero", nombre2
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.tablero_j2)
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print "                       Tablero", nombre1
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
            self.print_tablero(self.board_j1)
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
                    os.system("reset")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese coordenadas válidas\n"
                time.sleep(1)
                os.system("reset")
        #hundiendo barco
        if (adiv_fil >= 0 and adiv_fil <= 9) and (adiv_col >= 0 and adiv_col <= 9):
            #tiro repetido
            if (self.board_j1[adiv_fil][adiv_col] == "☠") or \
                (self.board_j1[adiv_fil][adiv_col] == "X"):
                print "Ya dijiste esa."
                self.print_board(self.board_j1)
            elif self.tablero_j1[adiv_fil][adiv_col] == "⚓":
                print "¡Felicitaciones! ¡Hundiste mi barco!"
                score += 10
                self.explosion.play()
                self.board_j1[adiv_fil][adiv_col] = "☠"
                self.tablero_j1[adiv_fil][adiv_col] = "☠"
                self.print_board(self.board_j1)

            elif self.tablero_j1[adiv_fil][adiv_col] == "*":
                print "¡ Fatal Marino has impactado en la bomba !"
                score = 0
                return 16
            else:
                #No impacte el barco
                print "¡No impactaste mi barco!"
                self.board_j1[adiv_fil][adiv_col] = "X"
                self.tablero_j1[adiv_fil][adiv_col] = "X"
                self.print_board(self.board_j1)
        else:
            #fuera oceano
            if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                print "Vaya, esto ni siquiera está en el océano."
                self.print_board(self.board_j1)

        print "Turnos Restantes: "+ str(decremento - 1)
        print "puntos al momento: "+ str(score)
        time.sleep(2)
        os.system("reset")
        return score

    def start_players(self):
        """Inicia el Multi_Player"""
        self.batalla.play(loops=5, maxtime=0, fade_ms=0)
        score = 0
        oportunidad = 10
        cont_j1 = 0
        cont_j2 = 0
        puntaje_j1 = 0
        puntaje_j2 = 0
        repetir = "si"
        while repetir == "si":
            self.limpiar()
            self.armar_tableros()
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
                    if len(self.nombre1) <= 2:
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
                    time.sleep(2)
                    os.system("reset")
                except(RuntimeError, NameError, ValueError):
                    if len(self.nombre2) <= 2:
                        print u"Debe ingresar un nombre válido\n"
                        time.sleep(2)
                        os.system("reset")
                    else:
                        self.nombre2 = self.nombre2
                        break
            print "             ☠☠☠☠☠☠☠☠☠☠☠☠☠☠ ", self.nombre1, " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠"
            raw_input("Presione Enter para Continuar ...")
            self.tablero_j1 = self.colocar_barcos_players(self.tablero_j1, self.nombre1)
            os.system("reset")

            print "             ☠☠☠☠☠☠☠☠☠☠☠☠☠☠ ", self.nombre2, " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠"
            raw_input("Presione Enter para Continuar ...")
            self.tablero_j2 = self.colocar_barcos_players(self.tablero_j2, self.nombre2)
            os.system("reset")
            turno = 0

            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
            print " ☠☠☠☠                  BattleShip: Start Game             ☠☠☠☠ "
            print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"

            while turno < oportunidad:#¡De aquí en adelante todo debería ir en tu bucle for!

                cont_j1 = self.play_j1(turno, score, self.nombre1, self.nombre2, oportunidad)
                cont_j2 = self.play_j2(turno, score, self.nombre1, self.nombre2, oportunidad)

                if cont_j1 == 16:
                    print self.nombre1 + " Lo Sentimos has perdido. "
                    break
                elif cont_j2 == 16:
                    print self.nombre2 + " Lo Sentimos has perdido. "
                    break
                else:
                    puntaje_j1 += cont_j1
                    puntaje_j2 += cont_j2

                turno += 1
                #contador de turnos
                if turno == oportunidad or cont_j1 == 16 or cont_j2 == 16:
                    print "Terminó el juego"
                    print "Puntaje "+ self.nombre1 + ": "+ str(puntaje_j1)
                    print "Puntaje "+ self.nombre2 + ": "+ str(puntaje_j2)

                    if puntaje_j1 > puntaje_j2:
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
                        print "         ¡Felicitaciones! ", self.nombre1, " ¡Has Ganado!      "
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
                        self.llenado_de_puntajes(self.nombre1, puntaje_j1, 1)
                    elif puntaje_j2 > puntaje_j1:
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
                        print "         ¡Felicitaciones! ", self.nombre2, " ¡Has Ganado!       "
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
                        self.llenado_de_puntajes(self.nombre1, puntaje_j1, 2)
                    elif puntaje_j1 == puntaje_j2:
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
                        print " ☠☠☠☠           ¡Excelente Marinos han Empatado!          ☠☠☠☠ "
                        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
                        self.llenado_de_puntajes(self.nombre1, puntaje_j1, 1)
                        self.llenado_de_puntajes(self.nombre1, puntaje_j1, 2)
            while True:
                repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                repetir = repetir.lower()
                try:
                    if repetir == "no":
                        self.batalla.stop()
                        break
                    elif repetir == "si":
                        self.batalla.stop()
                        time.sleep(1)
                        self.limpiar()
                        self.armar_tableros()
                        os.system("reset")
                        self.start_players()

                    else:
                        print "Error de ingreso"
                        time.sleep(1)
                        os.system("reset")
                except(RuntimeError, TypeError, NameError, ValueError):
                    os.system("reset")

            os.system("reset")
            self.menu_multi()

    def llenado_de_puntajes(self, nombre, puntos, player):
        """ Llenado de Diccionarios """
        if player == 1 or player == 2:

            if puntos >= 10 and puntos <= 20:
                self.rangos[nombre] = "Cabo"
            elif puntos >= 30 and puntos <= 40:
                self.rangos[nombre] = "Sargento"
            elif puntos >= 50 and puntos <= 60:
                self.rangos[nombre] = "Teniente"
            elif puntos >= 70 and puntos <= 80:
                self.rangos[nombre] = "Capitán"
            elif puntos >= 90 and puntos <= 100:
                self.rangos[nombre] = "Mayor"
            self.tabla_de_puntajes[nombre] = puntos

        print "   *******   Battleship ****** Detalles de la Batalla ***** "
        print "Nombre: "+ nombre
        print "Puntos: "+ str(self.tabla_de_puntajes[nombre])
        print "Rango Naval: "+ str(self.rangos[nombre]) + "\n"

        raw_input("Presione enter para continuar... ")


    def inst_multi(self):
        """Instrucciones del Multiplayer"""
        self.pixer.play(loops=3, maxtime=0, fade_ms=0)
        print"                           ***** BattleShip Instrucciones * Multi-Player © ***** \n"
        print """En este modo de juego hasta los mejores amigos son rivales.

        Ya que tú y un amigo pueden embarcarse en una guerra inimaginable donde: 
        Remolcadores, Destructores, Fragatas, Patrulleros, Submarinos y Bombas
        seran la sensasión.

        Dimensiones del tablero 10 filas enumeradas del (0-9) y 
        10 columnas enumeradas del (0-9) y para empezar el ataque
        deberas ingresar las coordenadas a tu elección (fila-columna).
        ¡Ojo deberan ser numeros enteros!

        Pues tendras 10 oportunidades para lograr la mayor cantidad
        de puntos que tu adversario.

        Depende de tus puntos así sera tu Rango Naval:
            De 10-20  = Cabo
            De 30-40  = Sargento
            De 50-60  = Teniente
            De 70-80  = Capitán
            De 90-100 = Mayor

        Si buscabas un juego en el que no fuese necesario lógica, 
        presición, valor y desición...  
        ¡ Lo sentimos NO es éste!
        ¿Estás listo para 
                            Batalla Naval ?\n"""

        raw_input("Presione enter para continuar... ")
        self.pixer.stop()
        os.system("reset")
        self.menu_multi()

    def puntajes_altos(self):
        """Puntajes Altos del Multiplayer"""
        self.pixer.play(loops=3, maxtime=0, fade_ms=0)
        print"                      ***** BattleShip Medallero * Multi-Player © ***** \n"
        max_score = self.tabla_de_puntajes
        puesto_naval = self.rangos

        #print ordenar
        for i in max_score:
            print "Nombre: "+ str(i)
            print "Puntos: "+ str(max_score[i])
            print "Rango Naval: "+ str(puesto_naval[i]) + "\n\n"

        raw_input("Presione enter para continuar... ")
        self.pixer.stop()
        os.system("reset")
        self.menu_multi()


    def menu_multi(self):
        """funcion menu Multiplayer"""
        menu_multiplay = {1:self.inst_multi, 2:self.start_players, 3:self.puntajes_altos, 4:menu}
        opcion = 0
        self.epica.play(loops=3, maxtime=0, fade_ms=0)
        while True:

            print"                   ***** BattleShip Menú * Multi-Player © ***** \n"
            print "1. Instrucciones"
            print "2. Jugar"
            print "3. Medallero"
            print "4. Volver al Menú Principal"

            opcion = raw_input("Ingresa una opción: ")
            try:
                opcion = int(opcion)
                if opcion > 0 and opcion <= 4:
                    break
                else:
                    print "Ingrese opción válida\n"
                    time.sleep(1)
                    os.system("reset")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese opción válida\n"
                time.sleep(1)
                os.system("reset")

        if menu_multiplay.has_key(opcion):
            self.epica.stop()
            os.system("reset")
            menu_multiplay[opcion]()
        else:
            "No existe la clave"

        opcion = 0



##############################################################
##############            Clase Menu           ###############
##############################################################


def instrucciones():
    """Acerca de Batalla Naval """
    PIXER.play(loops=4, maxtime=0, fade_ms=0)
    os.system("reset")
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
    print " ☠☠☠☠                Acerca de Batalla Naval              ☠☠☠☠ "
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"

    print """Batalla Naval:
    La batalla naval (juego de los barquitos o hundir la flota,
    nombre con el que se comercializó en España el juego de mesa;
    hundiendo barquitos, en algunos lugares de Hispanoamérica),
    del nombre en inglés battleship,es un juego tradicional
    de adivinación que involucra a dos participantes.

    Se ha comercializado como juego de mesa
    en distintos formatos por varias marcas.
    El primero en sacarlo al mercado fue Milton Bradley Company,
    en 1931, y se jugaba con lápiz y papel.
    En 2012 se estrenó una película basada en el juego,
    titulada Battleship."""
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n"

    print """Tableros:
    Cada jugador maneja dos tableros divididos en casillas.
    Cada tablero representa una zona diferente del mar abierto:
    la propia y la contraria.
    En uno de los tableros, el jugador coloca sus barcos y registra
    los «tiros» del oponente;
    en el otro, se registran los tiros propios, al tiempo que se
    deduce la posición de los barcos del contrincante.

    Naves:
    Al comenzar, cada jugador posiciona sus barcos en el 
    primer tablero, de forma secreta, invisible al oponente.

    Cada quien ocupa, según sus preferencias, una misma
    cantidad de casillas, horizontal y/o verticalmente,
    las que representan sus naves. Ambos participantes deben
    ubicar igual el número de naves, por lo que es habitual,
    antes de comenzar, estipular de común acuerdo la cantidad y
    el tamaño de las naves que se posicionarán en el tablero.
    
     Naves Existentes:
            1. Submarino de 1 Posición
            2. Patrullero de 2 Posiciónes
            3. Fragata de 3 Posiciónes
            4. Destructor de 4 Posiciónes
            5. Remolcador de 5 Posiciónes

    Desarrollo del juego
    Una vez todas las naves han sido posicionadas,
    se inicia una serie de rondas. En cada ronda, cada
    jugador en su turno «dispara»
    hacia la flota de su oponente indicando una posición
    (las coordenadas de una casilla),
    la que registra en el segundo tablero.
    Si esa posición es ocupada por parte de un barco contrario,
    el oponente cantará ¡Averiado! (¡Toque! o ¡Tocado!) si todavía
    quedan partes del barco (casillas) sin dañar, o
    ¡Hundido! si con ese disparo la nave ha quedado totalmente destruida
    (esto es, si la acertada es la última de las casillas
    que conforman la nave que quedaba por acertar).
    Si la posición indicada no corresponde a una parte de
    barco alguno, cantará ¡Agua!.

    Cada jugador referenciará en ese segundo tablero,
    de diferente manera y a su conveniencia, los disparos
    que han caído sobre una nave oponente y los que han caído al mar:
    en la implementación del juego con lápiz y papel,
    pueden señalarse con una cruz los tiros errados y
    con un círculo los acertados a una nave, o con cuadrados
    huecos y rellenos, como se ve en la imagen; 
    en la versión con pizarras, se utilizan pines de un
    color para los aciertos y de otro para las marras.


    Fin del juego:
    El juego puede terminar con un ganador o en empate.

    hay ganador: quien descubra, quien destruya primero
    todas las naves de su oponente será el vencedor
    (como en tantos otros juegos en los que se participa por turnos, 
    en caso de que el participante que
    comenzó la partida hunda en su última jugada el último barco
    de su oponente que quedaba a flote,
    el otro participante tiene derecho a una última posibilidad
    para alcanzar el empate,
    a un último disparo que también le permita terminar de 
    hundir la flota contraria, lo que supondría un empate);

    empate: si bien lo habitual es continuar el juego hasta que
    haya un ganador,
    el empate también puede alcanzarse si, tras haber
    disparado cada jugador una
    misma cantidad de tiros fija y predeterminada
    (como una variante permitida en el juego),
    ambos jugadores han acertado en
    igual número de casillas contrarias.

    Modos de Juego:
    1. Single Player: En el cual se llena el tablero automáticamente 
                      y el jugador debera destruir la flota.

    2. Multiplayer: En este modo deberas enfrentarte con un amigo."""

    raw_input("Presione enter para continuar... ")
    PIXER.stop()
    os.system("reset")
    menu()


def navy():
    """ Funcion de Etiqueta """
    print """                   ☠☠☠☠☠☠☠☠☠☠☠☠  Batalla Naval 6.0  ☠☠☠☠☠☠☠☠☠☠☠

                                         # #  ( )
                                      ___#_#___|__
                                  _  |____________|  _ 
                           _=====| | |            | | |==== _ 
                     =====| |.---------------------------. | |====
        <--------------------'   .  .  .  .  .  .  .  .   '-------------->
         \                              POSEIDON                        /
          \____________________________________________________________/
        wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
           wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    """
    raw_input("Presione enter...")
    os.system("reset")

def play1():
    """se dirige al menu"""
    navy()
    batalla = _Player()
    batalla.menu_single()
    os.system("reset")
    menu()

def play1_2():
    """Inicia el Juego de Jugador 1 y jugador 2 """
    navy()
    naval = _Mplayer()
    naval.menu_multi()
    menu()

def salir():
    """Funcion Salir"""
    print "Saliendo ..."
    time.sleep(2)
    os.system("reset")
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
    print " ☠☠☠☠                  Batalla Naval 6.0                  ☠☠☠☠ "
    print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n"
    print  "                    ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠"
    print  "                        Kevin Herrera"
    print  "                    ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠\n"
    print  "                  KAR_KO,INDUSTRIS Corporing ®"
    time.sleep(1)
    sys.exit()

def menu():
    """Funcion menu Principal"""
    menu = {1:instrucciones, 2:play1, 3:play1_2, 4:salir}
    opcion = 0
    EPICA.play(loops=4, maxtime=0, fade_ms=0)
    while True:

        print"                           ***** BattleShip Menú © ***** \n"
        print "1. Acerca de Batalla Naval"
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
                os.system("reset")
        except(RuntimeError, TypeError, NameError, ValueError):
            print "Ingrese opción válida\n"
            time.sleep(1)
            os.system("reset")

    if menu.has_key(opcion):
        EPICA.stop()
        os.system("reset")
        menu[opcion]()

    else:
        print 'No hay clave buscada'
    opcion = 0
navy()
menu()
