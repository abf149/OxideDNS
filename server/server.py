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

key=""
value=""
if len(args.keys())>0:
    key=args.keys()[0]
    value=args[key].value

if key=="s": #Set ip

	f=open('ip.txt','w')
    	f.write(value)
	f.close()

	print "<html>" + str(value)  + " written.  </html>"
else: #Get ip

	f=open('ip.txt','r')
	ip=f.read()
	f.close()
    
	print str(ip)
