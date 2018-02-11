 #!/bin/bash
#Auteur: @Korigan, 17/08/13 @gambit, 18/12/16/
#Ressources: Http://wiki.hackbbs.org
#Contact: irc.hackint.eu,#HackBBS
#Testé sur kubuntu 15.04 x64 raspberry B kali x32 et programmateurs scl3711 et acr122u
#Probleme d'extraction mfoc sur raspberry B+ et 2015-05-05-raspbian-wheezy quand l'interface graphique est lancée !???!
echo "[+] Creation du repertoire de travail"
cd nfc
echo "[+] Gestion des dépendances"
apt-get install libudev-dev pkg-config libusb-dev subversion autoconf openssl automake git libtool libssl-dev;
echo "[+] Décompression des archives"
tar -xvzf scl3711_-_linux_64-bit_driver.gz
tar -xvzf driver_scl3711_linux.gz
tar -xjvf pcsc-lite-1.8.14.tar.bz2
tar -xjvf libnfc-1.7.1.tar.bz2
tar -xjvf mfoc-0.10.7.tar.bz2
unzip libfreefare.zip
unzip mfcuk-094.zip
echo "[+] Installation de pcsc-lite 1.8.14"
cd pcsc-lite-1.8.14; ./configure && make && make install; cd ..
echo "[+] Installation des drivers x64 et x86"
cd sclgeneric_2.09_linux_64bit/; ./install.sh
cd scx371x_2.11_linux_32bit/; ./install.sh
echo "[+] Installation de libnfc 1.7.1 et patchage pour l'écriture du secteur O(uid0) (numéro de série)"
cd ../libnfc-1.7.1
sed -i 's/if (uiBlock == 0 \&\&/\/\/if (uiBlock == 0 \&\&/' utils/nfc-mfclassic.c
sed -i 's/continue/\/\/continue/g' utils/nfc-mfclassic.c
./configure && make && make install; cd ..
echo "[+] Gestion des conflis de drivers"
cat << EOF > /etc/modprobe.d/blacklist-libnfc.conf
blacklist pn533_usb
blacklist pn533
blacklist nfc
EOF
echo "[+] Installation de logiciel: mfoc 0.10.7"
cd mfoc-0.10.7; ./configure && make && make install; cd ..
echo "[+] Installation de logiciel: mfcuk 0.38 rev 094 DEBUGGUE !!!!"
cd mfcuk-094; autoreconf -vis && ./configure && make && make install; cd ..
echo "[+] Installation de logiciel: libfreefare"
cd libfreefare; autoreconf -vis && ./configure --prefix=/usr && make && make install; cd ..
echo "[+] Gestion d'éventuelles erreurs de dépendances"
sh -c "echo /usr/local/lib > /etc/ld.so.conf.d/usr-local-lib.conf"
ldconfig
#Pour tester, lsusb affichera le dongle scl3711 ou l'acr122u lorsque vous les brancherez
#sudo nfc-list affichera, si un badge est présent, son numéro de série ainsi que différentes informations...
#have fun !!!
