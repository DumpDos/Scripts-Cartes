#!/usr/bin/env python 
# coding: utf-8
# Créé par DumpDos, 2017

#--- librairies ---#
import os
import re
import sys
import time
import datetime

#--- fonction type de ticket ---#

def ticket_type_define(ticket_var0, ticket_var1):
   
   ticket_int_var0 = int(ticket_var0)
   ticket_int_var1 = int(ticket_var1) 
   
   if ticket_int_var0 == 0 and ticket_int_var1 == 98:
      ticket_name = "Ticket test"

   elif ticket_int_var0  == 2:
      ticket_name = "10 Voyages"
   
   elif ticket_int_var0  == 8:
      ticket_name = "1 Voyage"

   elif ticket_int_var0  == 15:
      ticket_name = "VisiTAG 1 jour"

   elif ticket_int_var0  == 16:
      ticket_name = "Tribu 1 jour"

   elif ticket_int_var0  == 29:
      ticket_name = "VisiTAG 3 jour"

   else:
      ticket_name = "Undefined"

   return ticket_name

#--- fonction calcul solde ticket ---#

def ticket_sold_info(ticket_num, type):

   ticket_sold_int = int(ticket_num)

   if ticket_sold_int == 0:
      if type == "VisiTAG 1 jour" or type == "Tribu 1 jour":
         ticket_sold_cont = "24"
         ticket_sold_name = "Heures"
      
      elif type == "VisiTAG 3 jour":
      	 ticket_sold_cont = "72"
         ticket_sold_name = "Heures"

      else:
         ticket_sold_cont = "0"
         ticket_sold_name = "Aucun voyage"

   elif ticket_sold_int == 1:
      ticket_sold_cont = "1"
      ticket_sold_name = "Voyage"

   elif ticket_sold_int > 1:
      ticket_sold_cont = ticket_sold_int
      ticket_sold_name = "Voyages"

   return (ticket_sold_cont, ticket_sold_name)

#--- fonction calcul horodatage ---#

def ticket_horo_info(timestamp):
   
   timestamp_2018 = int(1514761200)
   timestamp_tic = int(timestamp)
   timestamp_sec = ((timestamp_tic * 60) + (timestamp_2018 - 86400))
   ticket_time_cont = datetime.datetime.fromtimestamp(timestamp_sec)
   return ticket_time_cont
#--- fonction ligne et sens ticket ---#

def ticket_line_dir(ligne, sens):
   
   ligne_int = int(ligne)
   sens_int = int(sens)

   if ligne_int == 91:
      line = "'A'"
      if sens_int == 1:
         dire = "'Denis Papin'"
      if sens_int == 0:
         dire = "'La Poya'"

   elif ligne_int == 92:
      line = "'B'"
      if sens_int == 1:
         dire = "'Denis Papin'"
      if sens_int == 0:
         dire = "'La Poya'"

   elif ligne_int == 93:
      line = "'C'"
      if sens_int == 1:
         dire = "'Le Prisme'"
      if sens_int == 0:
         dire = "'Condilac - Universités'"
 
   elif ligne_int == 94:
      line = "'D'"
      if sens_int == 1:
         dire = "'Les Taillées - Universités'"
      if sens_int == 0:
         dire = "'Étienne Grappe'"

   elif ligne_int == 95:
      line = "'E'"
      if sens_int == 1:
         dire = "'Louise Michelle'"
      if sens_int == 0:
         dire = "'Fontanil - Paluel'"

   else:
      line = "undefined"
      dire = "undefined"
   
   return(line, dire)
   
#--- fonction arrets tram  ---#

def ticket_stops_define(arret):
    
    fichier = open("arrets_tag.txt", "r")

    for stop_search in fichier.readlines():
        if arret in stop_search:
           
           result = re.search(r"\'([^:]+)\'", stop_search)
           return result.group()                  
           print("Arrêt       : %s" % (result.group()))

#--- Script ---#

#--- Efface écran ---#
os.system('clear')

#--- Passage clavier qwerty ---#
os.system('setxkbmap us')
 
#--- affichage ---#
print '\033[34m***************************************************************'
print '*********************\033[31m TAG TICKET INFO \033[34m*************************' 
print '*******************\033[33m CTRL+C pour quitter \033[34m***********************'#--- boucle ---# while True:
print '***************************************************************'   

