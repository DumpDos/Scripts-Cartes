#!/usr/bin/env python 
# coding: utf-8

#--- librairies ---#
import os
import re
import sys
import time
import datetime

#--- Variables ---#
file_vigik = "keys/vigik.txt"
file_mifar = "keys/mifare.txt"

#--- fonction logo ---#

def aff_logo():
	os.system('clear')
	print"\033[34m****************************************************************************"
	print"\033[33m  __  __ _  __                 ______                     _                 "
	print" |  \/  (_)/ _|               |  ____|                   | |                "
	print" | \  / |_| |_ __ _ _ __ ___  | |__   _ __   ___ ___   __| | ___ _   _ _ __ "
	print" | |\/| | |  _/ _` | '__/ _ \ |  __| | '_ \ / __/ _ \ / _` |/ _ \ | | | '__|"
	print" | |  | | | || (_| | | |  __/ | |____| | | | (_| (_) | (_| |  __/ |_| | |   "
	print" |_|  |_|_|_| \__,_|_|  \___| |______|_| |_|\___\___/ \__,_|\___|\__,_|_|   "
	print" "
	print"\033[34m****************************************************************************"
	print"\033[33mBeta V0.1, DumpDos 2018, Ctrl+C Pour quitter"
	print""

#--- fonction vérification device ---#
def nfc_devi():

	raw_devi = os.popen("nfc-list").read()
	int_device_emp = raw_devi.find('found')
	int_device_ful = raw_devi.find('UID')

	if int_device_emp == -1 or int_device_ful == -1:
		str_devi = raw_devi[39:-1]
		print ("\033[32mLecteur NFC détecté : %s " % (str_devi))
		print""
		
	else:
		print ("\033[31mAucun lecteur détecté")
		print""

#--- fonction lecture badge ---#

def read_devi(type, keys_file, action, file_name):

	date = datetime.datetime.now()
	file_name_time = date.strftime("./dumps/%Y%m%d_%H%M%S.dmp")
	
	if type == 'm':
		keys_file_type = file_mifar

	elif type == 'v':
		keys_file_type = file_vigik

	elif type == 'f':
		keys_file_type = keys_file

	if file_name == '':

		os.system('mfoc -P 500 -f %s -O %s' % (keys_file_type, file_name_time))
		aff_logo()
	
	else:
		aff_logo()
		print""
		print"\033[36mCopie du Badge en cours..."
		os.system('mfoc -P 500 -f %s -O %s' % (keys_file_type, file_name))
	
	return (file_name)

#--- Script ---#

#--- Efface écran ---#
os.system('clear')

#--- Initialisation ---#

aff_logo()
nfc_devi()

#--- Récupération des données ---#

try:

	print"\033[36m#===[Type de badge]===#:"
	print"\033[37m"
	print"Mifare Classic  : m"
	print"Vigik           : v"
	print"Fichier de clés : f"
	print""
	type_raw = raw_input("\033[33mType : ")
	
	aff_logo()
		
	if type_raw == 'f':
		print""
		keys_raw = raw_input("\033[33mEmplacement du fichier de clés : ")
		
	else:
		keys_raw = 'none'

	
	print"\033[36m#====[Actions]====#:"
	print"\033[37m"
	print"Lecture du badge : r"
	print"Copie du badge   : w"
	print"Copies multiples : m"
	print"Creation         : c"
	print""
	actn_raw = raw_input("\033[33mType : ")

	if actn_raw == 'r':
		print""
		file_nam = raw_input("\033[33mNom du dump : ")
		read_devi(type_raw, keys_raw, actn_raw, file_nam)

	elif actn_raw == 'c':
		print""
		file_raw = raw_input("\033[33mEmplacement du fichier .dmp : ")

except KeyboardInterrupt:
	print''
	os.system('clear')
	sys.exit(0)
