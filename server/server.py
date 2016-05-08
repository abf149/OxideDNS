#!/usr/bin/python

##
#server.py
#Author: Andrew Feldman, 5/8/16
#
#Description: Dynamic DNS for remote operation of the OxidePrinter
#
#Usage: 
#
#<url>?s=<IP> saves <IP> in a local file named ip.txt
#<url>?g=<anything> serves a webpage containing the contents of ip.txt
#
#Extremely simple, no guarantees of performance.
# 

import cgi
print "Content-type: text/html\n"

#Fetch URL key/value
args=cgi.FieldStorage()
key=args.keys()[0]
value=args[cmd].value

if key=="s": #Set ip

	f=open('ip.txt','w')
    f.write(value)
	f.close()

	print "<html>" + str(value)  + " written.  </html>"
elif cmd=="g": #Get ip

	f=open('ip.txt','r')
	c=f.read()
	f.close()
    
	print "<html>" + c + "</html>"
