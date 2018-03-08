#!/bin/bash
#
# Weblogic      Startup script
#
# chkconfig: - 85 15
# description: Administratation console

SERVER=<ADMIN NAME>
PORT=<ADMIN PORT>
SLEEP=5

case "$1" in
	start)
		echo "** Demarrage de $SERVER **"
		su - oracle -c "/REP/middleware/user_projects/domains/<DOMAINE>/bin/startWebLogic.sh 2>  /LOGS/weblogic/$1-$SERVER.log 1>&2 &"
		while !(: < /dev/tcp/127.0.0.1/$PORT) 2>/dev/null
		do
			echo "** Attente du demarrage de $SERVER **"
			sleep $SLEEP
		done
		cat /LOGS/weblogic/$1-$SERVER.log
	;;


	stop)
		echo "** Stoping Admin Server **"
		su - oracle -c "/REP/middleware/user_projects/domains/<DOMAINE>/bin/stopWebLogic.sh 2>  /LOGS/weblogic/$1-$SERVER.log 1>&2 &"
		while (: < /dev/tcp/127.0.0.1/$PORT) 2>/dev/null
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