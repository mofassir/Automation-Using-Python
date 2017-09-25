import string, time, sys, datetime,Tkinter, exceptions
 

ix = Ixia(79, user='mh')

ix.initPort('port1',07,1)
ix.initPort('port2',07,3)
#ix.initPort('port3',16,1)
#ix.initPort('port4',7,2)
#ix.initPort('port5',7,3)
#ix.initPort('port6',7,4)

portList=['port1','port2']
#portList=['port1']
#portList=['port1','port2','port3']
#portList=['watch1','watch2','port1','port2']
print "--------", len(sys.argv)
while True:	
	#Default to narrow format - my phone (date on separate line)
	#Add any argument, and put everything on the same line
	if len(sys.argv)<1:
		print  time.strftime("%H:%M:%S: "),
	else:	
		print  time.strftime("%H:%M:%S: ") 
	for port in portList:
	        #print  '%12dTx'%ix.getTxPktRate(ix.portDict['port1']),
                #print  '%7dRx'%ix.getRxPktRate(ix.portDict['port2']),
	        
		print  '%7dTx'%ix.getTxPktRate(ix.portDict['port2']),
		print  '%7dRx'%ix.getRxPktRate(ix.portDict['port2']),

	        print  '%7dRx'%ix.getRxPktRate(ix.portDict['port1']),
		print  '%7dTx'%ix.getTxPktRate(ix.portDict['port1']),
	 

    		#print  '%7dRx'%ix.getRxPktRate(ix.portDict['port2']),

      	        print
#	print time.strftime("%H:%M:%S: ") + '%8d %8d %8d'%(ix.getRxPktRate(ix.portDict['port1']),ix.getRxPktRate(ix.portDict['port2']),ix.getRxPktRate(ix.portDict['port3']))
	time.sleep(1)
