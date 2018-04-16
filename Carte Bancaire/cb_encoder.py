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
      
      #--- initialisation ---#
      cb_encoder_regi = open(file_1, "w")
      cb_encoder_base = open(file_2, "a")

      #--- Entrée numéro ticket ---#
      print '\033[37mEntrez les informations de la carte'
      cb_number_raw = raw_input("\033[31mNuméro de carte       : ")
      cb_civtit_raw = raw_input("Titre de civilité     : ")
      cb_frstna_raw = raw_input("Nom                   : ")
      cb_lastna_raw = raw_input("Prénom                : ")
      cb_montva_raw = raw_input("Mois de d'expiration  : ")
      cb_yearva_raw = raw_input("Année de d'expiration : ")
      cb_infocr_raw = raw_input("Clé de cryptage carte : ")
	  
      first_line = char_1 + cb_number_raw + char_2 + cb_frstna_raw + char_3 + cb_lastna_raw + char_4 + cb_civtit_raw +char_2 + cb_yearva_raw + cb_montva_raw + cb_infocr_raw + char_5
      print first_line
	  
   #--- sortie script ---#
   except KeyboardInterrupt:
      print''
      os.system('clear')
      sys.exit(0)
