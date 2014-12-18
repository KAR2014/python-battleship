# -*- coding: utf-8 -*-
"""BattleShip 3.0 """
import random
import os
import sys
import time

#Librerias del reproductor
import pygame.mixer
pygame.mixer.init(44100, -16, 2, 4096)

class _Player(object):
    """Clase de Single Player"""

    def __init__(self):
        """ Iniciamos Variables Globales """
        self.sonido = pygame.mixer.Sound("pirata.wav")
        self.tablero = []
        self.board = []
        self.validar_h = 0
        self.validar_v = 0
        self.barco = 0
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        #Iniciamos Métodos
        self.armar_tableros()
        self.fila_aleatoria()
        self.columna_aleatoria()
        self.opcion_pos()

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
        barco_fila = barco_fila
        barco_col = barco_col
        contador = contador
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
        barco_fila = barco_fila
        barco_col = barco_col
        contador = contador
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
        print " ☠☠☠☠                  BattleShip Tablero                 ☠☠☠☠ "
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
        self.validar_h = 0
        self.validar_v = 0
        self.barco = 5
        print "\n                    ☠☠☠☠☠☠ 5. Remolcadores ☠☠☠☠☠☠"

        #Barcos de 5
        while kar5 < 2:
            self.bar_fil = self.fila_aleatoria()
            self.bar_col = self.columna_aleatoria()
            #print "FILA: " + str(self.bar_fil)
            #print "COLUMNA: " + str(self.bar_col)
            self.opcion = self.opcion_pos()
            #print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 5 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_h == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            self.tablero[self.bar_fil + i][self.bar_col] = "⚓"
                        kar5 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 5:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 5 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_v == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            self.tablero[self.bar_fil][self.bar_col+i] = "⚓"
                        kar5 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == 2:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 5:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              5. Remolcadores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 4
        time.sleep(1)

        print "\n                    ☠☠☠☠☠☠ 4. Destructores ☠☠☠☠☠☠"
        #Barcos de 4
        while kar4 < 1:
            self.bar_fil = self.fila_aleatoria()
            self.bar_col = self.columna_aleatoria()
            #print "FILA: " + str(self.bar_fil)
            #print "COLUMNA: " + str(self.bar_col)
            self.opcion = self.opcion_pos()
            #print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 6 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_h == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Destructor # "+ str(kar4 + 1) + " Colocado"
                        for i in range(0, 4):
                            self.tablero[self.bar_fil + i][self.bar_col] = "⚓"
                        kar4 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 6:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 6 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_v == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Destructor #"+ str(kar4 + 1) +" Colocado"
                        for i in range(0, 4):
                            self.tablero[self.bar_fil][self.bar_col+i] = "⚓"
                        kar4 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == 2:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 6:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              4. Destructores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 3
        time.sleep(1)


        print "\n                    ☠☠☠☠☠☠ 3. Fragatas ☠☠☠☠☠☠"

        #Barcos de 3
        while kar3 < 1:
            self.bar_fil = self.fila_aleatoria()
            self.bar_col = self.columna_aleatoria()
            #print "FILA: " + str(self.bar_fil)
            #print "COLUMNA: " + str(self.bar_col)
            self.opcion = self.opcion_pos()
            #print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 7 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_h == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Fragata #"+ str(kar3 + 1) +" Colocado"
                        for i in range(0, 3):
                            self.tablero[self.bar_fil + i][self.bar_col] = "⚓"
                        kar3 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 7:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 7 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_v == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Fragata #"+ str(kar3 + 1) + " Colocado"
                        for i in range(0, 3):
                            self.tablero[self.bar_fil][self.bar_col+i] = "⚓"
                        kar3 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == False:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 7:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                3. Fragatas Colocados                ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 2
        time.sleep(1)

        print "\n                    ☠☠☠☠☠☠ 2. Patrulleros ☠☠☠☠☠☠"

        #Barcos de 2
        while kar2 < 2:
            self.bar_fil = self.fila_aleatoria()
            self.bar_col = self.columna_aleatoria()
            #print "FILA: " + str(self.bar_fil)
            #print "COLUMNA: " + str(self.bar_col)
            self.opcion = self.opcion_pos()
            #print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 8 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_h == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Patrullero #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            self.tablero[self.bar_fil + i][self.bar_col] = "⚓"
                        kar2 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 8:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 8 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco)
                    if self.validar_v == 1:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Patrullero #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            self.tablero[self.bar_fil][self.bar_col+i] = "⚓"
                        kar2 += 1
                        #raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == 2:
                        #print "FILA: " + str(self.bar_fil)
                        #print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        self.bar_fil = self.fila_aleatoria()
                        self.bar_col = self.columna_aleatoria()
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 8:
                    #print "FILA: " + str(self.bar_fil)
                    #print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    self.bar_fil = self.fila_aleatoria()
                    self.bar_col = self.columna_aleatoria()
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               2. Patrulleros Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 1
        time.sleep(1)


        print "\n                    ☠☠☠☠☠☠ 1. Submarinos ☠☠☠☠☠☠"

        #Barcos de 1
        while kar1 < 3:
            self.bar_fil = self.fila_aleatoria()
            self.bar_col = self.columna_aleatoria()
            #print "FILA: " + str(self.bar_fil)
            #print "COLUMNA: " + str(self.bar_col)
            time.sleep(1)

            self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco)
            self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco)
            if self.validar_h == 1 and self.validar_v == 1:
                #print "FILA: " + str(self.bar_fil)
                #print "COLUMNA: " + str(self.bar_col)
                print "Submarino #"+ str(kar1 + 1) + " Colocado"
                self.tablero[self.bar_fil][self.bar_col] = "⚓"
                kar1 += 1
                #raw_input("Presione Enter para Continuar ...")
            elif self.validar_h == 2 and self.validar_v == 2:
                #print "FILA: " + str(self.bar_fil)
                #print "COLUMNA: " + str(self.bar_col)
                print "Lo Sentimos Hay un Barco en esa Posición"
                print "Restableciedo Coordenadas Espere ... ⌛"
                self.bar_fil = self.fila_aleatoria()
                self.bar_col = self.columna_aleatoria()
                time.sleep(1)
                os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                1. Submarinos Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 0
        time.sleep(1)

        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               BattleShip: Ships in Board            ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero()

        time.sleep(1)

    def start_single(self):
        """Inicia el Single Player"""
        repetir = "si"
        while repetir == "si":
            explosion = pygame.mixer.Sound("ex.wav")
            self.colocar_barcos()
            os.system("clear")
            score = 0
            repetido = 0
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
                    if self.tablero[adiv_fil][adiv_col] == "⚓":
                        print "¡Felicitaciones! ¡Hundiste mi barco!"
                        score += 10
                        explosion.play()
                        self.board[adiv_fil][adiv_col] = "☠"
                        self.print_board()

                        #fuera oceano
                    elif self.board[adiv_fil][adiv_col] == "☠" or self.board[adiv_fil][adiv_col] == "X" or repetido > 0:

                        print "Ya dijiste esa."
                        self.print_board()
                    else:
                        #No impacte el barco
                        print "¡No impactaste mi barco!"
                        self.board[adiv_fil][adiv_col] = "X"
                        self.print_board()
                else:
                    #tiro repetido
                    if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                        repetido += 1
                        print "Vaya, esto ni siquiera está en el océano."
                        self.print_board()
                turno += 1
                #contador de turnos
                if turno == 5:
                    print "Terminó el juego"
                    #Contador de puntaje
                    if score == 40 or score == 50:
                        print "Felcitaciones Has Ganado"
                        print "Puntaje Final: ", (score)
                    elif score == 30:
                        print "Muy Bien Marino"
                        print "Puntaje Final: ", (score)
                    elif score <= 20:
                        print "Fatal Como Capitán eres Pésimo"
                        print "Puntaje Final: ", (score)
                time.sleep(2)
                os.system("clear")
            while True:
                repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                repetir = repetir.lower()
                try:
                    if repetir == "":
                        print "¡Error ingrese opcion válida!"
                        time.sleep(1)
                        os.system("clear")
                    repetir = float(repetir)
                    repetir = int(repetir)
                    print "¡Error ingrese opcion válida!"
                    time.sleep(1)
                    os.system("clear")
                except(RuntimeError, TypeError, NameError, ValueError):
                    repetir = repetir
                if repetir == "si":
                    self.sonido.stop()
                    time.sleep(1)
                    os.system("clear")
                    new_game = _Player()
                    new_game.start_single()
                elif repetir == "no":
                    self.sonido.stop()
                    break
                break
            break
        os.system("clear")

