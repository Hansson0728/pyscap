#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS must verify there have not been unauthorized changes to the DBMS software and information: not supported</message>'
else
	echo '<result>notchecked</result>'
fi