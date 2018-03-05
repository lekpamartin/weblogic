#!/bin/sh
# 
# Martin LEKPA

ERROR=0

PASSWORD=$1
PORT=${2:-7001}

OUTPUT=/tmp/check-datasource-status-${PORT}.log

cd /appli/oracle/middleware/wlserver_10.3/server/bin
. ./setWLSEnv.sh > /dev/null
java weblogic.WLST /appli/scripts/weblogic/check-datasource-status.py $PASSWORD ${PORT} > $OUTPUT

ERROR=$?

RESULT=`grep "SUP" $OUTPUT | tr -s "\n" ">"`

echo "$RESULT"
exit $ERROR
