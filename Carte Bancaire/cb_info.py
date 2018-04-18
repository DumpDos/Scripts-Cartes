#!/usr/bin/env python 
# coding: utf-8

#--- librairies ---#
import os
import re
import sys
import time
import datetime

#--- fonction mise en forme du pan ---#

def pan_define(pan_str):
   
   pan_list = list(pan_str)
   nul_char = " " 
   
   pan_for = (pan_list[0] +
              pan_list[1] +
              pan_list[2] +
              pan_list[3] +
              nul_char +
              pan_list[4] +
              pan_list[5] +
              pan_list[6] +
              pan_list[7] +
              nul_char +
              pan_list[8] +
              pan_list[9] +
              pan_list[10] +
              pan_list[11] +
              nul_char +
              pan_list[12] +
              pan_list[13] +
              pan_list[14] +
              pan_list[15]
             )

   return pan_for
   
#--- fonction exatraction nom titulaire ---#

def tit_define(tit_str):

   tit_for_var = tit_str.replace('/',' ')
   tit_civ_var = re.search(r"\.([A-Z]+)", tit_for_var)
   result = tit_civ_var.group()

   tit_for = tit_for_var.replace(result,'')
   tit_civ = result.replace('.','')

   return (tit_for, tit_civ)

#--- fonction calcul expiration ---#

def exp_define(yea_str, mon_str):

   yea_int = int(yea_str)
   mon_int = int(mon_str)
   mon_list = ["Janvier",
               "Février",
               "Mars",
               "Avril",
               "Mai",
               "Juin",
               "Juillet",
               "Août",
               "Septembre",
               "Octobre",
	       "Novembre",
               "Décembre",
              ]

   mon_for = mon_list [mon_int-1]
   yea_for = yea_int + 2000
   
   return (mon_for, yea_for)
   
def srv_define(srv_str):
   srv_0_list = ["null",
                 "Echanges internationaux possibles",
                 "Echanges internationaux possibles avec utilisation de la puce",
		 "null",
		 "null",
                 "Echanges nationaux seulement",
                 "Echanges nationaux seulement avec utilisation de la puce",
                 "Echanges uniquement sur accords",
                 "null",
                 "null",
                 "Carte test",
                ]
   srv_1_list = ["Autorisation de paiement sans restriction",
                 "null",
		 "Autorisation de paiement délivrée par la banque",
		 "null",
                 "Autorisation de paiment délivrée par la banque, sauf accord terminal",
                ]
   srv_2_list = ["Pas de restrictions de retrait, code requis",
                 "Pas de restrictions de retrait",
		 "Retrait interdit, sauf biens et services",
		 "Retrait uniquement, code requis",
		 "Retrait possible, solde créditeur requis",
		 "Retrait interdit, sauf biens et services, code requis",
		 "Pas de restrictions de retrait, code requis si possible",
		 "Retrait interdit, sauf biens et services, code requis si possible",
                ]
	
   srv_list = list(srv_str)

   srv_0 = srv_0_list[int(srv_list[0])]
   srv_1 = srv_1_list[int(srv_list[1])]
   srv_2 = srv_2_list[int(srv_list[2])]
   
   return (srv_0, srv_1, srv_2)


#--- Script ---#

#--- Efface écran ---#
os.system('clear')

#--- Passage clavier qwerty ---#
os.system('setxkbmap us')
 
#--- affichage ---#
print '\033[34m***************************************************************'
print '*************************\033[31m CB INFO \033[34m*****************************' 
print '*******************\033[33m CTRL+C pour quitter \033[34m***********************'
print '***************************************************************'   

