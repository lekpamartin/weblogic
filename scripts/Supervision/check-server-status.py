#############################################################
"""
 AUTEUR: Martin LEKPA
 DESCRIPTION: Script de verification du status des serveurs du domaine
"""
##############################################################

def serverStatus(server):
 cd('/ServerLifeCycleRuntimes/' + server.getName())
 return cmo.getState()
import sys

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


servers = cmo.getServers()
domainRuntime()
print '#### Weblogic Statut ####'

for server in servers:
 serverState = serverStatus(server)
 print '[SUP] ', str(server.getName()), ' : ', serverState
 if serverState == 'RUNNING' :
  ERROR = ERROR + 0
 elif serverState == 'STARTING' :
  ERROR = ERROR + 1
 else :
  ERROR = ERROR + 2

print ''
disconnect()
stopRedirect()

print ''
print 'Code retour : ', ERROR
sys.exit(ERROR)
