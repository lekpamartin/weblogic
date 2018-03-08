#!/bin/bash
#
# Weblogic      Startup script
#
# chkconfig: - 86 15
# description: Managed Server

SERVER=<MANAGED NAME>
PORT=<MANAGED PORT>
SLEEP=5

case "$1" in
	start)
		echo "** Demarrage de $SERVER **"
		su - oracle -c "/REP/middleware/user_projects/domains/<DOMAINE>/bin/startManagedWebLogic.sh $SERVER 2> /LOGS/weblogic/$1-$SERVER.log 1>&2 &"
		while !(: < /dev/tcp/127.0.0.1/$PORT) 2>/dev/null
		do
			echo "** Attente du demarrage de $SERVER **"
			sleep $SLEEP
		done
		cat /LOGS/weblogic/$1-$SERVER.log
	;;


	stop)
		echo "** Arret de $SERVER **"
		su - oracle -c "/REP/middleware/user_projects/domains/<DOMAINE>/bin/stopManagedWebLogic.sh $SERVER  2> /LOGS/weblogic/$1-$SERVER.log 1>&2 &"
		while !(: < /dev/tcp/127.0.0.1/$PORT) 2>/dev/null
		do
			echo "** Attente de l arret de $SERVER **"
			sleep $SLEEP
		done
		cat /LOGS/weblogic/$1-$SERVER.log
	;;


	*)
		echo "Usage: $0 {start|stop}"
		exit 1
	;;

esac

exit $?