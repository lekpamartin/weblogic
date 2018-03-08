#############################################################
"""
 AUTEUR: Martin LEKPA
 DESCRIPTION: Script de verification du status des bases du domaine
 ATTENTION : Il y a des fonction que vous pouvez activer pour demarrer,... automatiquement : deconseillé si des maintenances sont faites sur les bases
"""
##############################################################


import sys
import re

ERROR = 0

username = 'weblogic'

password = sys.argv[1]
port = sys.argv[2]
URL='t3://localhost:' + port

redirect('/tmp/startWLS.log');

try:
 connect(username,password,URL)
except:
 print '[SUP] Impossible de se connecter au server d admin : Verifier s il est demarre.'
 ERROR = ERROR + 2
 sys.exit(ERROR)


p=re.compile('Warning.*')
allServers=domainRuntimeService.getServerRuntimes();
if (len(allServers) > 0):
  for tempServer in allServers:
    jdbcServiceRT = tempServer.getJDBCServiceRuntime();
    dataSources = jdbcServiceRT.getJDBCDataSourceRuntimeMBeans();
    if (len(dataSources) > 0):
      for dataSource in dataSources:
        result=dataSource.testPool()
        m=p.match(str(result))
        if m or str(result)=='None':
          print '[SUP] '+dataSource.getName()+' : Running'
          ERROR = ERROR + 0
        elif m or 'Suspended' in str(result):
          print '[SUP] '+dataSource.getName()+' : Suspended, il faut desactiver la suspension'
          #dataSource.resume();
          ERROR = ERROR + 1
        elif m or 'not active' in str(result):
          print '[SUP] '+dataSource.getName()+' : Shutdown, doit etre demarre'
          #dataSource.start();
          ERROR = ERROR + 2
        else:
          print '[SUP] '+dataSource.getName()+' : Error : '+str(result).strip()
          ERROR = ERROR + 2

print ''
print 'Code retour : ', ERROR

sys.exit(ERROR)
