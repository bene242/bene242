#!/bin/bash
#
# dieses Skript kann man beliebig oft ausführen
#
# Anzahl der Sicherungen die aufgehoben werden sollen
KEEP=30
BACKUPS=`find /root/mysqldumps -name "mysqldump-*.gz" | wc -l | sed 's/\ //g'`
while [ $BACKUPS -ge $KEEP ]
do
ls -tr1 /root/mysqldumps/mysqldump-*.gz | head -n 1 | xargs rm -f
BACKUPS=`expr $BACKUPS - 1`
done
DATE=`date +%Y-%m-%d--%H-%M-%S`
rm -f /root/mysqldumps/.mysqldump-${DATE}.gz_INPROGRESS
/usr/bin/mysqldump --defaults-extra-file="/root/my.cnf"  --all-databases  | gzip -c -9 > /root/mysqldumps/.mysqldump-${DATE}.gz_INPROGRESS
mv -f /root/mysqldumps/.mysqldump-${DATE}.gz_INPROGRESS /root/mysqldumps/mysqldump-${DATE}.gz
exit 0
