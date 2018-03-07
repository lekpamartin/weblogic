#############################################################
"""
 AUTEUR: Martin LEKPA
 DESCRIPTION: Script de verification du status des applications du domaine
"""
##############################################################


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


cd ('AppDeployments')
myapps=cmo.getAppDeployments()

for appName in myapps:
       domainConfig()
       cd ('/AppDeployments/'+appName.getName()+'/Targets')
       mytargets = ls(returnMap='true')
       domainRuntime()
       cd('AppRuntimeStateRuntime')
       for targetinst in mytargets:
             curstate=cmo.getCurrentState(appName.getName(),targetinst)
             print '[SUP] ', appName.getName(), ' : ', curstate
             if curstate == 'STATE_ACTIVE' :
              ERROR = ERROR + 0
             elif curstate == 'STATE_NEW' or curstate == 'STATE_PREPARED' :
              ERROR = ERROR + 1
             else :
              ERROR = ERROR + 2

print ''
print 'Code retour : ', ERROR

sys.exit(ERROR)
