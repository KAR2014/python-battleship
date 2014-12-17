# -*- coding: utf-8 -*-
"""BattleShip 3.0 """
import random
import os
import sys
import time

#Librerias del reproductor
import pygame.mixer
pygame.mixer.init(44100, -16, 2, 4096)
epica = pygame.mixer.Sound("epica.wav")     # Dura 9 segundos
print "Reproduciendo ..."
epica.play(loops=2, maxtime=0, fade_ms=0)

"""Clase de Single Player"""
class _Player(object):

    """ Metodo de Iniciación"""
    def __init__(self):
        self.tablero = []
        self.board = []
        self.armar_tablero_1()
        self.armar_tablero_2()
        self.fila_aleatoria()
        self.columna_aleatoria()
        self.opcion_pos()

    """ Armamos Tablero 1 """
    def armar_tablero_1(self):
        for x in range(0, 10):
            self.tablero.append(10 * ['♒'])
        #print tablero

    """ Armamos Tablero en Blanco """
    def armar_tablero_2(self):
        for x in range(0, 10):
            self.board.append(10 * ['♒'])
        #print board

    """ Imprimimos Tablero 1 """
    def print_tablero(self):
        for i in self.tablero:
            print "  ".join(i)
    """ Imprimimos Tablero en Blanco """
    def print_board(self):
        for i in self.board:
            print "  ".join(i)

    """ Definiremos posición Horizontal o Vertical (1/2) """
    def opcion_pos(self):
        return random.randint(1, 2)

    """ Fila Aleatoria """
    def fila_aleatoria(self):
        return random.randint(0, len(self.tablero)-1)

    """ Columna Aleatoria """
    def columna_aleatoria(self):
        return random.randint(0, len(self.tablero[0])-1)

    """Validacion Posicion Horizontal"""
    def validar_horizontal(self, barco_fila, barco_col, contador):
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

    """Validacion posicion Vertical"""
    def validar_vertical(self, barco_fila, barco_col, contador):
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

    '''Posicionando Barcos'''
    def colocar_barcos(self):
        self.sonido = pygame.mixer.Sound("pirata.wav")     # Declaramos Sonido del Juego
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

    """Inicia el Single Player"""
    def start_single(self):
        repetir = "si"
        while repetir == "si":
            pygame.mixer.init(44100, -16, 2, 4096)
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

"""Funcion del Menu"""
def menu():
    oportunidad = 0
    while True:
        while (oportunidad != 1) or (oportunidad != 2) or (oportunidad != 3) or (oportunidad != 4):

            print"                    ***** BattleShip © ***** \n"
            print "1. Instrucciones"
            print "2. Single Player"
            print "3. MultiPlayer"
            print "4. Salir"

            oportunidad = raw_input("Ingresa una opción: ")
            try:
                oportunidad = int(oportunidad)
                if oportunidad > 0 and oportunidad <= 4:
                    break
                else:
                    print "Ingrese opción válida\n"
                    time.sleep(1)
                    os.system("clear")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese opción válida\n"
                time.sleep(1)
                os.system("clear")

        if oportunidad == 1:
            print "Bienvenido a las Instrucciones"


        if oportunidad == 2:
            epica.stop()
            print "Bienvenido a Single Player"
            os.system("clear")
            batalla = _Player()
            batalla.start_single()
            epica.play()

        if oportunidad == 3:
            print "Bienvenido a MultiPlayer"
            #naval = _Multi_Player()

        if oportunidad == 4:
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
    oportunidad = 0
    return
menu()
