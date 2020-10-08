#ip sweep python

import os   

#and then check the response...
ip = "0"
hostname = "10.11.1." + str(ip)
#response = os.system("ping -c 1 " + hostname)

for ip in range(255+1) :
 hostname = "10.11.1." + str(ip)
 response = os.system("ping -c 1 " + hostname )

 if response == 0:    

  print (hostname, 'is up!')
 else:
  print (hostname, 'is down!')