#--- boucle ---# 
while True:

   #--- entrée exception ---#
   try:
   
      #--- variables ---#   
      date = datetime.datetime.now()
      tag_info_base = open("tag_info_base.txt", "a")

      #--- Entrée numéro ticket ---#
      ticket_raw = raw_input("\033[37mPassez un ticket dans le lecteur: ")

      #--- récupération des infos ---#
      ticket_list = list(ticket_raw)
      ticket_star = ticket_list [1] + ticket_list [2] + ticket_list [3]
      ticket_type = ticket_list [4] + ticket_list [5]
      ticket_sold = ticket_list [11] + ticket_list [12] + ticket_list [13]
      ticket_time = ticket_list [14] + ticket_list [15] + ticket_list [16] + ticket_list [17] + ticket_list [18] + ticket_list [19]
      ticket_line = ticket_list [20] + ticket_list [21]
      ticket_sens = ticket_list [22]
      ticket_empl = ticket_list [24] + ticket_list [25]
      ticket_paxs = ticket_list [28] + ticket_list [29]
      ticket_vehi = ticket_list [32] + ticket_list [33] + ticket_list [34] + ticket_list [35]
      ticket_endi = ticket_list [39] + ticket_list [40]
   
      if ticket_star == "874":  

         #--- Conversion des infos ---#
         (ticket_name)                        = ticket_type_define(ticket_type, ticket_endi)
         (ticket_sold_cont, ticket_sold_name) = ticket_sold_info(ticket_sold, ticket_name)
         (ticket_time_cont)                   = ticket_horo_info(ticket_time)
         (ticket_line_numb, ticket_line_dire) = ticket_line_dir(ticket_line, ticket_sens)
         (ticket_stop_name)                   = ticket_stops_define(ticket_vehi)

         #--- affichage infos  ---#
         print '****************************************************************************'
         print("\033[33mEn-tête     : %s" % (ticket_star))
         print("Type        : %s" % (ticket_name))
         print("Solde       : %s %s" % (ticket_sold_cont, ticket_sold_name))
         print("Horodatage  : %s GMT" % (ticket_time_cont))
         print("Emplacement : %s" % (ticket_empl))
         print("Passagers   : %s" % (ticket_paxs))
         print("Ligne       : %s" % (ticket_line_numb))
         print("Direction   : %s" % (ticket_line_dire))
         print("Arrêt       : %s" % (ticket_stop_name))
         print("Véhicule    : %s" % (ticket_vehi))
         print("Terminaison : %s" % (ticket_endi))
         print '\033[37m****************************************************************************'
   
         #--- récupération des données ---#
   
      
         tag_info_base.write("\nTicket enregistré le %s/%s/%s à %s:%s" % (date.day, date.month, date.year, date.hour, date.minute))
         tag_info_base.write("\n****************************************************************************")
         tag_info_base.write("\nTicket      : %s" % (ticket_raw))
         tag_info_base.write("\nEn-tête     : %s" % (ticket_star))
         tag_info_base.write("\nType        : %s" % (ticket_name))
         tag_info_base.write("\nSolde       : %s %s" % (ticket_sold_cont, ticket_sold_name))
         tag_info_base.write("\nHorodatage  : %s GMT" % (ticket_time_cont))
         tag_info_base.write("\nEmplacement : %s" % (ticket_empl))
         tag_info_base.write("\nPassagers   : %s" % (ticket_paxs))
         tag_info_base.write("\nLigne       : %s" % (ticket_line_numb))
         tag_info_base.write("\nDirection   : %s" % (ticket_line_dire))
         tag_info_base.write("\nArrêt       : %s" % (ticket_stop_name))
         tag_info_base.write("\nVéhicule    : %s" % (ticket_vehi))
         tag_info_base.write("\nTerminaison : %s" % (ticket_endi))
         tag_info_base.write("\n****************************************************************************")
         tag_info_base.close()
      
      #--- Erreur ---#
      else:

         #--- affichage infos  ---#  
         print '****************************************************************************'
         print '\033[31mErreur'
         print '\033[37m****************************************************************************'

         #--- récupération des données ---
         tag_info_base.write("\nTicket enregistré le %s/%s/%s à %s:%s" % (date.day, date.month, date.year, date.hour, date.minute))
         tag_info_base.write("\n****************************************************************************")
         tag_info_base.write("\nErreur")
         tag_info_base.write("\n****************************************************************************")
   
   #--- sortie script ---#
   except KeyboardInterrupt:
      os.system('setxkbmap fr')
      print''
      sys.exit(0)
