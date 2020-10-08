#ip sweep python

import os   

#replace ip address with your ip
ip = "0"
ips = "10.11.1." + str(ip)

for ip in range(255+1) :
 ips = "10.11.1." + str(ip)
 response = os.system("ping -c 1 " + ips )

 if response == 0:    

  print (ips, 'is up!')
 else:
  print (ips, 'is down!')
