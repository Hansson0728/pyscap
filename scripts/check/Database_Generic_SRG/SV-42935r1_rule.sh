#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not notify appropriate individuals when account disabling actions are taken</message>'
else
	echo '<result>notchecked</result>'
fi