#!/usr/bin/env python 
# coding: utf-8

#--- librairies ---#
import os
import re
import sys
import time
import datetime

#--- Variables ---#

char_1 = '%B'
char_2 = '^'
char_3 = '/'
char_4 = '.'
char_5 = '?'
char_6 = ';'
char_7 = '='
char_8 = '+'
char_9 = ' '

#--- Fonctions ---#

def maj_convert(str_raw):
	str_con = str_raw.upper()
	return str_con

def str_addspac(str_raw):

        tal_var = len(str_raw)
	while not tal_var == 25:
           tal_var = len(str_raw)
           str_raw = str_raw + char_9
 
        return str_raw

#--- Script ---#

#--- Efface écran ---#
os.system('clear')

 
#--- affichage ---#
print '\033[34m***************************************************************'
print '************************\033[31m CB ENCODER \033[34m***************************' 
print '*******************\033[33m CTRL+C pour quitter \033[34m***********************'
print '***************************************************************'   

#--- boucle ---# 
while True:

   #--- entrée exception ---#
   try:
   
      #--- variables ---#   
      date = datetime.datetime.now()
      file_1 = date.strftime("./enregistrements/encoder_%Y%m%d_%H%M%S.txt")
      file_2 = "./enregistrements/cb_encoder_base.txt"
      
      #--- Ouverture des logs ---#
      cb_encoder_regi = open(file_1, "w")
      cb_encoder_base = open(file_2, "a")

      #--- Entrées Varibles ---#
      print '\033[37mEntrez les informations de la carte'
      cb_number_raw = raw_input("\033[31mNuméro de carte       : ")
      cb_civtit_raw = raw_input("Titre de civilité     : ")
      cb_frstna_raw = raw_input("Nom                   : ")
      cb_lastna_raw = raw_input("Prénom                : ")
      cb_montva_raw = raw_input("Mois de d'expiration  : ")
      cb_yearva_raw = raw_input("Année de d'expiration : ")
      cb_infocr_raw = raw_input("Clé de cryptage carte : ")

      #--- Initialisation des Varibles ---#	  
      cb_number = len(cb_number_raw)
      
      if cb_number == 16:

         (cb_civtit_con) = maj_convert(cb_civtit_raw)
         (cb_frstna_con) = maj_convert(cb_frstna_raw)
         (cb_lastna_con) = maj_convert(cb_lastna_raw)
         test = cb_lastna_con + char_9 + char_1
         test1 = len(test)
         print test1
         print test

         cb_strnam_raw = cb_frstna_con + char_3 + cb_lastna_con + char_4 + cb_civtit_con

         (cb_strnam_con) = str_addspac(cb_strnam_raw)
	  
         first_line = char_1 + cb_number_raw + char_2 + cb_strnam_con  +char_2 + cb_yearva_raw + cb_montva_raw + cb_infocr_raw + char_5
         print first_line
      else:
         print 'Erreur'
	  
   #--- sortie script ---#
   except KeyboardInterrupt:
      print''
      os.system('clear')
      sys.exit(0)
