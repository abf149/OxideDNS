##
#agent.py
#Author: Andrew Feldman, 5/8/16
#
#Description: Dynamic DNS agent script to register OxidePrinter IP with OxideDNS server
#
#Usage: Configure to run as a background process at startup. Assumes the OxidePrinter is connected
#to a Linux-like controller.
#
#python agent.py 1800 &
#
#where 1800 is the period in seconds between IP updates. The default is 30min=1800s
#

import sys
import socket
import time

period_seconds=1800
if len(sys.argv)==2: period_seconds=int(float(sys.argv[1])) #Convert to float and truncate to accommodate floating-point input
#For any other number of terminal arguments, ignore and assume default period

while(True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #From http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    #May fail if ethernet and wifi are connected
    ip=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

    print ("https://abf149.scripts.mit.edu/oxidedns/demo.py?s="+str(ip),443)
    
    sock.connect(("https://abf149.scripts.mit.edu/oxidedns/demo.py?s="+str(ip),443))
    
    rbuf=sock.recv(1024)
    
    print rbuf
    
    sock.close()
    
    time.sleep(period_seconds)



