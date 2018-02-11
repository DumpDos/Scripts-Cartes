#!/bin/bash

#####################################################################$
# vigik_encoder.sh
# DumpDos
#####################################################################$

clear

echo 'Placez le badge à copier sur le lecteur et appuiez sur une touche'
read -n 1 ch

mfoc -P 500 -k a22ae129c013 -k 484558414354 -k 49FAE4E3849F -k 38FCF33072E0 -k 8AD5517B4B18 -k 509359F131B1 -k 6C78928E1317 -k AA0720018738 -k A6CAC2886412 -k 62D0C424ED8E -k E64A986A5D94 -k 8FA1D601D0A2 -k 89347350BD36 -k 66D2B7DC39EF -k 6BC1E1AE547D -k 22729A9BD40F -k 484558414354 -O carte-originale.dmp

clear

echo 'Placez un badge vierge sur le lecteur et appuiez sur une touche'
read -n 1 ch

mfoc -P 500 -O carte-vierge.dmp

sleep 3

nfc-mfclassic W a carte-originale.dmp carte-vierge.dmp