#--- boucle ---# 
while True:

   #--- entrée exception ---#
   try:
   
      #--- variables ---#   
      date = datetime.datetime.now()
      file_1 = date.strftime("./enregistrements/%Y%m%d_%H%M%S.txt")
      file_2 = "./enregistrements/cb_info_base.txt"
      
      #--- initialisation ---#
      cb_info_regi = open(file_1, "w")
      cb_info_base = open(file_2, "a")

      #--- Entrée numéro ticket ---#
      print '\033[37mPassez une carte bancaire dans le lecteur'
      cb1_raw = raw_input("\033[31mCB1:")
      cb2_raw = raw_input("CB2:")
	  

      #--- récupération des infos ---#
      cb1_list = list(cb1_raw)
      cb2_list = list(cb2_raw)
	  
      cb1_con = cb1_list [1]
      cb1_pan = (cb1_list [02] + 
		 cb1_list [03] + 
		 cb1_list [04] + 
		 cb1_list [05] + 
		 cb1_list [06] + 
		 cb1_list [07] + 
		 cb1_list [08] + 
		 cb1_list [09] + 
		 cb1_list [10] + 
		 cb1_list [11] + 
		 cb1_list [12] + 
		 cb1_list [13] + 
		 cb1_list [14] + 
		 cb1_list [15] + 
		 cb1_list [16] + 
		 cb1_list [17]
		)
      cb1_tit = (cb1_list [19] + 
		 cb1_list [20] + 
		 cb1_list [21] + 
		 cb1_list [22] + 
	   	 cb1_list [23] + 
	         cb1_list [24] + 
		 cb1_list [25] + 
		 cb1_list [26] + 
		 cb1_list [27] + 
		 cb1_list [28] + 
		 cb1_list [29] +
                 cb1_list [30] +
                 cb1_list [31] +
                 cb1_list [32] +
                 cb1_list [33] +
                 cb1_list [34] +
                 cb1_list [35] +
                 cb1_list [36] +
                 cb1_list [37] +
                 cb1_list [38] +
                 cb1_list [39] +
                 cb1_list [40] +
                 cb1_list [41] +
                 cb1_list [42] +
                 cb1_list [43] +
                 cb1_list [44]
		 )
      cb1_yea = cb1_list [46] + cb1_list [47]
      cb1_mon = cb1_list [48] + cb1_list [49]
      cb1_srv = cb1_list [50] + cb1_list [51] + cb1_list [52]

      if cb1_con == "B":  

         #--- Conversion des infos ---#
         (pan_for)          = pan_define(cb1_pan)
         (tit_for, tit_civ) = tit_define(cb1_tit)
         (mon_for, yea_for) = exp_define(cb1_yea, cb1_mon)
         (ech_for, aut_for, ret_for) = srv_define(cb1_srv)

         #--- affichage infos  ---#
         print '\033[37m****************************************************************************'
         print ("\033[33mPAN                      : %s" % (pan_for))
         print ("Titulaire                : %s %s" % (tit_civ, tit_for))
         print ("Expiration               : %s %s" % (mon_for, yea_for))
         print ("Conditons échanges       : %s" % (ech_for))
         print ("Autorisation de paiement : %s" % (aut_for))
         print ("Autorisation de retrait  : %s" % (ret_for))
         print '\033[37m****************************************************************************'
   
         #--- récupération des données ---#
   
      
         cb_info_base.write("\nCarte enregistrée le %s/%s/%s à %s:%s" % (date.day, date.month, date.year, date.hour, date.minute))
         cb_info_base.write("\n****************************************************************************")
         cb_info_base.write("\nPAN        : %s" % (pan_for))
         cb_info_base.write("\nTitulaire  : %s %s" % (tit_civ, tit_for))
         cb_info_base.write("\nExpiration : %s %s" % (mon_for, yea_for))
         cb_info_base.write("\n****************************************************************************")
         
         cb_info_regi.write("\n%s" % (cb1_raw))
         cb_info_regi.write("\n%s" % (cb2_raw))
         cb_info_regi.write("\n+?")

      #--- Erreur ---#
      else:

         #--- affichage infos  ---#  
         print '****************************************************************************'
         print '\033[31mErreur'
         print '\033[37m****************************************************************************'

         #--- récupération des données ---
         cb_info_base.write("\nTicket enregistré le %s/%s/%s à %s:%s" % (date.day, date.month, date.year, date.hour, date.minute))
         cb_info_base.write("\n****************************************************************************")
         cb_info_base.write("\nErreur")
         cb_info_base.write("\n****************************************************************************")
		 
      cb_info_base.close()
      cb_info_regi.close()

   #--- sortie script ---#
   except KeyboardInterrupt:
      os.system('setxkbmap fr')
      print''
      os.system('clear')
      sys.exit(0)