class _Multi_Player(object):
    """Clase de _Multi_Player"""

    def __init__(self):
        """ Iniciamos Variables Globales """
        self.up = pygame.mixer.Sound("up.wav")
        self.tablero_J1 = []
        self.tablero_J2 = []
        self.board_J1 = []
        self.board_J2 = []
        self.validar_h = 0
        self.validar_v = 0
        self.barco = 0
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        #Iniciamos Métodos
        self.armar_tableros()

        
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
        tablero = tablero
        for i in tablero:
            print "  ".join(i)

    def print_board(self, board):
        """ Imprimimos Tablero en Blanco player 1 """
        board = board 
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
        barco_fila = barco_fila
        barco_col = barco_col
        contador = contador
        tablero = tablero
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
        barco_fila = barco_fila
        barco_col = barco_col
        contador = contador
        tablero = tablero
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

    def colocar_barcos_player1(self):
        '''Posicionando Barcos'''    # Declaramos Sonido del Juego
        print "Reproduciendo ..."
        self.up.play(loops=4, maxtime=0, fade_ms=0)
        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                  BattleShip Jugador 1               ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(self.tablero_J1)
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
        self.validar_h = 0
        self.validar_v = 0
        self.barco = 5
        while True:
            print "\n                    ☠☠☠☠☠☠ 5. Remolcadores ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if self.barco == 5:
                if (cant_barcos > 0) and (cant_barcos <= 3):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 3 barcos!"
                    time.sleep(1)
                    os.system("clear")

        raw_input("Presione Enter para continuar ... \n")

        #Barcos de 5
        while kar5 < cant_barcos:
            self.bar_fil = self.fila_player()
            self.bar_col = self.columna_player()
            print "FILA: " + str(self.bar_fil)
            print "COLUMNA: " + str(self.bar_col) + "\n"
            self.opcion = self.opcion_pos()
            print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 5 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_h == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            self.tablero_J1[self.bar_fil + i][self.bar_col] = "⚓"
                        kar5 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 5:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 5 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_v == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar5 + 1) + " Colocado"
                        for i in range(0, 5):
                            self.tablero_J1[self.bar_fil][self.bar_col+i] = "⚓"
                        kar5 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 5:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              5. Remolcadores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(self.tablero_J1)
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 4
        time.sleep(1)

        while True:
            print "\n                    ☠☠☠☠☠☠ 4. Destructores ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if self.barco == 4:
                if (cant_barcos > 0) and (cant_barcos <= 4):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 4 barcos!"
                    time.sleep(1)
                    os.system("clear")

        raw_input("Presione Enter para continuar ... \n")

        #Barcos de 4
        while kar4 < cant_barcos:
            self.bar_fil = self.fila_player()
            self.bar_col = self.columna_player()
            print "FILA: " + str(self.bar_fil)
            print "COLUMNA: " + str(self.bar_col) + "\n"
            self.opcion = self.opcion_pos()
            print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 6 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_h == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar4 + 1) + " Colocado"
                        for i in range(0, 4):
                            self.tablero_J1[self.bar_fil + i][self.bar_col] = "⚓"
                        kar4 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 6:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 6 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_v == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar4 + 1) + " Colocado"
                        for i in range(0, 4):
                            self.tablero_J1[self.bar_fil][self.bar_col+i] = "⚓"
                        kar4 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 6:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠              4. Destructores Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(self.tablero_J1)
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 3
        time.sleep(1)


        while True:
            print "\n                    ☠☠☠☠☠☠ 3. Fragatas ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if self.barco == 3:
                if (cant_barcos > 0) and (cant_barcos <= 6):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 6 barcos!"
                    time.sleep(1)
                    os.system("clear")

        raw_input("Presione Enter para continuar ... \n")

        #Barcos de 3
        while kar3 < cant_barcos:
            self.bar_fil = self.fila_player()
            self.bar_col = self.columna_player()
            print "FILA: " + str(self.bar_fil)
            print "COLUMNA: " + str(self.bar_col) + "\n"
            self.opcion = self.opcion_pos()
            print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 7 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_h == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar3 + 1) + " Colocado"
                        for i in range(0, 3):
                            self.tablero_J1[self.bar_fil + i][self.bar_col] = "⚓"
                        kar3 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 7:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 7 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_v == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar3 + 1) + " Colocado"
                        for i in range(0, 3):
                            self.tablero_J1[self.bar_fil][self.bar_col+i] = "⚓"
                        kar3 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 7:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                3. Fragatas Colocados                ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(self.tablero_J1)
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 2
        time.sleep(1)

        while True:
            print "\n                    ☠☠☠☠☠☠ 2. Patrulleros ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if self.barco == 2:
                if (cant_barcos > 0) and (cant_barcos <= 10):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 10 barcos!"
                    time.sleep(1)
                    os.system("clear")

        raw_input("Presione Enter para continuar ... \n")

        #Barcos de 2
        while kar2 < cant_barcos:
            self.bar_fil = self.fila_player()
            self.bar_col = self.columna_player()
            print "FILA: " + str(self.bar_fil)
            print "COLUMNA: " + str(self.bar_col) + "\n"
            self.opcion = self.opcion_pos()
            print "Posición: "+ str(self.opcion)
            time.sleep(1)
            if self.opcion == 1:
                if self.bar_fil <= 8 and self.bar_col <= 9:
                    self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_h == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            self.tablero_J1[self.bar_fil + i][self.bar_col] = "⚓"
                        kar2 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_h == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_fil > 8:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
            elif self.opcion == 2:
                if self.bar_col <= 8 and self.bar_fil <= 9:
                    self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
                    if self.validar_v == 1:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Remolcador #"+ str(kar2 + 1) + " Colocado"
                        for i in range(0, 2):
                            self.tablero_J1[self.bar_fil][self.bar_col+i] = "⚓"
                        kar2 += 1
                        raw_input("Presione Enter para Continuar ...")
                    elif self.validar_v == 2:
                        print "FILA: " + str(self.bar_fil)
                        print "COLUMNA: " + str(self.bar_col)
                        print "Lo Sentimos Hay un Barco en esa Posición"
                        print "Restableciedo Coordenadas Espere ... ⌛"
                        time.sleep(1)
                        os.system("clear")
                    #opcion = 0
                elif self.bar_col > 7:
                    print "FILA: " + str(self.bar_fil)
                    print "COLUMNA: " + str(self.bar_col)
                    print "El barco no esta en el Oceano"
                    print "Restableciedo Coordenadas Espere ... ⌛"
                    time.sleep(1)
                    os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               2. Patrulleros Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(self.tablero_J1)
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 1
        time.sleep(1)


        while True:
            print "\n                    ☠☠☠☠☠☠ 1. Submarinos ☠☠☠☠☠☠"
            cant_barcos = self.numero_barcos()

            if self.barco == 1:
                if (cant_barcos > 0) and (cant_barcos <= 15):
                    break
                else:
                    print "¡Error Solo puedes ingresar un máximo de 15 barcos!"
                    time.sleep(1)
                    os.system("clear")

        raw_input("Presione Enter para continuar ... \n")
        #Barcos de 1
        while kar1 < cant_barcos:
            self.bar_fil = self.fila_player()
            self.bar_col = self.columna_player()
            print "FILA: " + str(self.bar_fil)
            print "COLUMNA: " + str(self.bar_col)
            time.sleep(1)

            self.validar_h = self.validar_horizontal(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
            self.validar_v = self.validar_vertical(self.bar_fil, self.bar_col, self.barco, self.tablero_J1)
            if self.validar_h == 1 and self.validar_v == 1:
                print "FILA: " + str(self.bar_fil)
                print "COLUMNA: " + str(self.bar_col)
                print "Submarino #"+ str(kar1 + 1) + " Colocado"
                self.tablero_J1[self.bar_fil][self.bar_col] = "⚓"
                kar1 += 1
                raw_input("Presione Enter para Continuar ...")
            elif self.validar_h == 2 and self.validar_v == 2:
                print "FILA: " + str(self.bar_fil)
                print "COLUMNA: " + str(self.bar_col)
                print "Lo Sentimos Hay un Barco en esa Posición"
                print "Restableciedo Coordenadas Espere ... ⌛"
                time.sleep(1)
                os.system("clear")
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠                1. Submarinos Colocados              ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        #self.print_tablero()
        self.bar_fil = 0
        self.bar_col = 0
        self.opcion = 0
        self.barco = 0
        time.sleep(1)

        print
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ "
        print " ☠☠☠☠               BattleShip: Ships in Board            ☠☠☠☠ "
        print " ☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠ \n\n"
        self.print_tablero(self.tablero_J1)

        time.sleep(1)

    def start_players(self):
        """Inicia el Single Player"""
        repetir = "si"
        while repetir == "si":
            explosion = pygame.mixer.Sound("ex.wav")
            self.colocar_barcos_player1()
            os.system("clear")
            score = 0
            repetido = 0
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
                    self.print_board(self.board_J1)
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
                    if self.tablero_J1[adiv_fil][adiv_col] == "⚓":
                        print "¡Felicitaciones! ¡Hundiste mi barco!"
                        score += 10
                        explosion.play()
                        self.board_J1[adiv_fil][adiv_col] = "☠"
                        self.print_board(self.board_J1)

                        #fuera oceano
                    elif self.board_J1[adiv_fil][adiv_col] == "☠" or self.board_J1[adiv_fil][adiv_col] == "X" or repetido > 0:

                        print "Ya dijiste esa."
                        self.print_board(self.board_J1)
                    else:
                        #No impacte el barco
                        print "¡No impactaste mi barco!"
                        self.board_J1[adiv_fil][adiv_col] = "X"
                        self.print_board(self.board_J1)
                else:
                    #tiro repetido
                    if (adiv_fil < 0 or adiv_fil > 9) or (adiv_col < 0 or adiv_col > 9):
                        repetido += 1
                        print "Vaya, esto ni siquiera está en el océano."
                        self.print_board(self.board_J1)
                turno += 1
                #contador de turnos
                if turno == 5:
                    print "Terminó el juego"
                    #Contador de puntaje
                    if score == 40 or score == 50:
                        print "Felcitaciones Has Ganado"
                        print "Puntaje Final: ", (score)
                    elif score == 30:
                        print "Muy Bien Marino"
                        print "Puntaje Final: ", (score)
                    elif score <= 20:
                        print "Fatal Como Capitán eres Pésimo"
                        print "Puntaje Final: ", (score)
                time.sleep(2)
                os.system("clear")
            while True:
                repetir = raw_input("¿Desea jugar otra vez? si/no\n")
                repetir = repetir.lower()
                try:
                    if repetir == "":
                        print "¡Error ingrese opcion válida!"
                        time.sleep(1)
                        os.system("clear")
                    repetir = float(repetir)
                    repetir = int(repetir)
                    print "¡Error ingrese opcion válida!"
                    time.sleep(1)
                    os.system("clear")
                except(RuntimeError, TypeError, NameError, ValueError):
                    repetir = repetir
                if repetir == "si":
                    self.up.stop()
                    time.sleep(1)
                    os.system("clear")
                    new_game = _Player()
                    new_game.start_players()
                elif repetir == "no":
                    self.up.stop()
                    break
                break
            break
        os.system("clear")

class _Menu(object):
    """Clase Menu"""
    def __init__(self):
        self.opcion = 0
        self.epica = pygame.mixer.Sound("epica.wav")     # Dura 9 segundos
        print "Reproduciendo ..."
    def menu_opciones(self):
        """Funcion del Menu"""
        self.epica.play(loops=2, maxtime=0, fade_ms=0)
        while True:
            while (self.opcion != 1) or (self.opcion != 2) or (self.opcion != 3) or (self.opcion != 4):

                print"                    ***** BattleShip © ***** \n"
                print "1. Instrucciones"
                print "2. Single Player"
                print "3. MultiPlayer"
                print "4. Salir"

                self.opcion = raw_input("Ingresa una opción: ")
                try:
                    self.opcion = int(self.opcion)
                    if self.opcion > 0 and self.opcion <= 4:
                        break
                    else:
                        print "Ingrese opción válida\n"
                        time.sleep(1)
                        os.system("clear")
                except(RuntimeError, TypeError, NameError, ValueError):
                    print "Ingrese opción válida\n"
                    time.sleep(1)
                    os.system("clear")

            if self.opcion == 1:
                print "Bienvenido a las Instrucciones"


            if self.opcion == 2:
                self.epica.stop()
                print "Bienvenido a Single Player"
                os.system("clear")
                batalla = _Player()
                batalla.start_single()
                self.epica.play()

            if self.opcion == 3:
                self.epica.stop()
                print "Bienvenido a MultiPlayer"
                os.system("clear")
                naval = _Multi_Player()
                naval.start_players()
                self.epica.play()

            if self.opcion == 4:
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
        self.opcion = 0
        return
JUGAR = _Menu()
JUGAR.menu_opciones()
